from PilaSecuencial import Pila

class Number:

    __number = 0
    __pila = None

    def __init__(self, decimal, dimension):
        self.__number = decimal
        self.__pila = Pila(dimension)

    def calcularBinario(self):
        if (self.__number <= 0):
            return 0
        while self.__number > 0:
            residuo = int(self.__number % 2)
            self.__number = int(self.__number / 2)
            self.__pila.agregar(residuo)

    def mostrar(self):
        self.__pila.mostrar()

if __name__ == '__main__':
    number = Number(14, 5)
    number.calcularBinario()
    number.mostrar()
    