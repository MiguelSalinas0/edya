from PilaEncadenada import Pila

class Number:

    __number = 0
    __pila = None

    def __init__(self, number):
        self.__number = number
        self.__pila = Pila()

    def calcularFactorial(self):
        total = 1
        while (not self.__pila.vacia()):
            total = total * self.__pila.suprimir()
        print('\nEl factorial de {}! es: {}'.format(self.__number, total))

    def cargarPila(self):
        aux = self.__number
        while (aux > 0):
            self.__pila.insertar(aux)
            aux = aux - 1

    def mostrarPila(self):
        self.__pila.mostrar()


if __name__ == '__main__':
    n = int(input('Ingrese un numero: '))
    number = Number(n)
    number.cargarPila()
    number.mostrarPila()
    number.calcularFactorial()
