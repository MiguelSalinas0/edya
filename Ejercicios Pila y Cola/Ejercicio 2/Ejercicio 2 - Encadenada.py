from PilaEncadenada import Pila

class Number:

    __number = 0
    __pila = None

    def __init__(self, number):
        self.__number = number
        self.__pila = Pila()

    def calcularBinario(self):
        if (self.__number <= 0):
            return 0
        while self.__number > 0:
            residuo = int(self.__number % 2)
            self.__number = int(self.__number / 2)
            self.__pila.insertar(residuo)

    def mostrar(self):
        self.__pila.mostrar()

if __name__ == '__main__':
    n = int(input('Ingrese un numero: '))
    number = Number(n)
    number.calcularBinario()
    number.mostrar()
    