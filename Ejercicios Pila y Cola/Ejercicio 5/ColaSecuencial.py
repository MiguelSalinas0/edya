import numpy as np

class Cola:

    __max = 0
    __pr = 0
    __ul = 0
    __cant = 0
    __items = None

    def __init__(self, max):
        self.__max = max
        self.__items = np.empty(max, dtype=int)

    def vacia(self):
        return self.__cant == 0

    def insertar(self, dato):
        if (self.__cant < self.__max):
            self.__items[self.__ul] = dato
            self.__ul = (self.__ul + 1) % self.__max
            self.__cant += 1

    def suprimir(self):
        if (self.vacia()):
            print('Cola Vacia')
        else:
            eliminado = self.__items[self.__pr]
            self.__pr = (self.__pr + 1) % self.__max
            self.__cant -= 1
            return eliminado

    def mostrar(self):
        j = 0
        if(not self.vacia()):
            i = self.__pr
            while j < self.__cant:
                print(self.__items[i])
                i = (i + 1) % self.__max
                j += 1



if __name__ == '__main__':
    cola = Cola(3)
    cola.insertar(5)
    cola.insertar(10)
    cola.insertar(15)
    cola.mostrar()
    print('-----------')
    cola.suprimir()
    cola.mostrar()
    print('-----------')
    cola.insertar(20)
    cola.suprimir()
    cola.mostrar()