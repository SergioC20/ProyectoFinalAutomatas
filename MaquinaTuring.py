from graphviz import Digraph

class MaquinaTuring2Cintas:
    def __init__(self):
        # Definición del alfabeto y símbolos
        self.L = {'a', 'b', '*', '#'}
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
            ('q0', '#'): ('q1', '#', 'D'),
            ('q1', 'a'): ('q2', 'a', 'D'),
            ('q2', '#'): ('q3', '#', 'D'),
            ('q3', 'a'): ('q3', 'a', 'D'),
            ('q3', '#'): ('q4', '#', 'D'),
            ('q4', '#'): ('qf', '#', 'D'),
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
            ('q0', '#'): ('q1', '#', 'I'),
            ('q1', 'a'): ('q2', 'a', 'I'),
            ('q2', '#'): ('q3', '#', 'I'),
            ('q3', '#'): ('q4', '#', 'I'),
            ('q4', 'a'): ('qf', 'a', 'I'),
        }

    def generar_grafo_automata(self, cadena, num_cadena):
        dot = Digraph(comment=f'Autómata para cadena {cadena}')
        dot.attr(rankdir='LR')
        
        # Agregar todos los estados
        for estado in self.Q:
            if estado in self.Qf:
                dot.node(estado, estado, shape='doublecircle')
            else:
                dot.node(estado, estado, shape='circle')
        
        # Agregar las transiciones relevantes para esta cadena
        simbolos_cinta1 = set(cadena[::2])
        simbolos_cinta2 = set(cadena[1::2])
        
        # Transiciones de izquierda a derecha
        for (q, s), (nq, ns, d) in self.transiciones_cinta1_ID.items():
            if s in simbolos_cinta1:
                dot.edge(q, nq, label=f'C1: {s}/{ns},{d}')
                
        for (q, s), (nq, ns, d) in self.transiciones_cinta2_ID.items():
            if s in simbolos_cinta2:
                dot.edge(q, nq, label=f'C2: {s}/{ns},{d}')
        
        # Transiciones de derecha a izquierda
        for (q, s), (nq, ns, d) in self.transiciones_cinta1_DI.items():
            if s in simbolos_cinta1:
                dot.edge(q, nq, label=f'C1: {s}/{ns},{d}')
                
        for (q, s), (nq, ns, d) in self.transiciones_cinta2_DI.items():
            if s in simbolos_cinta2:
                dot.edge(q, nq, label=f'C2: {s}/{ns},{d}')

        # Guardar el grafo
        nombre_archivo = f'automata_cadena_{num_cadena}'
        dot.render(nombre_archivo, format='png', cleanup=True)
        print(f"\nGrafo del autómata guardado como: {nombre_archivo}.png")

    def imprimir_tablas_transicion(self, cadena, num_cadena):
        print(f"\n=== TABLA DE SIMBOLOGÍA PARA CADENA {num_cadena}: {cadena} ===")
        print("L = {a, b, *, #}")
        print("r = L")
        print("B = {*, #}")
        print("Q = {q0, q1, q2, q3, q4, qf}")
        print("Qf = {qf}")
        print("f = {I, D}")

        print("\n=== TABLAS DE TRANSICIÓN IZQUIERDA A DERECHA ===")
        
        simbolos_cinta1 = set(cadena[::2])
        simbolos_cinta2 = set(cadena[1::2])
        
        print("\nTabla Cinta 1 (Posiciones Impares):")
        print("╔══════════════╦═══════════════╦══════════════╦══════════════╦═══════════╗")
        print("║ Estado Actual║ Símbolo Leído ║ Nuevo Estado ║ Nuevo Símbolo║ Dirección ║")
        print("╠══════════════╬═══════════════╬══════════════╬══════════════╬═══════════╣")
        for (q, s), (nq, ns, d) in self.transiciones_cinta1_ID.items():
            if s in simbolos_cinta1:
                print(f"║ {q:12} ║ {s:13} ║ {nq:12} ║ {ns:12} ║ {d:9} ║")
        print("╚══════════════╩═══════════════╩══════════════╩══════════════╩═══════════╝")

        print("\nTabla Cinta 2 (Posiciones Pares):")
        print("╔══════════════╦═══════════════╦══════════════╦══════════════╦═══════════╗")
        print("║ Estado Actual║ Símbolo Leído ║ Nuevo Estado ║ Nuevo Símbolo║ Dirección ║")
        print("╠══════════════╬═══════════════╬══════════════╬══════════════╬═══════════╣")
        for (q, s), (nq, ns, d) in self.transiciones_cinta2_ID.items():
            if s in simbolos_cinta2:
                print(f"║ {q:12} ║ {s:13} ║ {nq:12} ║ {ns:12} ║ {d:9} ║")
        print("╚══════════════╩═══════════════╩══════════════╩══════════════╩═══════════╝")

        print("\n=== TABLAS DE TRANSICIÓN DERECHA A IZQUIERDA ===")
        
        print("\nTabla Cinta 1 (Posiciones Impares):")
        print("╔══════════════╦═══════════════╦══════════════╦══════════════╦═══════════╗")
        print("║ Estado Actual║ Símbolo Leído ║ Nuevo Estado ║ Nuevo Símbolo║ Dirección ║")
        print("╠══════════════╬═══════════════╬══════════════╬══════════════╬═══════════╣")
        for (q, s), (nq, ns, d) in self.transiciones_cinta1_DI.items():
            if s in simbolos_cinta1:
                print(f"║ {q:12} ║ {s:13} ║ {nq:12} ║ {ns:12} ║ {d:9} ║")
        print("╚══════════════╩═══════════════╩══════════════╩══════════════╩═══════════╝")

        print("\nTabla Cinta 2 (Posiciones Pares):")
        print("╔══════════════╦═══════════════╦══════════════╦══════════════╦═══════════╗")
        print("║ Estado Actual║ Símbolo Leído ║ Nuevo Estado ║ Nuevo Símbolo║ Dirección ║")
        print("╠══════════════╬═══════════════╬══════════════╬══════════════╬═══════════╣")
        for (q, s), (nq, ns, d) in self.transiciones_cinta2_DI.items():
            if s in simbolos_cinta2:
                print(f"║ {q:12} ║ {s:13} ║ {nq:12} ║ {ns:12} ║ {d:9} ║")
        print("╚══════════════╩═══════════════╩══════════════╩══════════════╩═══════════╝")

    def separar_cintas(self, cadena):
        cinta1 = cadena[::2]  # Posiciones impares
        cinta2 = cadena[1::2]  # Posiciones pares
        return cinta1, cinta2

    def procesar_cadena(self, cadena, num_cadena):
        print(f"\n{'='*50}")
        print(f"Procesando cadena {num_cadena}: {cadena}")
        print(f"{'='*50}")
        
        # Generar el grafo del autómata para esta cadena
        self.generar_grafo_automata(cadena, num_cadena)
        
        # Separar la cadena en las dos cintas
        cinta1, cinta2 = self.separar_cintas(cadena)
        
        # Mostrar las cintas en el formato especificado
        print(f"\nCintas para cadena {num_cadena}:")
        print(f"I₁ (posiciones impares): {{{', '.join(cinta1)}}}")
        print(f"I₀ (posiciones pares): {{{', '.join(cinta2)}}}")
        
        # Imprimir las tablas de transición
        self.imprimir_tablas_transicion(cadena, num_cadena)
        
        # Procesar de izquierda a derecha
        print(f"\nLectura de Izquierda a Derecha (Cadena {num_cadena}):")
        print(f"Cinta 1 (posiciones impares): {' → '.join(cinta1)}")
        print(f"Cinta 2 (posiciones pares):   {' → '.join(cinta2)}")
        
        # Procesar de derecha a izquierda
        print(f"\nLectura de Derecha a Izquierda (Cadena {num_cadena}):")
        print(f"Cinta 1 (posiciones impares): {' ← '.join(reversed(cinta1))}")
        print(f"Cinta 2 (posiciones pares):   {' ← '.join(reversed(cinta2))}")
        


    def leer_cadenas_de_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'r') as file:
            cadenas = file.readlines()
        return [cadena.strip() for cadena in cadenas]

    def main(self):
        # Leer el nombre del archivo desde la consola
        nombre_archivo = input("Ingrese el nombre del archivo de texto (incluya la extensión .txt): ")
        cadenas = self.leer_cadenas_de_archivo(nombre_archivo)
        
        # Procesar cada cadena individualmente
        for i, cadena in enumerate(cadenas, 1):
            self.procesar_cadena(cadena, i)

if __name__ == "__main__":
    m = MaquinaTuring2Cintas()
    m.main()