## PROBLEMAS: Monjes y Caníbales, Maridos y Esposas, Ranas
**Orozco Mora Jorge Alexander**  
*NC: 22120703*

---

### Monjes y Canibales
Tres monjes y tres caníbales se encuentran en un lado del río y deben cruzar al otro lado utilizando un bote que solo puede transportar dos personas a la vez.
La condición es que en ningún lado del río puede haber más caníbales que monjes, porque los caníbales se comerían a los monjes.

#### *La medida de rendimiento que define el criterio de éxito*
El criterio de éxito se cumple cuando los tres monjes y los tres caníbales se encuentran en el lado opuesto del río y en ningún momento se violó la regla de que los caníbales no superen en número a los monjes en alguno de los lados.

#### *El conocimiento del medio en el que habita el acumulado por el agente*
El agente conoce:
- Número de monjes y caníbales
- Capacidad del bote (máximo dos personas)
- Ubicación del bote
- Reglas del problema
- Estado actual de cada lado del río

#### *Las acciones que el agente puede llevar acabo*
El agente puede realizar las siguientes acciones:
- Mover un monje
- Mover dos monjes
- Mover un caníbal
- Mover dos caníbales
- Mover un monje y un caníbal

#### *La secuencia de percepciones del agente hasta este momento*
El agente percibe en cada estado:
- Cuántos monjes hay en cada lado
- Cuántos caníbales hay en cada lado
- Posición del bote

### Maridos y Esposas
Tres matrimonios deben cruzar un río usando un bote con capacidad para dos personas.
La condición es que ninguna esposa puede quedarse con otro hombre si su esposo no está presente, porque se producirían celos.
El objetivo es que todos crucen el río.

#### *La medida de rendimiento que define el criterio de éxito*
El éxito se alcanza cuando las tres parejas se encuentran en el lado opuesto del río sin haber violado la regla de que una esposa no puede estar con otro hombre sin su esposo.

#### *El conocimiento del medio en el que habita el acumulado por el agente*
El agente conoce:
- Número de personas
- Quién es esposo de quién
- Capacidad del bote
- Ubicación del bote
- Regla de los celos
- Estado actual de cada lado

#### *Las acciones que el agente puede llevar acabo*
El agente puede:
- Mover una persona
- Mover dos personas

Siempre respetando la capacidad del bote y la regla de celos

#### *La secuencia de percepciones del agente hasta este momento*
El agente percibe:
- Quién está en cada lado
- Quién está en el bote
- Posición del bote

### Ranas
Hay tres ranas en el lado izquierdo mirando hacia la derecha y tres ranas en el lado derecho mirando hacia la izquierda.
El objetivo es intercambiar sus posiciones.

#### *La medida de rendimiento que define el criterio de éxito*
El éxito se alcanza cuando las ranas del lado izquierdo pasan al lado derecho y las del lado derecho pasan al lado izquierdo respetando las reglas de movimiento.

#### *El conocimiento del medio en el que habita el acumulado por el agente*
El agente conoce:
- Número de ranas
- Posición de cada rana
- Espacio vacío
- Reglas de movimiento
- Estado actual del tablero

#### *Las acciones que el agente puede llevar acabo*
El agente puede:
- Avanzar una rana a un espacio vacío
- Saltar una rana sobre otra
- Mover solo hacia adelante

No puede:
- retroceder
- saltar dos ranas
- moverse a un espacio ocupado

#### *La secuencia de percepciones del agente hasta este momento*
El agente percibe:
- Posición de cada rana
- Espacio vacío
- Dirección de movimiento