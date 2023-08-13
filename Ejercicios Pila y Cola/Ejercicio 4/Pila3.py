class Pila3:

    __tope = 0
    __cantidad = 0
    __items = []

    def __init__(self, cantidad):
        self.__cantidad = cantidad

    def vacia(self):
        return self.__tope == 0

    def llena(self):
        return self.__tope == self.__cantidad

    def agregar(self, dato):
        if (self.llena()):
            print('Pila Llena')
        else:
            self.__items.append(dato)
            self.__tope += 1

    def suprimir(self):
        eliminado = None
        if (self.vacia()):
            print('Pila Vacia')
        else:
            eliminado = self.__items.pop()
            self.__tope -= 1
        return eliminado

    def getTope(self):
        return self.__items[self.__tope-1]

    def llena2(self, cantidad):
        return self.__tope == cantidad

    def mostrar(self):
        print('\nPila 3')
        if (self.vacia()):
            print('[]')
        for i in range(self.__tope):
            print('[{}] '.format(self.__items[i]), end="")
