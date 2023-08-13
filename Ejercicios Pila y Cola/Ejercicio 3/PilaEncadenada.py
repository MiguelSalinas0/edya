class Nodo:

    __dato = None
    __sig = None

    def obtenerItem(self):
        return self.__dato

    def cargarItem(self, dato):
        self.__dato = dato

    def setSig(self, tope):
        self.__sig = tope

    def getSig(self):
        return self.__sig


class Pila:

    __tope = None
    __cantidad = 0

    def __init__(self):
        self.__cantidad = 0
        self.__tope = None

    def vacia(self):
        return self.__cantidad == 0

    def insertar(self, dato):
        nodo = Nodo()
        nodo.cargarItem(dato)
        nodo.setSig(self.__tope)
        self.__tope = nodo
        self.__cantidad += 1

    def suprimir(self):
        aux = Nodo()
        item = 0
        if (self.vacia()):
            print('Pila Vacia')
        else:
            aux = self.__tope
            item = self.__tope.obtenerItem()
            self.__tope = self.__tope.getSig()
            self.__cantidad -= 1
            del aux
            return item

    def mostrar(self):
        aux = self.__tope
        while aux != None:
            print('[{}] '.format(aux.obtenerItem()), end='')
            aux = aux.getSig()
