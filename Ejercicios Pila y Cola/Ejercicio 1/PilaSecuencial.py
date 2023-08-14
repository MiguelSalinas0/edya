import numpy as np


class Pila:

    __tope = 0
    __cantidad = 0
    __items = None

    def __init__(self, cantidad):
        self.__cantidad = cantidad
        self.__items = np.empty(self.__cantidad, dtype=int)

    def vacia(self):
        return self.__tope == 0

    def llena(self):
        return self.__tope == self.__cantidad

    def agregar(self, dato):
        if (self.llena()):
            print('Pila Llena')
        else:
            self.__items[self.__tope] = dato
            self.__tope += 1

    def suprimir(self):
        eliminado = None
        if (self.vacia()):
            print('Pila Vacia')
        else:
            eliminado = self.__items[self.__tope-1]
            self.__tope -= 1
        return eliminado

    def mostrar(self):
        for i in range(self.__tope-1, -1, -1):
            print(self.__items[i])
