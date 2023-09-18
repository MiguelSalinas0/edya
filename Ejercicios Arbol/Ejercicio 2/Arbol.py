class Nodo:

    __dato = None
    __izquierda = None
    __derecha = None
    __frequencia = None

    def __init__(self, dato, frequencia):
        self.__dato = dato
        self.__frequencia = frequencia
        self.__izquierda = None
        self.__derecha = None

    def getFreq(self):
        return self.__frequencia

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

    def esHoja(self):
        return self.__izquierda is None and self.__derecha is None

    def __repr__(self):
        return f'( {self.__frequencia} - {self.__dato} )'


class Arbol:

    __raiz = None

    def __init__(self, raiz):
        self.__raiz = raiz

    def getRaiz(self):
        return self.__raiz
