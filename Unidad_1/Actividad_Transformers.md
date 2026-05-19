## ACTIVIDAD MANUAL — ENTENDER TRANSFORMERS SIN COMPUTADORA
**Orozco Mora Jorge Alexander**  
*NC: 22120703*

---
### Actividad 1: La Matriz de Atencion
#### Enunciado
Frase corta (4 palabras):  
**EL   GATO   COME   PESCADO**

Imagina que eres la palabra **COME** y quieres entender qué haces en la oración.  
Puntúa del 0 al 10 cuánto te “importa” cada palabra para entenderte (10 = muchísimo).


|  | EL | GATO | COME | PESCADO |
|--------------|----|------|------|---------|
| COME →       | 2  | 9    | 5    | 10      |

#### Paso 2 — Convertir a porcentajes (mini-softmax)

**Puntuaciones elegidas:**
- EL = 2  
- GATO = 9  
- COME = 5  
- PESCADO = 10  

**Suma total:**  
2 + 9 + 5 + 10 = **26**

##### Tabla de resultados

| Palabra  | Puntuación | ÷ Suma (26) | × 100 ≈ % |
|----------|-----------|-------------|-----------|
| EL       | 2         | 2/26        | 7.69 %    |
| GATO     | 9         | 9/26        | 34.62 %   |
| COME     | 5         | 5/26        | 19.23 %   |
| PESCADO  | 10        | 10/26       | 38.46 %   |
| **Total**| **26**    | —           | **100 %** |

#### Paso 3 — Interpretacion

Le di más atención a PESCADO, y sí tiene sentido porque es el objeto directo del verbo “come” y completa su significado.

**Pregunta de Cierre**  
No sería igual, porque como PESCADO (objeto) pondría más atención en COME para saber qué acción me afecta y menos en palabras como EL, ya que no influyen tanto en mi significado.

### Actividad 2: La Palabra Ambigua (Dos Contextos)
#### Frase A
**FUIMOS   AL   BANCO   DEL   RIO**

##### Fila de BANCO (puntuaciones)
- FUIMOS = 3  
- AL = 2  
- BANCO = 4  
- DEL = 6  
- RIO = 10  

**Suma total:** 25

##### Porcentajes

| Palabra | Puntuación | ÷ Suma (25) | × 100 ≈ % |
|---------|-----------|-------------|-----------|
| FUIMOS  | 3         | 3/25        | 12 %      |
| AL      | 2         | 2/25        | 8 %       |
| BANCO   | 4         | 4/25        | 16 %      |
| DEL     | 6         | 6/25        | 24 %      |
| RIO     | 10        | 10/25       | 40 %      |
| **Total** | **25**  | —           | **100 %** |

#### Frase B
**FUIMOS   AL   BANCO   A   SACAR   DINERO**

##### Fila de BANCO (puntuaciones)
- FUIMOS = 3  
- AL = 2  
- BANCO = 4  
- A = 3  
- SACAR = 8  
- DINERO = 10  

**Suma total:** 30

##### Porcentajes

| Palabra | Puntuación | ÷ Suma (30) | × 100 ≈ % |
|---------|-----------|-------------|-----------|
| FUIMOS  | 3         | 3/30        | 10 %      |
| AL      | 2         | 2/30        | 6.67 %    |
| BANCO   | 4         | 4/30        | 13.33 %   |
| A       | 3         | 3/30        | 10 %      |
| SACAR   | 8         | 8/30        | 26.67 %   |
| DINERO  | 10        | 10/30       | 33.33 %   |
| **Total** | **30**  | —           | **100 %** |

#### Preguntas

**¿En cuál frase BANCO le da más puntos a “RIO” / “DEL”?**  
En la Frase A.

**¿En cuál le da más a “DINERO” / “SACAR”?**  
En la Frase B.

#### Explicación
La palabra **BANCO** cambia su significado según el contexto.  
En la Frase A se relaciona con un lugar natural (río), mientras que en la Frase B se refiere a una institución financiera.  
Esto muestra cómo el contexto cambia la atención, como en un Transformer.

### Actividad 3: Mascara Causal (No Hacer Trampa)
#### Cuadrícula 4×4

Filas = palabra que “pregunta”  
Columnas = palabra a la que mira  

| Pregunta \ Mira | EL | GATO | COME | PESCADO |
|-----------------|----|------|------|---------|
| EL              | ✓  | ✗    | ✗    | ✗       |
| GATO            | ✓  | ✓    | ✗    | ✗       |
| COME            | ✓  | ✓    | ✓    | ✗       |
| PESCADO         | ✓  | ✓    | ✓    | ✓       |

#### Respuestas

**¿Cuántos ✓ hay en la fila de la última palabra (PESCADO)?**  
**4**

**¿Cuántos ✓ hay en la fila de la primera palabra (EL)?**  
**1**

#### Explicación
La máscara causal es necesaria porque el modelo genera el texto paso a paso y no puede ver el futuro.  
Así se asegura de usar solo la información disponible hasta ese momento y no “hacer trampa”.  
Esto permite que el texto se construya de forma coherente, como lo hacemos al escribir o hablar.

### Actividad 4: Varias Cabezas (Varios Criterios)
#### Frase
**MARIA   NO   COMIO   PORQUE   ESTABA   ENFERMA**

Cada persona puntúa solo la fila de **COMIO** según su criterio.

#### Persona 1 — Causa (¿quién explica el porqué?)

##### Puntuaciones
- MARIA = 2  
- NO = 3  
- COMIO = 4  
- PORQUE = 9  
- ESTABA = 8  
- ENFERMA = 10  

**Suma:** 36

##### Porcentajes

| Palabra  | Puntuación | ÷ 36 | % ≈ |
|----------|-----------|------|------|
| MARIA    | 2         | 2/36 | 5.56 % |
| NO       | 3         | 3/36 | 8.33 % |
| COMIO    | 4         | 4/36 | 11.11 % |
| PORQUE   | 9         | 9/36 | 25 % |
| ESTABA   | 8         | 8/36 | 22.22 % |
| ENFERMA  | 10        | 10/36| 27.78 % |
| **Total**| **36**    | —    | **100 %** |

#### Persona 2 — Sujeto (¿quién realiza la acción?)

##### Puntuaciones
- MARIA = 10  
- NO = 4  
- COMIO = 5  
- PORQUE = 3  
- ESTABA = 2  
- ENFERMA = 2  

**Suma:** 26

##### Porcentajes

| Palabra  | Puntuación | ÷ 26 | % ≈ |
|----------|-----------|------|------|
| MARIA    | 10        | 10/26 | 38.46 % |
| NO       | 4         | 4/26  | 15.38 % |
| COMIO    | 5         | 5/26  | 19.23 % |
| PORQUE   | 3         | 3/26  | 11.54 % |
| ESTABA   | 2         | 2/26  | 7.69 % |
| ENFERMA  | 2         | 2/26  | 7.69 % |
| **Total**| **26**    | —     | **100 %** |

#### Persona 3 — Vecinos (palabras cercanas)

##### Puntuaciones
- MARIA = 3  
- NO = 9  
- COMIO = 5  
- PORQUE = 9  
- ESTABA = 3  
- ENFERMA = 2  

**Suma:** 31

##### Porcentajes

| Palabra  | Puntuación | ÷ 31 | % ≈ |
|----------|-----------|------|------|
| MARIA    | 3         | 3/31 | 9.68 % |
| NO       | 9         | 9/31 | 29.03 % |
| COMIO    | 5         | 5/31 | 16.13 % |
| PORQUE   | 9         | 9/31 | 29.03 % |
| ESTABA   | 3         | 3/31 | 9.68 % |
| ENFERMA  | 2         | 2/31 | 6.45 % |
| **Total**| **31**    | —    | **100 %** |

#### Comparación

**¿Las tres filas son iguales?**  
No, cada una da importancia a palabras distintas según su criterio.

#### Reflexión
Ver la frase desde varios criterios permite entender mejor el significado completo.  
Unas “cabezas” captan la causa, otras el sujeto y otras la cercanía.  
Juntas, ofrecen una comprensión más rica que usar solo un punto de vista.

### Actividad 5: Encoder vs Decoder (Role-Play)
#### Debrief (Reflexión)

**¿Qué fue más fácil: leer todo (encoder) o escribir de a poco (decoder)?**  
Leer todo (encoder) suele ser más fácil porque ya tienes el contexto completo desde el inicio.

**¿En qué momento el decoder “necesitó” mirar atrás?**  
Cuando tuvo que decidir la siguiente palabra y necesitó recordar las anteriores para mantener coherencia.

**¿Cómo se relaciona esto con traducir o con un chatbot?**  
El encoder entiende todo el mensaje primero, mientras el decoder genera la respuesta paso a paso usando ese contexto, como en traducción o en un chatbot.