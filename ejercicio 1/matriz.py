'''Ejercicio práctico1 (3Puntos): Creación de una clase en Python que representa una matriz.
Para este ejercicio, deberás crear una clase que representa una matriz.
Las operaciones (funciones=métodos, deben de ir en otra clase que el constructor) que esta clase debe permitir son la creación de una matriz a partir de una lista de listas,
la impresión de la matriz en una forma legible, y el cálculo de la transpuesta de la matriz.
Asegúrate de que cada método tenga una única responsabilidad.'''

class Matriz:
    def __init__(self, elementos):
        self.elementos = elementos

    def imprimir(self):
        for fila in self.elementos:
            print(fila)

class Imprimir(Matriz):
    def __init__(self, elementos):
        super().__init__(elementos)

    def imprimir(self):
        for fila in self.elementos:
            print(fila)


class Traspuesta(Matriz):
    def __init__(self, elementos):
        super().__init__(elementos)

    def traspuesta(self):
        return Matriz([[fila[i] for fila in self.elementos] for i in range(len(self.elementos[0]))])     #función landa, mejor que bucle for. Solo para volumen pequeño. Lo mejor sería una función recursiva.


class Lanzador(Imprimir, Traspuesta):
    #creame un metodo que me llame  a la funcion traspuesta y a la función imprimir y que me lo recoja en un input de todos los elemento de la matriz.
    def __init__(self):
        self.elementos = []
        self.cantidad_filas = int(input("Introduce la cantidad de filas: "))
        self.cantidad_columnas = int(input("Introduce la cantidad de columnas: "))
        self.crear_matriz()
        self.matriz = Matriz(self.elementos)
        self.traspuesta = Traspuesta(self.elementos)
        self.imprimir = Imprimir(self.elementos)
     
    
    def crear_matriz(self):
        for i in range(self.cantidad_filas):
            fila = []
            for j in range(self.cantidad_columnas):
                fila.append(int(input(f"Introduce el elemento {i+1}, {j+1}: ")))
            self.elementos.append(fila)


    def lanzar(self):
        print("La matriz es: ")
        self.imprimir.imprimir()
        print("La matriz traspuesta es: ")
        traspuesta_result = self.traspuesta.traspuesta()
        imprimir_traspuesta = Imprimir(traspuesta_result.elementos)
        imprimir_traspuesta.imprimir()


if __name__ == "__main__":
    lanzador = Lanzador()
    lanzador.lanzar()
  