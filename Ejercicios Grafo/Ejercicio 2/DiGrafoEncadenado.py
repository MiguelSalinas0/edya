import numpy as np
from ListaEnlazada import ListaEnlazada

import networkx as nx
import matplotlib.pyplot as plt

Nodo = str


class DiGrafoEncadenado:

    __nodos: None
    __adyacencia: None

    def __init__(self, nodos: list[Nodo], adyacencia: list[tuple[Nodo, Nodo]]):
        self.__nodos = np.array(nodos)
        self.__adyacencia = np.array([ListaEnlazada() for i in range(len(nodos))])

        for nodo1, nodo2 in adyacencia:
            i = self._posNodo(nodo1)
            j = self._posNodo(nodo2)

            self.__adyacencia[i].insertar(j)

    def _posNodo(self, nodo):
        for i in range(len(self.__nodos)):
            if self.__nodos[i] == nodo:
                return i
        raise Exception("Nodo invalido")

    def nodosSalida(self, nodo):
        posNodo = self._posNodo(nodo)
        nodos = []
        for i in range(len(self.__adyacencia)):
            if self.__adyacencia[posNodo][i]:
                nodos.append(self.__nodos[i])
        return nodos

    def nodosEntrada(self, nodo):
        posNodo = self._posNodo(nodo)
        nodos = []
        for i in range(len(self.__adyacencia)):
            if self.__adyacencia[i][posNodo]:
                nodos.append(self.__nodos[i])
        return nodos

    def nodosFuente(self, nodo):
        longitud = self.nodosEntrada(nodo)
        return True if longitud == 0 else False

    def nodosSumidero(self, nodo):
        longitud = self.nodosSalida(nodo)
        return True if longitud == 0 else False

    @staticmethod
    def graficar(nodos: list[Nodo], adyacencia: list[tuple[Nodo, Nodo]]):
        G = nx.DiGraph()
        G.add_nodes_from(nodos)
        G.add_edges_from(adyacencia)
        nx.draw(G, with_labels=True)
        plt.show()


if __name__ == '__main__':
    nodos = ['A', 'B', 'C', 'D', 'E', 'F']
    adyacencia = [('A', 'B'), ('A', 'D'), ('B', 'C'), ('B', 'E'), ('B', 'F'), ('C', 'D'), ('D', 'B'), ('E', 'D'), ('E', 'F'), ('F', 'D'), ('F', 'A')]

    grafo = DiGrafoEncadenado(nodos, adyacencia)

    # print(grafo.esAciclico())
    print(grafo.nodosFuente())
    grafo.graficar(nodos, adyacencia)
