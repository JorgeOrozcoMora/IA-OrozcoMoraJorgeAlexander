import json
import re
from pathlib import Path
import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify

app = Flask(__name__)

# Definición de rutas base de recursos
ROOT = Path(__file__).resolve().parent / "modelo"
model = None
stoi = {}
itos = {}
BLOCK_SIZE = 64

# Carga el Modelo para Usarlo
def load_model_and_meta():
    """Carga los artefactos de la red neuronal y configura los mapeos de tokens"""
    global model, stoi, itos, BLOCK_SIZE

    meta_path = ROOT / "meta.json"
    model_path = ROOT / "asistente.keras"

    if not meta_path.is_file() or not model_path.is_file():
        raise FileNotFoundError("No se encontraron los archivos del modelo. Ejecuta entrenamiento.py")

    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)

    BLOCK_SIZE = int(meta["block_size"])
    chars = meta["chars"]

    stoi = {c: i for i, c in enumerate(chars)}
    itos = {i: c for c, i in stoi.items()}

    model = tf.keras.models.load_model(model_path)

    model.predict(np.zeros((1, BLOCK_SIZE)))

    print("-> Servidor Flask: Modelo cargado correctamente en memoria.")

# Genera Texto a partir de lo que el Usuario Escribio
def predict_completion(prefix, max_new=40, temperature=0.3):
    """Autocompletado optimizado: rápido + cortes inteligentes + detección de métodos"""

    ids = [stoi.get(c, stoi.get(' ', 0)) for c in prefix]
    rng = np.random.default_rng()

    prefix_limpio = prefix.lower().strip()

    # Detectar estructuras de control
    es_estructura_control = any(k in prefix_limpio for k in ["if", "for", "while", "switch"])

    # Detectar apertura de método
    patron_metodo = r'\b\w+\s+\w+\s*\($'
    es_metodo = re.search(patron_metodo, prefix_limpio) is not None

    # Buffer reutilizable
    input_buffer = np.zeros((1, BLOCK_SIZE), dtype=np.int32)

    max_steps = min(max_new, 20)

    for _ in range(max_steps):
        x = ids[-BLOCK_SIZE:]

        # Padding eficiente
        if len(x) < BLOCK_SIZE:
            pad_val = ids[0] if len(ids) > 0 else 0
            x = [pad_val] * (BLOCK_SIZE - len(x)) + x

        input_buffer[0, :] = x

        # Predicción rápida
        preds = model.predict_on_batch(input_buffer)
        logits = preds[0, -1, :]

        # Temperatura + estabilidad
        logits = logits / max(temperature, 1e-6)
        logits = logits - logits.max()

        probs = np.exp(logits) / np.sum(np.exp(logits))
        next_id = int(rng.choice(len(probs), p=probs))
        ids.append(next_id)

        char_generado = itos.get(next_id, ' ')

        # Método → cerrar y abrir bloque
        if char_generado == ')' and es_metodo:
            ids.append(stoi.get('{', 0))
            break

        # Estructuras de control
        if char_generado == ')' and es_estructura_control:
            break

        # Paradas comunes
        if char_generado in ('\n', ';', '}'):
            break

    full_text = "".join([itos.get(i, ' ') for i in ids])
    return full_text[len(prefix):]

# Devuelve una Prediccion
@app.route('/api/complete', methods=['POST'])
def complete_endpoint():
    """Endpoint para autocompletado directo de código en la posición del cursor"""
    data = request.get_json() or {}

    prefix = data.get("prefix", "")
    max_new = int(data.get("max_new", 20))
    temperature = float(data.get("temperature", 0.3))

    if not prefix:
        return jsonify({"ok": False, "error": "El campo 'prefix' es obligatorio."}), 400

    try:
        suffix = predict_completion(prefix, max_new, temperature)
        return jsonify({"ok": True, "suffix": suffix})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

# Devuelve Varias Sugerencias Diferentes
@app.route('/api/suggest', methods=['POST'])
def suggest_endpoint():
    """Endpoint para obtener una lista de predicciones en el panel QuickPick del editor"""
    data = request.get_json() or {}

    prefix = data.get("prefix", "")
    n = int(data.get("n", 3))

    if not prefix:
        return jsonify({"ok": False, "error": "El campo 'prefix' es obligatorio."}), 400

    try:
        suggestions = []
        seen = set()

        for i in range(n * 2):
            suffix = predict_completion(prefix, max_new=15, temperature=0.2 + (i * 0.1))
            first_line = suffix.split("\n")[0]

            candidate = prefix + first_line

            if candidate not in seen and len(first_line.strip()) > 0:
                seen.add(candidate)
                suggestions.append(candidate)

            if len(suggestions) >= n:
                break

        return jsonify({"ok": True, "suggestions": suggestions})

    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500


if __name__ == '__main__':
    load_model_and_meta()
    app.run(host='127.0.0.1', port=5000, debug=False)