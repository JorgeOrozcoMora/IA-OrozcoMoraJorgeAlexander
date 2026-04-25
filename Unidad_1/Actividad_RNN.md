## ACTIVIDAD RNN BASICA VANILLA
**Orozco Mora Jorge Alexander**  
*NC: 22120703*

---
El Termómetro de las Emociones (Una Vanilla RNN)Imagina que tú mismo
eres una Vanilla RNN y tu trabajo es predecir cuál será tu "Estado de
Ánimo General" al final del día. A diferencia de una red estática que
solo juzgaría lo que pasó hoy, tú tienes memoria.Tu cerebro (el nodo
recurrente) toma su decisión basándose en dos ingredientes que se
mezclan en una coctelera matemática todos los días:

1. Entrada de Hoy ($x_t$): ¿Qué te pasó hoy? (Ej. Encontraste dinero en
   la calle = +5 de alegría, o te saltaste el desayuno = -3 de energía).
2. El Estado Oculto Anterior ($h_{t-1}$): ¿Cómo te sentías ayer al irte
   a dormir?  (Esta es tu memoria a corto plazo).El Ciclo de la RNN (La
   Mezcla):


Al final del día, no eres solo el resultado de lo que te pasó hoy. Si
ayer ganaste la lotería (Estado Anterior muy alto), un pequeño
contratiempo hoy (Entrada negativa) no arruinará tu día por completo. Tu
memoria amortigua o potencia la entrada de hoy.La "magia" matemática de
la Vanilla RNN es simplemente:Estado de Hoy = (Evento de Hoy) + (Una
fracción de tu Estado de Ayer)El problema de la Vanilla RNN (y por qué
pierde la memoria con el tiempo) es esa "fracción". Si cada día que pasa
solo retienes el 50% del sentimiento del día anterior, después de una
semana, por más feliz que hayas estado el lunes, para el domingo ya ni
te acuerdas.

---
### Misión 1: El Lunes Increíble (Demostrando el Desvanecimiento)

Objetivo: Ver cómo un evento muy fuerte se olvida con el tiempo si no
hay nuevos estímulos.

- Día 1 (Lunes): Te ganas un premio. Tu "Evento de Hoy" es +10. (Tu Estado
Final es 10).

- Día 2 al Día 5: Son días completamente normales, no pasa nada ni bueno
ni malo. Tu "Evento de Hoy" para todos estos días es 0.

Tu Tarea: Calcula tu Estado Final para el Viernes (Día 5). Verás que la
alegría del Lunes casi ha desaparecido.

**Respuesta:** Se tienen los siguientes datos: el Día 1 ocurre un evento con valor de +10, mientras que del Día 2 al Día 5 el evento es igual a 0. Para calcular el estado emocional se aplica la fórmula correspondiente en cada día. En el Día 1, el valor inicial es h1=10. En el Día 2, se obtiene h2=0+0.5(10)=5. Para el Día 3, el cálculo es h3=0+0.5(5)=2.5. En el Día 4, resulta h4=0+0.5(2.5)=1.25. Finalmente, en el Día 5 se calcula h5=0+0.5(1.25)=0.625. Como resultado final, el viernes el estado emocional es de 0.625, lo que indica que la gran alegría experimentada el lunes casi desapareció.

---

### Misión 2: El Rescate Emocional (Superando el Pasado)

Objetivo: Entender cuánta energía nueva se necesita para revertir una
memoria negativa acumulada.

- Día 1: Te enfermas. Evento = -6.

- Día 2: Te regañan en el trabajo. Evento = -4.

- Día 3: Tienes una cita médica de rutina. Evento = 0.

Tu Tarea: ¿De qué magnitud tiene que ser el "Evento" del Día 4 para que
tu Estado Final de ese día logre ser positivo (mayor a cero)?

**Respuesta:** Se tienen los siguientes datos: en el Día 1 ocurre un evento con valor de -6, en el Día 2 un evento de -4, en el Día 3 el evento es igual a 0 y en el Día 4 el evento es desconocido. Para calcular el estado emocional se aplica la fórmula correspondiente cada día. En el Día 1, el valor inicial es h1=−6. En el Día 2, se obtiene h2=−4+0.5(−6), por lo tanto h2=−4−3=−7. Para el Día 3, el cálculo es h3=0+0.5(−7)=−3.5. En el Día 4, se plantea h4=x4+0.5(−3.5), de modo que h4=x4−1.75. Como se desea que el estado emocional sea positivo, se establece la condición 4>0. Entonces, x4−1.75>0, lo que implica que x4>1.75. Como resultado final, el evento del Día 4 debe ser mayor que 1.75, es decir, con un evento de +2 o más ya se lograría un estado positivo.

---

### Misión 3: Constancia vs. El Pico (Cómo aprende la red)

Objetivo: Comparar qué tiene mayor impacto a largo plazo: un evento
gigante y aislado, o eventos pequeños pero constantes.

- Escenario A: Un pico el Día 1 (+10), y luego ceros (0) el resto de la
semana.

- Escenario B: Pequeñas alegrías todos los días. Eventos de +3 desde el
Día 1 hasta el Día 5.

Tu Tarea: Compara el Estado Final del Día 5 en ambos
escenarios. Descubrirás que una Vanilla RNN prefiere y recuerda mejor la
información reciente y constante.

**Respuesta:** Se analizan dos escenarios distintos. En el Escenario A, ocurre un evento de +10 en el Día 1, mientras que del Día 2 al Día 5 los eventos son iguales a 0. Con los cálculos previamente realizados, se obtiene como resultado final que en el Día 5 el estado emocional es h5=0.625. En el Escenario B, ocurre un evento de +3 todos los días. Para el Día 1, el valor inicial es h1=3. En el Día 2, se calcula h2=3+0.5(3)=4.5. Para el Día 3, el resultado es h3=3+0.5(4.5)=5.25. En el Día 4, se obtiene h4=3+0.5(5.25)=5.625. Finalmente, en el Día 5 se calcula h5=3+0.5(5.625)=5.8125.
Como resultado final, el Escenario B produce un estado emocional mucho mayor en el quinto día, con un valor de 5.8125, mientras que el Escenario A solo alcanza 0.625. Esto muestra que pequeñas alegrías constantes tienen un efecto más duradero que una sola gran alegría inicial.