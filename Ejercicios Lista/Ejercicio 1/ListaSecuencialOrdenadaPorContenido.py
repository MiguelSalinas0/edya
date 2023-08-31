import numpy as np


class ListaSecuencialOrdenadaPorContenido:
    __tope = 0
    __maximo = 0
    __items = None

    def __init__(self, max):
        self.__maximo = max
        self.__items = np.empty(max, dtype=int)

    def vacia(self):
        return self.__tope == 0

    def llena(self):
        return self.__maximo == self.__tope

    def insertar(self, elemento):
        if not self.llena():
            if self.__tope == 0:
                self.__items[self.__tope] = elemento
                self.__tope += 1
            else:
                i = 0
                while (elemento > self.__items[i]) and (i <= self.__tope):
                    i += 1
                for j in range(self.__tope, i, -1):
                    self.__items[j] = self.__items[j-1]
                self.__items[i] = elemento
                self.__tope += 1

    def suprimir(self, elemento):
        if self.vacia():
            print("Lista Vacia")
        else:
            i = 0
            while (elemento != self.__items[i]) and (i < self.__tope):
                i += 1
            if i == self.__tope:
                print("El elemento no se encuetra en la lista")
            else:
                aux = self.__items[i]
                for j in range(i, self.__tope, +1):
                    self.__items[j] = self.__items[j+1]
                self.__tope -= 1
                return aux

    def primer_elemento(self):
        if not self.vacia():
            return self.__items[0]

    def ultimo_elemento(self):
        if not self.vacia():
            return self.__items[self.__tope - 1]

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
        try:
            if posicion >= 0 and posicion <= self.__tope:
                return self.__items[posicion]
        except TypeError:
            pass

    def recorrer(self):
        print("·············································")
        for i in range(self.__tope):
            print(self.__items[i])


if __name__ == '__main__':
    lista = ListaSecuencialOrdenadaPorContenido(10)
    lista.insertar(20)
    lista.insertar(5)
    lista.insertar(10)
    lista.insertar(21)
    lista.insertar(30)
    lista.recorrer()
    lista.suprimir(10)
    lista.recorrer()
