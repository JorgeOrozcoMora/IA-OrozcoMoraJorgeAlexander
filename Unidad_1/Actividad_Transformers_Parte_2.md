## ACTIVIDAD MANUAL PARTE 2 — ENTENDER TRANSFORMERS
**Orozco Mora Jorge Alexander**  
*NC: 22120703*

---
### Actividad 6: Matriz de Atencion Completa
#### Frase de trabajo (5 palabras)
**LA · NIÑA · PEQUEÑA · COME · FRUTA**

#### Paso 1 — Puntuar todas las filas
Para cada palabra de la fila izquierda, puntúa de **0 a 10** cuánto te importa cada columna (incluyéndose a sí misma si tiene sentido).

|  | LA | NIÑA | PEQUEÑA | COME | FRUTA |
|------------------|----|------|---------|------|-------|
| LA               | 2  | 9    | 6       | 1    | 2     |
| NIÑA             | 6  | 2    | 8       | 9    | 5     |
| PEQUEÑA          | 3  | 9    | 2       | 4    | 3     |
| COME             | 1  | 8    | 5       | 2    | 9     |
| FRUTA            | 1  | 6    | 3       | 9    | 2     |

#### Paso 2 — Normalizar cada fila por separado
|  | LA | NIÑA | PEQUEÑA | COME | FRUTA | Suma |
|------------------|----|------|---------|------|-------|------|
| LA               | 10% | 45% | 30% | 5% | 10% | 100% |
| NIÑA             | 20% | 7% | 27% | 30% | 16% | 100% |
| PEQUEÑA          | 14% | 43% | 10% | 19% | 14% | 100% |
| COME             | 4% | 32% | 20% | 8% | 36% | 100% |
| FRUTA            | 5% | 29% | 14% | 43% | 9% | 100% |

#### Paso 3 — Observación
Patrón principal:

- LA → NIÑA  
- PEQUEÑA → NIÑA  
- NIÑA → COME  
- COME → FRUTA  
- FRUTA → COME 

#### Preguntas de análisis

**¿La fila de COME se parece a la de FRUTA? ¿Por qué deberían diferir?**
Se parecen, pero no son iguales:
- COME se enfoca en FRUTA (objeto) y NIÑA (sujeto)
- FRUTA se enfoca más en COME (verbo)  
El verbo conecta, el objeto depende del verbo

**¿Alguna fila reparte atención casi pareja (~20%)?**
No en este caso. 
**¿Qué palabra podría ser esa y por qué?** Si ocurriera, sería una palabra como: “y”, “de”, “en”.  
Porque no tienen una relación dominante

**Si la frase tuviera 100 palabras, ¿cuántas celdas tendría la tabla?**
100 × 100 = 10,000 celdas   
**¿Por qué eso explica que textos muy largos cuestan más memoria?** Por eso textos largos consumen más memoria

### Actividad 7 - Softmax a Mano (De Puntajes a Probabilidades)
#### Situación

La palabra **PEQUEÑA** tiene estos puntajes:

| Hacia → | NIÑA | PEQUEÑA | COME | FRUTA |
|--------|------|---------|------|-------|
| Puntaje | 3.0 | 0.5 | 0.2 | 1.0 |

#### Paso 1 — Exponencial

Se calcula: \[e^x\]

| Palabra | Puntaje | \( e^x \approx \) |
|--------|--------|------------------|
| NIÑA   | 3.0    | 20.09 |
| PEQUEÑA| 0.5    | 1.65  |
| COME   | 0.2    | 1.22  |
| FRUTA  | 1.0    | 2.72  |
| **Suma** |      | **25.68** |

#### Paso 2 — Normalización

Se divide cada valor entre la suma:

\[\frac{e^x}{\text{suma}}\]

| Palabra | Cálculo | ≈ % |
|--------|---------|-----|
| NIÑA   | 20.09 / 25.68 | **78%** |
| PEQUEÑA| 1.65 / 25.68  | 6% |
| COME   | 1.22 / 25.68  | 5% |
| FRUTA  | 2.72 / 25.68  | 11% |

#### Paso 3 — Interpretación
- NIÑA domina claramente (78%)
- Aunque COME no era el menor puntaje, su porcentaje final es bajo
- Esto pasa porque softmax amplifica diferencias

Si NIÑA tuviera un puntaje mucho mayor (ej. 10):
- Su porcentaje sería casi 100%
- Esto se llama saturación

#### Pregunta

**¿Por qué no basta con dividir los puntajes entre su suma?** Porque:

1. No maneja bien números negativos
2. No resalta diferencias importantes
3. No modela bien la “competencia”

### Actividad 8 - Mezcla de "Vectores Contenido" (Values)
#### Datos (Coordenadas de Cada palabra en un "Mapa de Significado" Ficticio)

| Palabra  | Vector V = (x, y) |
|----------|-------------------|
| LA       | (1, 1)            |
| NIÑA     | (4, 5)            |
| PEQUEÑA  | (3, 4)            |
| COME     | (5, 1)            |
| FRUTA    | (6, 3)            |

#### Usa los % de la Fila de COME que Obtuviste en Actividad 6 (o estos de ejemplos si no los tienes):

| Hacia   | % |
|---------|----|
| LA      | 5% |
| NIÑA    | 35% |
| PEQUEÑA | 10% |
| COME    | 10% |
| FRUTA   | 40% |

#### Paso 1 — Convertir % a decimales (0.05, 0.35)

| Palabra  | Peso |
|----------|------|
| LA       | 0.05 |
| NIÑA     | 0.35 |
| PEQUEÑA  | 0.10 |
| COME     | 0.10 |
| FRUTA    | 0.40 |

### Paso 2 — Multiplica Cada Vector por su Peso y Sumar
Fórmula:\[\text{salida} = \sum (\text{peso} \times \text{vector})\]

| Palabra  | Cálculo | Resultado |
|----------|--------|----------|
| LA       | 0.05 × (1,1) | (0.05, 0.05) |
| NIÑA     | 0.35 × (4,5) | (1.40, 1.75) |
| PEQUEÑA  | 0.10 × (3,4) | (0.30, 0.40) |
| COME     | 0.10 × (5,1) | (0.50, 0.10) |
| FRUTA    | 0.40 × (6,3) | (2.40, 1.20) |

- Coordenada x: \[0.05 + 1.40 + 0.30 + 0.50 + 2.40 = 4.65\]
- Coordenada y: \[0.05 + 1.75 + 0.40 + 0.10 + 1.20 = 3.50\]
- Resultado Final: \[\text{salida} = (4.65,\ 3.50)\]

#### Paso 3 — Dibuja en Papel
- Coloca los puntos de cada palabra en el plano
- Dibuja el vector salida desde el origen

Resultado esperado:
- El vector final queda más cerca de FRUTA y NIÑA
- Porque tienen mayor peso (40% y 35%)

### Actividad 9 - Mascara de Padding (Frases de Distinta Longitud)
#### Lote de frases (longitud fija = 5)

- Frase 1: EL   GATO   COME   —   —  
- Frase 2: LA   NIÑA   PEQUEÑA   COME   FRUTA  
(— = PAD, relleno)

#### Paso 1 — Matriz 5×5 para Frase 1

Marcamos con **P** las filas/columnas que corresponden a PAD (posiciones 4 y 5).

|  | EL | GATO | COME | — (P) | — (P) |
|------------------|----|------|------|-------|-------|
| EL               |    |      |      |   P   |   P   |
| GATO             |    |      |      |   P   |   P   |
| COME             |    |      |      |   P   |   P   |
| — (P)            | P  |  P   |  P   |   P   |   P   |
| — (P)            | P  |  P   |  P   |   P   |   P   |

Las filas 4 y 5 son PAD, y las columnas 4 y 5 son PAD.

#### Paso 2 — Regla

**Regla:** “Una palabra real no puede prestar atención a PAD”.

Tachamos las celdas donde:
- la **fila es palabra real** (EL, GATO, COME)  
- la **columna es PAD** (posiciones 4 y 5)

| | EL | GATO | COME | — (P) | — (P) |
|------------------|----|------|------|-------|-------|
| EL               |    |      |      |  X    |  X    |
| GATO             |    |      |      |  X    |  X    |
| COME             |    |      |      |  X    |  X    |
| — (P)            | P  |  P   |  P   |   P   |   P   |
| — (P)            | P  |  P   |  P   |   P   |   P   |

Esas celdas se anulan antes del softmax (máscara de atención).

#### Paso 3 — Preguntas

**¿Por qué Frase 2 no necesita tantas celdas tachadas?**
Porque no tiene PAD (todas sus posiciones son palabras reales). Por lo tanto, no hay columnas de relleno que bloquear.

**¿Qué pasaría si el modelo atendiera mucho a PAD?**
- Aprendería **patrones falsos** basados en el relleno  
- Desperdiciaría atención en información que **no tiene significado**  
- Reduciría la calidad del aprendizaje y las predicciones  

### Actividad 10 - Atencion Cruzada (De Puntajes a Probabilidades)
#### Datos
**Encoder (español):**  
YO   QUIERO   CAFE  

**Decoder (inglés):**  
I   WANT   ___ 

#### Paso 1 — Matriz 3×3

Filas: I, WANT, (palabra 3 por escribir)  
Columnas: YO, QUIERO, CAFE  

| Desde (inglés) ↓ / Español → | YO | QUIERO | CAFE |
|-----------------------------|----|--------|------|
| Palabra 3 (por escribir)    | 1  | 3      | 9    |

#### Paso 2 - A Porcentajes y Responde

**¿CAFE debería ganar? ¿Por qué?** Sí. Porque la palabra que falta es "coffee", y:
- CAFE es su traducción directa
- Tiene la relación semántica más fuerte


**¿La fila de I podría mirar mucho a YO? ¿Tiene sentido?** Sí, tiene sentido.
- I = YO son equivalentes directos
- Es normal que la primera palabra en inglés mire fuertemente a su equivalente en español

**Diferencia clave: en self-attention las columnas y filas son el mismo idioma; aquí entrada y salida son columnas distintas.**

- **Self-attention**:
  - Filas y columnas = mismo idioma
  - Ejemplo: inglés → inglés

- **Cross-attention**:
  - Filas = idioma de salida (inglés)
  - Columnas = idioma de entrada (español)	

### Actividad 11 - Adivinar la Palabra Tapada (Estilo BERT / MLM)
#### Frase con hueco
EL   GATO   ___   PESCADO

#### Paso 1 — Candidatos
- COME  
- DUERME  
- VERDE  
- RAPIDO  

#### Paso 2 — Sin Mirar "Solucion"
Para el hueco, puntúa cada candidato del 0 al 10 según compatibilidad con EL, GATO, PESCADO (no con reglas gramaticales memorizadas solamente: piensa en sentido):

| Candidato | Puntaje |
|----------|--------|
| COME     | 10     |
| DUERME   | 4      |
| VERDE    | 1      |
| RAPIDO   | 2      |

## Paso 3 — Convierte a % (Softmax Manual o Reparto Proporcional)

Suma = 10 + 4 + 1 + 2 = 17  

| Candidato | Cálculo | % |
|----------|--------|---|
| COME     | 10 / 17 | 59% |
| DUERME   | 4 / 17  | 24% |
| VERDE    | 1 / 17  | 6%  |
| RAPIDO   | 2 / 17  | 11% |

## Paso 4 — Reflexión Escrita (5 Lineas)
**¿Por qué COME debería superar a VERDE?**
COME supera a VERDE porque tiene coherencia directa con GATO y PESCADO: un gato come pescado, mientras que "verde" no encaja semánticamente en la acción.

**¿DUERME podría tener algo de sentido?¿Qué atención habría entre GATO y DUERME?**
DUERME podría tener algo de sentido porque un gato puede dormir, pero pierde fuerza porque no conecta con PESCADO. La atención entre GATO y DUERME sería moderada, pero baja con PESCADO.

**¿Por qué BERT necesita ver PESCADO (derecha) aunque el hueco esté en el centro? (Bidireccional = contexto completo.)**  
BERT necesita ver PESCADO aunque esté a la derecha porque esa palabra ayuda a determinar la acción más probable. Sin ese contexto, varias opciones podrían parecer válidas. Esto muestra que BERT es bidireccional: usa tanto el contexto izquierdo como el derecho para tomar una mejor decisión.
El modelo no solo sigue reglas gramaticales, sino que aprende relaciones de significado entre palabras.
### Actividad 12 - Dos Capas de Atencion (Refinar la Presentacion)
#### Version Simplificada (Perfiles 1-5 en Lugar de 768 Numeros)

| Palabra  | Perfil |
|----------|--------|
| LA       | 2      |
| NIÑA     | 6      |
| PEQUEÑA  | 5      |
| COME     | 7      |
| FRUTA    | 8      |

#### Paso 1 — Segunda Ronda Solo Para FRUTA (capa 2)
Criterio:
- FRUTA (objeto) debe mirar fuerte al verbo (COME)
- También puede mirar al sujeto (NIÑA)
- Menor atención a modificadores o determinantes

| Desde FRUTA → | LA | NIÑA | PEQUEÑA | COME | FRUTA |
|---------------|----|------|---------|------|-------|
| Puntaje (0–10)| 1  | 6    | 3       | 10   | 4     |


#### Paso 2 — Escribe una Frase
En la segunda capa, FRUTA ya “sabe” que COME tiene perfil 7 porque la primera capa conectó verbo–objeto.

### Actividad 13 - RNN vs Transformer: Contar Conexiones
#### Dibuja 5 nodos en línea: A — B — C — D — E
##### Modo RNN (solo vecino anterior para pasar mensaje)

Enlaces:
A → B  
B → C  
C → D  
D → E  

Total: **4 enlaces** para que la información viaje de A a E.

## Modo atención (una capa, todos miran todos — sin máscara)
Cada palabra puede mirar a todas las demás (incluyéndose):
\[5 \times 5 = 25 \text{ celdas}\]

#### Preguntas

**¿Si A debe influir en E, cuántos “saltos” en RNN? ¿Y en una capa de atención?**
- En **RNN**: 4 saltos (A → B → C → D → E)  
- En **atención**: 1 salto (A puede mirar directamente a E en la misma capa)

**¿Cuál crece más rápido si la frase tiene 100 palabras: 100 enlaces secuenciales o 10,000 celdas?**
- RNN: crece de forma **lineal** → 100 enlaces  
- Atención: crece de forma **cuadrática** → \[100 \times 100 = 10,000 \text{ celdas}\]

**¿Por qué aun así usamos Transformers y no solo RNN?**
- Permiten paralelismo: todas las relaciones se calculan al mismo tiempo  
- Capturan mejor dependencias largas (no necesitan pasar por cada palabra)  
- Mejor calidad de representación del contexto  

### Actividad 14 - Softmax a Mano (Evitar Saturacion)
#### Ejercicio numérico
Vector de puntajes:
- Sin escalar: [8, 2, 2, 2]  
- Con escalar (÷2): [4, 1, 1, 1]

#### En papel
##### 1. Softmax aproximado de [8, 2, 2, 2]
Exponenciales aproximadas:

- e⁸ ≈ 2981  
- e² ≈ 7.39  

Suma total:\[2981 + 7.39 + 7.39 + 7.39 \approx 3003\]

Porcentajes:

| Valor | Cálculo | % |
|------|--------|---|
| 8    | 2981 / 3003 | **99%** |
| 2    | 7.39 / 3003 | 0.25% |
| 2    | 7.39 / 3003 | 0.25% |
| 2    | 7.39 / 3003 | 0.25% |

##### 2. Softmax de [4, 1, 1, 1]

Exponenciales aproximadas:

- e⁴ ≈ 54.6  
- e¹ ≈ 2.72  

Suma total: \[54.6 + 2.72 + 2.72 + 2.72 \approx 62.76\]

Porcentajes:

| Valor | Cálculo | % |
|------|--------|---|
| 4    | 54.6 / 62.76 | **87%** |
| 1    | 2.72 / 62.76 | 4% |
| 1    | 2.72 / 62.76 | 4% |
| 1    | 2.72 / 62.76 | 4% |

##### Comparación
Sí, la palabra con mayor puntaje sigue ganando en ambos casos, pero:
- Sin escalar: ~99% (dominancia extrema)  
- Con escalar: ~87% (más equilibrado)