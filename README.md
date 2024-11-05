# Sergio Iván Cardona Polanco
# Carné: 1222419
# PROYECTO FINAL LENGUAJES FORMALES Y AUTÓMATAS


# Máquina de Turing de Dos Cintas

Este proyecto implementa una máquina de Turing de dos cintas en Python, que procesa cadenas de entrada para mostrar cómo una máquina de Turing lee y procesa símbolos en ambas cintas. También genera una representación visual de los estados y transiciones del autómata, empleando Graphviz para crear gráficos de los estados.
- Características:

1. Definición de Estados y Símbolos: Define un conjunto de símbolos (`a`, `b`, `*`, `#`) y un conjunto de estados (`q0`, `q1`, `q2`, `q3`, `q4`, `qf`), donde `qf` es el estado de aceptación.
  
2. Transiciones:
   - Cinta 1 (Posiciones Impares): Definición de transiciones de izquierda a derecha (`transiciones_cinta1_ID`) y de derecha a izquierda (`transiciones_cinta1_DI`).
   - Cinta 2 (Posiciones Pares): Definición de transiciones de izquierda a derecha (`transiciones_cinta2_ID`) y de derecha a izquierda (`transiciones_cinta2_DI`).

3. Visualización: Utiliza Graphviz para representar el autómata en un grafo, permitiendo ver los estados y transiciones de la máquina para cada cadena de entrada.

4. Procesamiento: Lee cadenas desde un archivo `.txt` y las procesa, generando un diagrama de estados y tablas de transición para cada cadena.

## ¿Cómo funciona?

Flujo del programa:

1. Inicialización: Se definen las transiciones y estados de la máquina de Turing.
2. Procesamiento de cadenas:
   - Separación en Cintas: La cadena de entrada se divide en dos cintas: símbolos en posiciones impares para la cinta 1 y en posiciones pares para la cinta 2.
   - Generación del grafo: Se construye un grafo en Graphviz que muestra los estados y transiciones específicas para cada cadena.
   - Tablas de transición: Se generan tablas de transición que describen el comportamiento de la máquina en ambas cintas.
   - Lectura de izquierda a derecha y de derecha a izquierda: Se muestra el procesamiento de la cadena en ambas direcciones para cada cinta.

3. Visualización de resultados: Para cada cadena procesada, se genera y guarda un archivo PNG con el grafo de estados.

### Ejecución del código

Este programa puede ejecutarse en la línea de comandos y solicita al usuario el nombre del archivo `.txt` que contiene las cadenas a procesar.

```python
if __name__ == "__main__":
    m = MaquinaTuring2Cintas()
    m.main()
```

### Archivos generados

- Imágenes PNG: Se genera una imagen para cada cadena procesada que muestra el grafo de estados y transiciones.
- Tablas de transición: Las tablas de transición se muestran en la consola y detallan los cambios de estado para cada símbolo leído.

## Requisitos

- Python 3.x
- Librería Graphviz (instalable con `pip install graphviz`)

## Ejemplo de uso

1. **Preparar un archivo de texto** con cadenas que la máquina de Turing debe procesar. Ejemplo (`cadenas.txt`):

aba*#
abaaa*#
abaaa*##
abaa*#
abaaaa*#
aba*###
abaa*#bba*#
abaaa*bbaa*#
ababba*bbaa*#
abaaaa*aa*bba*#

2. **Ejecutar el programa** desde la línea de comandos:
   ```bash
   python nombre_del_archivo.py
   ```

3. **Ingresar el nombre del archivo de texto** cuando se solicite:
   ```
   Ingrese el nombre del archivo de texto (incluya la extensión .txt): cadenas.txt
   ```

4. El programa procesará cada cadena, generará los gráficos y mostrará las tablas de transición.
