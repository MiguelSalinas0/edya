'''
Ejercicio Nº3: Teniendo en cuenta que la frontera de un árbol binario es el conjunto de nodos terminales de éste, tomados de izquierda a derecha;
implemente un método que muestre la frontera de un ABB.
'''

class Nodo:

    __dato = None
    __izquierda = None
    __derecha = None

    def __init__(self, dato):
        self.__dato = dato
        self.__izquierda = None
        self.__derecha = None

    def getDato(self):
        return self.__dato

    def getIzquierda(self):
        return self.__izquierda

    def getDerecha(self):
        return self.__derecha

    def setDato(self, dato):
        self.__dato = dato

    def setIzquierda(self, izq):
        self.__izquierda = izq

    def setDerecha(self, der):
        self.__derecha = der


class Arbol:

    __raiz = None

    def __init__(self):
        self.__raiz = None

    def insertar(self, valor):
        def _insertar_recursivamente(nodo, valor):
            if valor < nodo.getDato():
                if nodo.getIzquierda() is None:
                    nodo.setIzquierda(Nodo(valor))
                else:
                    _insertar_recursivamente(nodo.getIzquierda(), valor)
            elif valor > nodo.getDato():
                if nodo.getDerecha() is None:
                    nodo.setDerecha(Nodo(valor))
                else:
                    _insertar_recursivamente(nodo.getDerecha(), valor)
            else:
                print('Valor duplicado')
        if self.__raiz is None:
            self.__raiz = Nodo(valor)
        else:
            _insertar_recursivamente(self.__raiz, valor)


    ######################### SOLUCION #########################
    def hoja(self, nodo):
        return nodo is not None and nodo.getIzquierda() is None and nodo.getDerecha() is None

    def frontera(self):
        frontera = []
        def _frontera_recursivo(nodo):
            if nodo:
                _frontera_recursivo(nodo.getIzquierda())
                if self.hoja(nodo):
                    frontera.append(nodo.getDato())
                _frontera_recursivo(nodo.getDerecha())
        _frontera_recursivo(self.__raiz)
        return frontera


if __name__ == '__main__':
    arbol = Arbol()
    arbol.insertar(45)
    arbol.insertar(23)
    arbol.insertar(65)
    arbol.insertar(2)
    arbol.insertar(38)
    arbol.insertar(52)
    arbol.insertar(48)
    arbol.insertar(96)
    arbol.insertar(7)
    print(arbol.frontera())
