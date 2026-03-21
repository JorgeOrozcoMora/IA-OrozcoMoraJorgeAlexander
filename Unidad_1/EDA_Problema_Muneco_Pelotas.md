## EDA Problema Muñeco y Pelotas
**Orozco Mora Jorge Alexander**  
*NC: 22120703*

---
### Descripcion del Problema
Se tiene un juego donde un muñeco debe decidir si saltar o no saltar cuando se le lanza una pelota.
Cada lanzamiento tiene características:
- Altura de la pelota
- Velocidad (puede variar)
- Acción del muñeco (saltar o no)

### Analisis de Variables
En el conjunto de datos se identifican tres variables principales: la altura de la pelota, la velocidad y la acción del muñeco. La variable altura y la velocidad funcionan como variables de entrada, mientras que la acción del muñeco representa la variable de salida, ya que depende de las condiciones del lanzamiento. Durante el análisis exploratorio se revisa la relación entre estas variables para determinar cuál influye más en la decisión. A partir de la exploración realizada, se observa que la altura tiene mayor impacto en el resultado, mientras que la velocidad no modifica el comportamiento del muñeco.

### Observacion de los Datos
Se observa que la variable más importante es la altura de la pelota, ya que al revisar los datos se identifica un patrón claro en la acción del muñeco. Cuando la altura de la pelota es alta, el muñeco no debe saltar, mientras que cuando la altura es baja, el muñeco sí debe saltar. Este comportamiento muestra que la decisión depende principalmente de la altura y que esta variable es suficiente para determinar la acción, sin necesidad de considerar otros factores, lo que confirma mediante la exploración de los datos que existe una relación directa entre la altura de la pelota y la respuesta del muñeco.

### Interpretacion del EDA
El análisis exploratorio de datos, permite concluir que la variable más importante para la toma de decisión es la altura de la pelota, ya que se observa que el comportamiento del muñeco depende directamente de esta característica. A partir de la exploración de los datos, se identifica que cuando la altura es baja el muñeco debe saltar, mientras que cuando la altura es alta el muñeco no debe saltar, por lo que no es necesario considerar la velocidad para determinar la acción. Esto indica que la información puede separarse claramente en dos grupos, uno correspondiente a los casos en los que el muñeco debe saltar y otro en los que no debe hacerlo.