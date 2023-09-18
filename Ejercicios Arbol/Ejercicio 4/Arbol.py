'''
Ejercicio Nº4: Usando el mismo objeto de datos del ej. 1, implemente una función para c/u de los siguientes incisos:
a) Mostrar el nodo padre y el nodo hermano, de un nodo previamente ingresado por teclado; éste puede o no existir en el árbol.
b) mostrar la cantidad de nodos del árbol en forma recursiva.
c) Mostrar la altura de un árbol.
d) Mostrar los sucesores de un nodo ingresado previamente por teclado.
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
    

    def _inorden_recursivo(self, nodo, clave):
        if nodo:
            self._inorden_recursivo(nodo.getIzquierda(), clave)
            if nodo.getDato() != clave:
                print(nodo.getDato(), end=" ")
            self._inorden_recursivo(nodo.getDerecha(), clave)


    ######################### INCISO A #########################
    def mostrarPadreHermano(self, clave):
        def _padre_hermano(nodoPadre, nodoHijo, clave):
            if nodoHijo is None:
                return None
            if clave == nodoHijo.getDato():
                print(f'Padre: {nodoPadre.getDato()}')
                if nodoPadre.getIzquierda() is not None and nodoPadre.getDerecha() is not None:
                    if nodoPadre.getIzquierda().getDato() == clave:
                        print(f'Hermano: {nodoPadre.getDerecha().getDato()}')
                    else:
                        print(f'Hermano: {nodoPadre.getIzquierda().getDato()}')
                else:
                    print('No tiene hermano')
            elif clave < nodoHijo.getDato():
                nodoPadre = nodoHijo
                return _padre_hermano(nodoPadre, nodoHijo.getIzquierda(), clave)
            else:
                nodoPadre = nodoHijo
                return _padre_hermano(nodoPadre, nodoHijo.getDerecha(), clave)
        if self.__raiz is None:
            raise Exception('Arbol vacio')
        else:
            return _padre_hermano(self.__raiz, self.__raiz, clave)
        

    ######################### INCISO B #########################
    def contar_nodos(self):
        return self._contar_nodos_recursivo(self.__raiz)

    def _contar_nodos_recursivo(self, nodo_actual):
        if nodo_actual is None:
            return 0
        return 1 + self._contar_nodos_recursivo(nodo_actual.getIzquierda()) + self._contar_nodos_recursivo(nodo_actual.getDerecha())


    ######################### INCISO C #########################
    def altura(self):
        def _altura_recursiva(nodo):
            if nodo is None:
                return 0
            else:
                altura_izquierda = _altura_recursiva(nodo.getIzquierda())
                altura_derecha = _altura_recursiva(nodo.getDerecha())
                return max(altura_izquierda, altura_derecha) + 1
        return _altura_recursiva(self.__raiz)
    

    ######################### INCISO D #########################
    def sucesores(self, clave):
        def _sucesores_recursivo(nodo, clave):
            if nodo is None:
                return None
            if clave == nodo.getDato():
                self._inorden_recursivo(nodo, clave)
            elif clave < nodo.getDato():
                return _sucesores_recursivo(nodo.getIzquierda(), clave)
            else:
                return _sucesores_recursivo(nodo.getDerecha(), clave)
        if self.__raiz is None:
            raise Exception('Arbol vacio')
        else:
            return _sucesores_recursivo(self.__raiz, clave)


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
    print(arbol.contar_nodos())
    print(arbol.altura())
    arbol.mostrarPadreHermano(23)
    arbol.sucesores(23)