from Pila import Pila
from manejador import Manejador

if __name__ == '__main__':
    maneja = Manejador()
    n = int(input('Ingrese la cantidad de discos: '))
    pila1 = Pila(n)
    pila2 = Pila(n)
    pila3 = Pila(n)
    cantM = 0
    for i in range(n):
        pila1.agregar((n - i - 1) * 5)
    maneja.mostrar(pila1, pila2, pila3)
    while not (pila1.vacia() and pila2.vacia()) or not pila3.llena():
        origen = int(input('Seleccione pila origen: '))
        destino = int(input('Seleccione pila destino: '))
        if (origen == 1):
            topeO = pila1.getTope()
            if (destino == 2):
                maneja.movimiento(pila1, pila2, topeO)
            if (destino == 3):
                maneja.movimiento(pila1, pila3, topeO)
        if (origen == 2):
            topeO = pila2.getTope()
            if (destino == 1):
                maneja.movimiento(pila2, pila1, topeO)
            if (destino == 3):
                maneja.movimiento(pila2, pila3, topeO)
        if (origen == 3):
            topeO = pila3.getTope()
            if (destino == 1):
                maneja.movimiento(pila3, pila1, topeO)
            if (destino == 2):
                maneja.movimiento(pila3, pila2, topeO)
        maneja.mostrar(pila1, pila2, pila3)
    print('\nCantidad de movimientos realizados es de: {}'.format(maneja.getCant()))
    print('\nLa cantidad mínima de jugadas para {} discos es de: {}\n'.format(n, (2**n)-1))
