from graphviz import Digraph

class MaquinaTuring2Cintas:
    def __init__(self):
        # Definición del alfabeto y símbolos
        self.L = {'a', 'b', '*', '#', 'g'}
        self.r = self.L
        self.B = {'*', '#'}
        self.Q = {'q0', 'q1', 'q2', 'q3', 'q4', 'qf'}
        self.Qf = {'qf'}
        self.f = {'I', 'D'}

        # Transiciones para la Cinta 1 (posiciones impares) - Izquierda a Derecha
        self.transiciones_cinta1_ID = {
            ('q0', 'a'): ('q1', 'a', 'D'),
            ('q1', 'b'): ('q2', 'b', 'D'),
            ('q2', 'a'): ('q3', 'a', 'D'),
            ('q3', 'a'): ('q3', 'a', 'D'),
            ('q3', 'b'): ('q1', 'b', 'D'),
            ('q3', '*'): ('q4', '*', 'D'),
            ('q4', 'b'): ('q1', 'b', 'D'),
            ('q4', '#'): ('qf', '#', 'D'),
        }

        # Transiciones para la Cinta 2 (posiciones pares) - Izquierda a Derecha
        self.transiciones_cinta2_ID = {
            ('q0', 'g'): ('q1', 'g', 'D'),
            ('q1', 'g'): ('q2', 'g', 'D'),
            ('q2', 'g'): ('q3', 'g', 'D'),
            ('q3', 'a'): ('q3', 'a', 'D'),
            ('q3', 'g'): ('q4', 'g', 'D'),
            ('q4', 'g'): ('qf', 'g', 'D'),
        }

        # Transiciones para la Cinta 1 (posiciones impares) - Derecha a Izquierda
        self.transiciones_cinta1_DI = {
            ('q0', 'b'): ('q1', 'b', 'I'),
            ('q1', '*'): ('q2', '*', 'I'),
            ('q2', 'a'): ('q3', 'a', 'I'),
            ('q3', 'b'): ('q4', 'b', 'I'),
            ('q4', 'a'): ('qf', 'a', 'I'),
        }

        # Transiciones para la Cinta 2 (posiciones pares) - Derecha a Izquierda
        self.transiciones_cinta2_DI = {
            ('q0', 'g'): ('q1', 'g', 'I'),
            ('q1', 'a'): ('q2', 'a', 'I'),
            ('q2', 'g'): ('q3', 'g', 'I'),
            ('q3', 'g'): ('q4', 'g', 'I'),
            ('q4', 'a'): ('qf', 'a', 'I'),
        }

    def imprimir_tablas_transicion(self):
        print("\n=== TABLAS DE TRANSICIÓN IZQUIERDA A DERECHA ===")
        
        print("\nTabla Cinta 1 (Posiciones Impares):")
        print("╔══════════════╦═══════════════╦══════════════╦══════════════╦═══════════╗")
        print("║ Estado Actual║ Símbolo Leído ║ Nuevo Estado ║ Nuevo Símbolo║ Dirección ║")
        print("╠══════════════╬═══════════════╬══════════════╬══════════════╬═══════════╣")
        for (q, s), (nq, ns, d) in self.transiciones_cinta1_ID.items():
            print(f"║ {q:12} ║ {s:13} ║ {nq:12} ║ {ns:12} ║ {d:9} ║")
        print("╚══════════════╩═══════════════╩══════════════╩══════════════╩═══════════╝")

        print("\nTabla Cinta 2 (Posiciones Pares):")
        print("╔══════════════╦═══════════════╦══════════════╦══════════════╦═══════════╗")
        print("║ Estado Actual║ Símbolo Leído ║ Nuevo Estado ║ Nuevo Símbolo║ Dirección ║")
        print("╠══════════════╬═══════════════╬══════════════╬══════════════╬═══════════╣")
        for (q, s), (nq, ns, d) in self.transiciones_cinta2_ID.items():
            print(f"║ {q:12} ║ {s:13} ║ {nq:12} ║ {ns:12} ║ {d:9} ║")
        print("╚══════════════╩═══════════════╩══════════════╩══════════════╩═══════════╝")

        print("\n=== TABLAS DE TRANSICIÓN DERECHA A IZQUIERDA ===")
        
        print("\nTabla Cinta 1 (Posiciones Impares):")
        print("╔══════════════╦═══════════════╦══════════════╦══════════════╦═══════════╗")
        print("║ Estado Actual║ Símbolo Leído ║ Nuevo Estado ║ Nuevo Símbolo║ Dirección ║")
        print("╠══════════════╬═══════════════╬══════════════╬══════════════╬═══════════╣")
        for (q, s), (nq, ns, d) in self.transiciones_cinta1_DI.items():
            print(f"║ {q:12} ║ {s:13} ║ {nq:12} ║ {ns:12} ║ {d:9} ║")
        print("╚══════════════╩═══════════════╩══════════════╩══════════════╩═══════════╝")

        print("\nTabla Cinta 2 (Posiciones Pares):")
        print("╔══════════════╦═══════════════╦══════════════╦══════════════╦═══════════╗")
        print("║ Estado Actual║ Símbolo Leído ║ Nuevo Estado ║ Nuevo Símbolo║ Dirección ║")
        print("╠══════════════╬═══════════════╬══════════════╬══════════════╬═══════════╣")
        for (q, s), (nq, ns, d) in self.transiciones_cinta2_DI.items():
            print(f"║ {q:12} ║ {s:13} ║ {nq:12} ║ {ns:12} ║ {d:9} ║")
        print("╚══════════════╩═══════════════╩══════════════╩══════════════╩═══════════╝")

    def separar_cintas(self, cadena):
        cinta1 = cadena[::2]  # Posiciones impares
        cinta2 = cadena[1::2]  # Posiciones pares
        return cinta1, cinta2

    def procesar_cadena(self, cadena):
        print("\nProcesando cadena:", cadena)
        
        # Separar la cadena en las dos cintas
        cinta1, cinta2 = self.separar_cintas(cadena)
        
        # Mostrar las cintas en el formato especificado
        print(f"I₁: {{{', '.join(cinta1)}}}")
        print(f"I₀: {{{', '.join(cinta2)}}}")
        
        # Procesar de izquierda a derecha
        print("\nLectura de Izquierda a Derecha:")
        print(f"Cinta 1 (posiciones impares): {' → '.join(cinta1)}")
        print(f"Cinta 2 (posiciones pares):   {' → '.join(cinta2)}")
        
        # Procesar de derecha a izquierda
        print("\nLectura de Derecha a Izquierda:")
        print(f"Cinta 1 (posiciones impares): {' → '.join(reversed(list(cinta1)))}")
        print(f"Cinta 2 (posiciones pares):   {' → '.join(reversed(list(cinta2)))}")

    def crear_grafo(self):
        dot = Digraph(comment='Máquina de Turing de 2 Cintas')
        dot.attr(rankdir='LR')
        
        for q in self.Q:
            if q in self.Qf:
                dot.node(q, q, shape='doublecircle')
            else:
                dot.node(q, q, shape='circle')
        
        # Agregar transiciones para ambas cintas
        for (q_actual, simbolo), (q_siguiente, nuevo_simbolo, direccion) in self.transiciones_cinta1_ID.items():
            dot.edge(q_actual, q_siguiente, f'C1: {simbolo}/{nuevo_simbolo},{direccion}')
        
        for (q_actual, simbolo), (q_siguiente, nuevo_simbolo, direccion) in self.transiciones_cinta2_ID.items():
            dot.edge(q_actual, q_siguiente, f'C2: {simbolo}/{nuevo_simbolo},{direccion}')
        
        return dot

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            return [linea.strip() for linea in archivo if linea.strip()]
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {nombre_archivo}")
        return []
    except Exception as e:
        print(f"Error al leer el archivo: {str(e)}")
        return []

def main():
    mt = MaquinaTuring2Cintas()
    
    # Solicitar nombre del archivo
    nombre_archivo = input("Ingrese el nombre del archivo con las cadenas: ")
    cadenas = leer_archivo(nombre_archivo)
    
    if not cadenas:
        print("No se encontraron cadenas para procesar.")
        return
    
    # Imprimir tablas de transición
    mt.imprimir_tablas_transicion()
    
    # Generar el grafo
    grafo = mt.crear_grafo()
    grafo.render('maquina_turing_2cintas', format='png', cleanup=True)
    print("\nSe ha generado el grafo 'maquina_turing_2cintas.png'")
    
    # Procesar cada cadena
    for cadena in cadenas:
        mt.procesar_cadena(cadena)

if __name__ == "__main__":
    main()