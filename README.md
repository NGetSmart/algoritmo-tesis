Algoritmo de generación de todos los grafos débilmente etiquetados de n vértices.

Este repositorio contiene una implementación en Python de un algoritmo que construye y filtra familias de subconjuntos del conjunto de números enteros que va de 0 hasta n, de acuerdo con ciertas reglas combinatorias basadas en promedios e intersecciones.

Descripción del algoritmo
Para un entero n mayor o igual que 3, el programa realiza tres pasos:

1) Construye familias de subconjuntos denominadas subconjuntos armónicos de enteros;
2) Genera todas las combinaciones posibles de esas familias;
3) Selecciona únicamente las combinaciones que cumplen tres condiciones:
- La unión de todos los subconjuntos coincide exactamente con los enteros entre 0 y n;
- La intersección de cada par de subconjuntos pertenece al conjunto de promedios enteros de todos los subconjuntos;
- Se verifica una relación de simetría entre los promedios de los distintos subconjuntos.
Después de procesar, el programa imprime las colecciones que satisfacen las tres condiciones para cada valor de n.

Modo de uso
Sitúese en la carpeta del proyecto y ejecute en una terminal:
python hsets_algorithm.py
El script muestra los resultados para los valores de n comprendidos entre 3 y 9.

Ejecución en línea
Cuando se añada el notebook interactivo, se podrá ejecutar el código desde Binder; la dirección aparecerá aquí.

Dependencias
Solo se utiliza la biblioteca estándar itertools incluida en cualquier instalación de Python 3, por lo que no se necesitan paquetes adicionales.

Archivos del repositorio
hsets_algorithm.py – implementación principal del algoritmo
notebook.ipynb – notebook interactivo (se añadirá próximamente)
README.md – este documento

Licencia
MIT License
