class Manejador:

    __cantM = 0

    def __init__(self):
        self.__cantM = 0

    def mostrar(self, pila1, pila2, pila3):
        print('\n--------------')
        pila1.mostrar()
        pila2.mostrar()
        pila3.mostrar()
        print('\n--------------\n')

    def movimiento(self, pilaO, pilaD, topeO):
        if (pilaD.vacia()):
            dato = pilaO.suprimir()
            pilaD.agregar(dato)
            self.__cantM += 1
        else:
            topeD = pilaD.getTope()
            if (topeO > topeD):
                dato = pilaO.suprimir()
                pilaD.agregar(dato)
                self.__cantM += 1
            else:
                print('\nNo es posible realizar el movimiento\n')

    def getCant(self):
        return self.__cantM
