import os
import json
import numpy as np
import tensorflow as tf

tf.keras.utils.set_random_seed(42)

# Cargar el dataset en C
with open("dataset.c", "r", encoding="utf-8") as f:
    corpus = f.read()

# Construir el Vocabulario de Caracteres
chars = sorted(set(corpus))
stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for ch, i in stoi.items()}
VOCAB_SIZE = len(chars)

print(f"VOCAB_SIZE: {VOCAB_SIZE} | Caracteres totales en corpus: {len(corpus)}")

# Codificar el texto plano a índices numéricos
SEQ = np.array([stoi[c] for c in corpus], dtype=np.int64)

# Crear Datos de Entrenamiento
BLOCK_SIZE = 64 
X_rows, Y_rows = [], []
for i in range(0, len(SEQ) - BLOCK_SIZE):
    X_rows.append(SEQ[i : i + BLOCK_SIZE])
    Y_rows.append(SEQ[i + 1 : i + 1 + BLOCK_SIZE])

X = np.stack(X_rows)
Y = np.stack(Y_rows)
print(f"Dimensiones de tensores - Entrada X: {X.shape} | Objetivos Y: {Y.shape}")

EMBED_DIM = 64     
HIDDEN_UNITS = 128  

# Modelo
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(BLOCK_SIZE,)),
    tf.keras.layers.Embedding(VOCAB_SIZE, EMBED_DIM),
    tf.keras.layers.SimpleRNN(HIDDEN_UNITS, activation="tanh", return_sequences=True, dropout=0.1),
    tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(VOCAB_SIZE))
])

# Compilación del Modelo
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
)

model.summary()

# Entrenamiento del Modelo
EPOCHS = 120  
BATCH_SIZE = 32
print("\n--- Iniciando Entrenamiento del Modelo ---")
history = model.fit(X, Y, epochs=EPOCHS, batch_size=BATCH_SIZE, verbose=1)

# Guarda el Modelo
os.makedirs("modelo", exist_ok=True)
model.save("modelo/asistente.keras")

# Guardamos la Meta
meta = {
    "block_size": BLOCK_SIZE,
    "chars": chars
}
with open("modelo/meta.json", "w", encoding="utf-8") as fj:
    json.dump(meta, fj, ensure_ascii=False)

print("\nEntrenamiento Terminado")