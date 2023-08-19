class Celda:

    __item = 0
    __sig = None

    def cargarSig(self, tope):
        self.__sig = tope

    def getSig(self):
        return self.__sig

    def cargarItem(self, dato):
        self.__item = dato

    def getItem(self):
        return self.__item


class Cola:

    __cant = 0
    __ul = Celda()
    __pr = Celda()

    def __init__(self):
        self.__cant = 0
        self.__pr = None
        self.__ul = None

    def vacia(self):
        return self.__cant == 0

    def insertar(self, dato):
        celda = Celda()
        celda.cargarItem(dato)
        celda.cargarSig(None)
        if (self.__ul == None):
            self.__pr = celda
        else:
            self.__ul.cargarSig(celda)
        self.__ul = celda
        self.__cant += 1

    def suprimir(self):
        if (self.vacia()):
            print('Cola Vacia')
        else:
            aux = self.__pr
            dato = aux.getItem()
            self.__pr = self.__pr.getSig()
            self.__cant -= 1
            if self.__pr == None:
                self.__ul = None
            del aux
            return dato

    def getPr(self):
        return self.__pr.getItem()

    def mostrar(self):
        aux = self.__pr
        while(aux != None):
            print('dato {}'.format(aux.getItem()))
            aux = aux.getSig()


if __name__ == '__main__':
    cola = Cola()
    cola.insertar(50)
    cola.insertar(90)
    cola.insertar(75)
    cola.mostrar()
    cola.suprimir()
    print('---------')
    cola.insertar(750)
    cola.mostrar()
    cola.suprimir()
    print('---------')
    cola.mostrar()