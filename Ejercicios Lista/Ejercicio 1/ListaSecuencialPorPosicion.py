import numpy as np


class ListaSecuencialPorPosicion:

    __tope = 0
    __maximo = 0
    __items = None

    def __init__(self, max):
        self.__items = np.empty(max, dtype=int)
        self.__maximo = max

    def vacia(self):
        return self.__tope == 0

    def insertar(self, posicion, elemento):
        if posicion >= 0 and posicion <= self.__maximo + 1:
            if posicion <= self.__tope + 1:
                for i in range(self.__tope, posicion, -1):
                    self.__items[i] = self.__items[i-1]
                self.__items[posicion] = elemento
                self.__tope += 1
            else:
                print("La posicion no existe en la lista ")
        else:
            print("La lista esta llena")

    def suprimir(self, posicion):
        if posicion >= 0 and posicion < self.__tope:
            aux = self.__items[posicion]
            for i in range(posicion, self.__tope):
                self.__items[i] = self.__items[i+1]
            self.__tope -= 1
            return aux
        else:
            print("La posicion no existe en la lista ")

    def primer_elemento(self):
        if not self.vacia():
            return self.__items[0]

    def ultimo_elemento(self):
        if not self.vacia():
            self.__items[self.__tope - 1]

    def siguiente(self, posicion):
        if posicion <= self.__tope:
            return posicion + 1

    def anterior(sefl, posicion):
        if posicion > 1:
            return posicion - 1

    def buscar(self, elemento):
        i = 0
        while i <= self.__tope and elemento != self.__items[i]:
            i += 1
        if elemento != self.__items[i]:
            return -1
        else:
            return i

    def recuperar(self, posicion):
        if posicion >= 0 and posicion <= self.__tope:
            return self.__items[posicion]
        else:
            print("La posicion no existe en la lista ")

    def recorrer(self):
        for i in range(self.__tope):
            print(self.__items[i])


if __name__ == '__main__':
    lista = ListaSecuencialPorPosicion(10)
    lista.insertar(0, 5)
    lista.insertar(1, 20)
    lista.insertar(2, 15)
    lista.insertar(3, 10)
    lista.insertar(6, 25)
    lista.recorrer()
    print('Recuperado: {}'.format(lista.recuperar(3)))
    print('Buscado: {}'.format(lista.buscar(10)))
