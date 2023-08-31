class Celda:

    __item = None
    __sig = None

    def setItem(self, item):
        self.__item = item

    def getItem(self):
        return self.__item

    def setSig(self, sig):
        self.__sig = sig

    def getSig(self):
        return self.__sig


class ListaEnlazadaOredenadaPorContenido:
    def __init__(self):
        self.__cant = 0
        self.__cabeza = None

    def vacia(self):
        return self.__cant == 0

    def insertar(self, elemento):
        nuevo = Celda()
        nuevo.setItem(elemento)
        if self.__cant == 0:
            nuevo.setSig(self.__cabeza)
            self.__cabeza = nuevo
        else:
            if self.__cabeza.getItem() < elemento:
                nuevo.setSig(self.__cabeza)
                self.__cabeza = nuevo
            else:
                aux = self.__cabeza
                anterior = aux.getSig()
                while aux != None and aux.getItem() < elemento:
                    anterior = aux
                    aux = aux.getSig()
                nuevo.setSig(aux)
                anterior.setSig(nuevo)
        self.__cant += 1

    def primer_elemento(self):
        if not self.vacia():
            return self.__cabeza.getItem()

    def ultimo_elemento(self):
        if not self.vacia():
            aux = self.__cabeza
            while aux.getSig() != None:
                aux = aux.getSig()
            return aux.getItem()

    def siguiente(self, posicion):
        if posicion <= self.__cant + 1:
            return posicion + 1

    def anterior(sefl, posicion):
        if posicion > 1:
            return posicion - 1

    def suprimir(self, elemento):
        if self.vacia():
            print("No se puede suprimir porque la lista esta vacia ")
        else:
            if elemento == self.__cabeza.getItem():
                aux = self.__cabeza
                item = self.__cabeza.getItem()
                self.__cabeza = self.__cabeza.getSig()
                del aux
                self.__cant -= 1
                return item
            else:
                aux = self.__cabeza
                anterior = self.__cabeza.getSig()
                while aux != None and aux.getItem() != elemento:
                    anterior = aux
                    aux = aux.getSig()
                if aux != None:
                    elemento = aux.getItem()
                    anterior.setSig(aux.getSig())
                    self.__cant -= 1
                    del aux
                    return elemento
                else:
                    print('El elemento no se encuentra en la lista')

    def recuperar(self, posicion):
        if posicion > 0 and posicion <= self.__cant + 1:
            if self.vacia():
                print("No se puede recuperar porque la lista esta vacia ")
            else:
                cont = 1
                aux = self.__cabeza
                while cont != posicion:
                    aux = aux.getSig()
                    cont += 1
                return aux.getItem()
        else:
            print("Posicion invalida ")

    def buscar(self, dato):
        if self.vacia():
            print("No existe el elemento porque la lista esta vacia ")
        else:
            cont = 1
            aux = self.__cabeza
            while aux != None and aux.getItem() != dato:
                aux = aux.getSig()
                cont += 1
            if aux == None:
                print("El elemento no existe ")
            else:
                print("Se encontro el elemento en la posicion {} de la lista".format(cont))
                return cont

    def recorrer(self):
        print("·············································")
        aux = self.__cabeza
        while aux != None:
            print(aux.getItem())
            aux = aux.getSig()


if __name__ == '__main__':
    lista = ListaEnlazadaOredenadaPorContenido()
    lista.insertar(20)
    lista.insertar(5)
    lista.insertar(10)
    lista.insertar(21)
    lista.insertar(30)
    lista.recorrer()
    lista.suprimir(10)
    lista.recorrer()
    print(lista.recuperar(1))
    print(lista.ultimo_elemento())
