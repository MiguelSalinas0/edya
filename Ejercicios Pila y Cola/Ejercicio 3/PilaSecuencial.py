class Pila:

    __tope = 0
    __cantidad = 0
    __items = []

    def __init__(self, cantidad):
        self.__cantidad = cantidad

    def vacia(self):
        return self.__tope == 0

    def llena(self):
        return self.__tope == self.__cantidad

    def insertar(self, dato):
        if (self.llena()):
            print('Pila Lena')
        else:
            self.__items.append(dato)
            self.__tope += 1

    def suprimir(self):
        eliminado = None
        if(self.vacia()):
            print('Pila Vacia')
        else:
            eliminado = self.__items.pop()
            self.__tope -= 1
        return eliminado

    def mostrar(self):
        for i in range(self.__tope):
            print('[{}] '.format(self.__items[i]), end='')
            