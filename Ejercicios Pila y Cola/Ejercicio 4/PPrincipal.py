from Pila import Pila
from Pila2 import Pila2
from Pila3 import Pila3
from manejador import Manejador

if __name__ == '__main__':
    maneja = Manejador()
    n = int(input('Ingrese la cantidad de discos: '))
    pila1 = Pila(n)
    pila2 = Pila2(n)
    pila3 = Pila3(n)
    cantM = 0
    for i in range(n):
        pila1.agregar(i*5)
    maneja.mostrar(pila1, pila2, pila3)
    while (pila3.llena2(pila1.getCantidad()) == False):
        origen = int(input('Seleccione de que pila mover el disco: '))
        destino = int(input('Seleccione a que pila mover el disco: '))
        if (origen == 1):
            topeO = pila1.getTope()
            if (destino == 2):
                maneja.movimiento(pila1, pila2, topeO)
                maneja.mostrar(pila1, pila2, pila3)
            if (destino == 3):
                maneja.movimiento(pila1, pila3, topeO)
                maneja.mostrar(pila1, pila2, pila3)
        if (origen == 2):
            topeO = pila2.getTope()
            if (destino == 1):
                maneja.movimiento(pila2, pila1, topeO)
                maneja.mostrar(pila1, pila2, pila3)
            if (destino == 3):
                maneja.movimiento(pila2, pila3, topeO)
                maneja.mostrar(pila1, pila2, pila3)
        if (origen == 3):
            topeO = pila3.getTope()
            if (destino == 1):
                maneja.movimiento(pila3, pila1, topeO)
                maneja.mostrar(pila1, pila2, pila3)
            if (destino == 2):
                maneja.movimiento(pila3, pila2, topeO)
                maneja.mostrar(pila1, pila2, pila3)
    print('\nCantidad de movimientos realizados es de: {}'.format(maneja.getCant()))
    print('\nLa cantidad mínima de jugadas para {} discos es de: {}\n'.format(n, (2**n)-1))
