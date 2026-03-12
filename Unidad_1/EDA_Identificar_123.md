## EDA para Identificar los Numeros 1,2,3
**Orozco Mora Jorge Alexander**  
*NC: 22120703*

---
### Objetivo del EDA
El objetivo del análisis exploratorio de datos (EDA) es estudiar el conjunto de imágenes que se utilizarán para entrenar un modelo capaz de reconocer los números 1, 2 y 3 en diferentes condiciones.

El sistema debe ser capaz de identificar los números en:

- Imágenes escritas a mano
- Imágenes impresas
- Fotografías
- Pantallas digitales
- Diferentes fondos
- Diferentes tamaños
- Diferente iluminación
- Diferentes orientaciones

### Dataset
El dataset estara compuesto por imagenes y tendra la siguiente estrutura:

- Clase 1
- Clase 2
- Clase 3  

y dentro de cada una de estas carpetas van a ir las imagenes de cada numero con todas sus versiones.

El dataset para identificar los numeros 1,2 y 3 debe de tener diferentes caracteristicas, las cuales pueden ser las siguientes:

- Diferentes tipos de letra
- Numeros escritos a mano
- Diferentes tamaños
- Diferentes colores
- Imagenes rotadas
- Imagenes con diferentes fondos

![Imagen de Diferentes Tipos de Numeros](https://upload.wikimedia.org/wikipedia/commons/b/b1/MNIST_dataset_example.png)

Para que el dataset funcione de forma correcta deberiamos de tener al menos 3000 imagenes para que el modelo funcione correctamente y no tenga problemas de aprendizaje, y estas debemos dividirlas de forma totalmente equitativa para que la cantidad de imagenes no este desbalanceado y el modelo pueda aprender correctamente, por ejemplo: 

- Clase 1: 1000 imagenes
- Clase 2: 1000 imagenes
- Clase 3: 1000 imagenes