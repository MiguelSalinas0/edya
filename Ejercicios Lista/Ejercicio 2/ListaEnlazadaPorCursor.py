import numpy as np


class Celda:

    __item = None
    __sig = None

    def __init__(self, valor, siguiente):
        self.__item = valor
        self.__sig = siguiente

    def setItem(self, item):
        self.__item = item

    def getItem(self):
        return self.__item

    def setSig(self, sig):
        self.__sig = sig

    def getSig(self):
        return self.__sig

    def __repr__(self):
        return f'[{self.__item} => {self.__sig}]'


class ListaEnlazadaPorCursor:

    __elementos: None
    __inicio: int
    __inicioVacio: int
    __cantElementos: int

    def __init__(self, dimension):
        self.__elementos = np.empty(dimension, dtype=Celda)
        self.__inicio = -1
        self.__inicioVacio = 0
        self.__cantElementos = 0

        for i in range(dimension - 1):
            self.__elementos[i] = Celda(None, i + 1)
        self.__elementos[dimension - 1] = Celda(None, -1)

    def __posicionValida(self, pos):
        return 0 <= pos <= self.__cantElementos

    def llena(self):
        return self.__inicioVacio == -1

    def vacia(self):
        return self.__inicio == -1

    def getDimension(self):
        return self.__cantElementos

    def insertar(self, dato, pos=-1):
        if pos == -1:
            pos = self.__cantElementos
        if self.llena():
            raise Exception('La lista está llena')
        elif not self.__posicionValida(pos):
            raise Exception('La posición no es válida')
        posElem = self.__inicioVacio
        elemento = self.__elementos[posElem]
        elemento.setItem(dato)
        self.__inicioVacio = elemento.getSig()
        if pos == 0:
            elemento.setSig(self.__inicio)
            self.__inicio = posElem
        else:
            anterior = self.__recuperar(pos - 1)
            elemento.setSig(anterior.getSig())
            anterior.setSig(posElem)
        self.__cantElementos += 1

    def eliminar(self, pos):
        if not self.__posicionValida(pos):
            raise Exception('La posición no es válida')
        if pos == 0:
            aux = self.__inicio
            self.__inicio = self.__elementos[aux].getSig()
            self.__elementos[aux].setSig(self.__inicioVacio)
            self.__inicioVacio = aux
        else:
            anterior = self.__recuperar(pos - 1)
            aux = anterior.getSig()
            anterior.setSig(self.__elementos[aux].getSig())
            self.__elementos[aux].setSig(self.__inicioVacio)
            self.__inicioVacio = aux

    def buscar(self, elem):
        pos = self.__inicio
        while pos != -1 and self.__elementos[pos].getItem() != elem:
            pos = self.__elementos[pos].getSig()
        return pos

    def primerElemento(self):
        return self.__elementos[self.__inicio].getItem() if not self.vacia() else None

    def ultimoElemento(self):
        return None if self.vacia() else self.recuperar(self.__cantElementos - 1)

    def __recuperar(self, pos):
        aux = self.__inicio
        while pos != 0:
            aux = self.__elementos[aux].getSig()
            pos -= 1
        return self.__elementos[aux]

    def recuperar(self, pos):
        return self.__recuperar(pos).getItem() if self.__posicionValida(pos) else None

    def mostrar(self):
        print('\n')
        print('Inicio:', self.__inicio)
        print('Inicio vacio:', self.__inicioVacio)
        i = 0
        for elem in self.__elementos:
            print(f'{i}: {elem}')
            i += 1

    def __iter__(self):
        pos = self.__inicio
        while pos != -1:
            yield self.__elementos[pos].getItem()
            pos = self.__elementos[pos].getSig()

    def __repr__(self):
        return str(list(self))


if __name__ == '__main__':
    lista = ListaEnlazadaPorCursor(10)
    lista.insertar(100)
    lista.insertar(200)
    lista.insertar(300)
    lista.insertar(400)
    lista.mostrar()
    lista.eliminar(3)
    lista.insertar(800, 2)
    lista.mostrar()
