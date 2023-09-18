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

    def nivel(self, clave):
        def _nivel_recursivo(nodo, clave, nivel_actual):
            if nodo is None:
                return -1
            if clave == nodo.getDato():
                return nivel_actual
            elif clave < nodo.getDato():
                return _nivel_recursivo(nodo.getIzquierda(), clave, nivel_actual + 1)
            else:
                return _nivel_recursivo(nodo.getDerecha(), clave, nivel_actual + 1)
        return _nivel_recursivo(self.__raiz, clave, 1)

    def hoja(self, clave):
        nodo = self.buscar(clave)
        return nodo is not None and nodo.getIzquierda() is None and nodo.getDerecha() is None

    def altura(self):
        def _altura_recursiva(nodo):
            if nodo is None:
                return 0
            else:
                altura_izquierda = _altura_recursiva(nodo.getIzquierda())
                altura_derecha = _altura_recursiva(nodo.getDerecha())
                return max(altura_izquierda, altura_derecha) + 1
        return _altura_recursiva(self.__raiz)

    def buscar(self, clave):
        def _buscar_recursivo(nodo, clave):
            if nodo is None:
                return None
            if clave == nodo.getDato():
                return nodo
            elif clave < nodo.getDato():
                return _buscar_recursivo(nodo.getIzquierda(), clave)
            else:
                return _buscar_recursivo(nodo.getDerecha(), clave)
        if self.__raiz is None:
            raise Exception('Arbol vacio')
        else:
            return _buscar_recursivo(self.__raiz, clave)

    def es_hijo(self, clavePadre, claveHijo):
        nodoPadre = self.buscar(clavePadre)
        if nodoPadre is None:
            return False
        else:
            if nodoPadre.getIzquierda() is not None and nodoPadre.getIzquierda().getDato() == claveHijo:
                return True
            elif nodoPadre.getDerecha() is not None and nodoPadre.getDerecha().getDato() == claveHijo:
                return True
            else:
                return False

    def es_padre(self, claveHijo, clavePadre):
        return self.es_hijo(clavePadre, claveHijo)

    def inorden(self):
        def _inorden_recursivo(nodo):
            if nodo:
                _inorden_recursivo(nodo.getIzquierda())
                print(nodo.getDato(), end=" ")
                _inorden_recursivo(nodo.getDerecha())
        _inorden_recursivo(self.__raiz)
        print()

    def preorden(self):
        def _preorden_recursivo(nodo):
            if nodo:
                print(nodo.getDato(), end=" ")
                _preorden_recursivo(nodo.getIzquierda())
                _preorden_recursivo(nodo.getDerecha())
        _preorden_recursivo(self.__raiz)
        print()

    def postorden(self):
        def _postorden_recursivo(nodo):
            if nodo:
                _postorden_recursivo(nodo.getIzquierda())
                _postorden_recursivo(nodo.getDerecha())
                print(nodo.getDato(), end=" ")
        _postorden_recursivo(self.__raiz)
        print()

    def suprimir(self, clave):
        self.__raiz = self._suprimir_recursivo(self.__raiz, clave)

    def _suprimir_recursivo(self, nodo, clave):
        if nodo is None:
            return nodo

        # Si la clave es menor que el valor actual, buscar en el subárbol izquierdo
        if clave < nodo.getDato():
            izq = self._suprimir_recursivo(nodo.getIzquierda(), clave)
            nodo.setIzquierda(izq)

        # Si la clave es mayor que el valor actual, buscar en el subárbol derecho
        elif clave > nodo.getDato():
            der = self._suprimir_recursivo(nodo.getDerecha(), clave)
            nodo.setDerecha(der)

        # Si la clave es igual al valor actual, encontramos el nodo a eliminar
        else:

            # Caso 1: Nodo es una hoja o tiene un solo hijo
            if nodo.getIzquierda() is None:
                return nodo.getDerecha()
            elif nodo.getDerecha() is None:
                return nodo.getIzquierda()

            # Caso 2: Nodo tiene dos hijos, encontrar el sucesor inorden
            sucesor = self._encontrar_minimo(nodo.getDerecha())
            dat = sucesor.getDato()
            nodo.setDato(dat)
            der = self._suprimir_recursivo(
                nodo.getDerecha(), sucesor.getDato())
            nodo.setDerecha(der)
        return nodo

    def _encontrar_minimo(self, nodo):
        while nodo.getIzquierda() is not None:
            nodo = nodo.getIzquierda()
        return nodo

    def camino(self, origen, destino):
        def buscar_camino_desde_nodo(nodo, destino):
            if nodo is None:
                return False
            if nodo.getDato() == destino:
                return True
            elif nodo.getDato() > destino:
                return buscar_camino_desde_nodo(nodo.getIzquierda(), destino)
            else:
                return buscar_camino_desde_nodo(nodo.getDerecha(), destino)
        nodo_origen = self.buscar(origen)
        if nodo_origen is not None:
            return buscar_camino_desde_nodo(nodo_origen, destino)


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
    print('---- Inorden ----')
    arbol.inorden()
    print('---- Preorden ----')
    arbol.preorden()
    print('---- Postorden ----')
    arbol.postorden()
    print("El nivel del nodo es {}".format(arbol.nivel(52)))
    print(arbol.hoja(7))
    print(arbol.altura())
    arbol.suprimir(52)
    print('---- Inorden ----')
    arbol.inorden()
    print(arbol.buscar(96))
    print(arbol.es_hijo(2, 7))
    print(arbol.es_padre(7, 2))
    print(arbol.camino(23, 7))
