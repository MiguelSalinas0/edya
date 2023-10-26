import numpy as np
from ListaEnlazada import ListaEnlazada

import networkx as nx
import matplotlib.pyplot as plt

Nodo = str


class GrafoEncadenado:

    __nodos: None
    __adyacencia: None

    def __init__(self, nodos: list[Nodo], adyacencia: list[tuple[Nodo, Nodo]]):
        self.__nodos = np.array(nodos)
        self.__adyacencia = np.array([ListaEnlazada() for i in range(len(nodos))])

        for nodo1, nodo2 in adyacencia:
            i = self._posNodo(nodo1)
            j = self._posNodo(nodo2)

            self.__adyacencia[i].insertar(j)
            self.__adyacencia[j].insertar(i)

    def _posNodo(self, nodo):
        for i in range(len(self.__nodos)):
            if self.__nodos[i] == nodo:
                return i
        raise Exception("Nodo invalido")

    def adyacentes(self, nodo: Nodo):
        posNodo = self._posNodo(nodo)
        adyacentes = []
        for i in range(len(self.__adyacencia)):
            if self.__adyacencia[posNodo][i] == 1:
                adyacentes.append(self.__nodos[i])
        return adyacentes

    def camino(self, inicio, destino, recorridos):
        if inicio == destino:
            return [destino]
        recorridos.append(inicio)
        for nodo in self.adyacentes(inicio):
            if nodo not in recorridos:
                camino = self.camino(nodo, destino, recorridos)
                if camino != None:
                    return [inicio] + camino
        raise Exception("No hay camino")

    def recorridoEnAncho(self, nodo, callback):
        recorridos = []
        cola = [nodo]
        while len(cola) > 0:
            nodo_actual = cola.pop(0)
            callback(nodo_actual)
            recorridos.append(nodo_actual)
            for nodo in self.adyacentes(nodo_actual):
                if nodo not in recorridos:
                    cola.append(nodo)
                    recorridos.append(nodo)

    def esConexo(self):
        encontrados = []
        self.recorridoEnAncho(self.__nodos[0], lambda nodo: encontrados.append(nodo))
        return len(encontrados) == len(self.__nodos)

    @staticmethod
    def graficar(nodos: list[Nodo], adyacencia: list[tuple[Nodo, Nodo]]):
        G = nx.Graph()
        G.add_nodes_from(nodos)
        G.add_edges_from(adyacencia)
        nx.draw(G, with_labels=True)
        plt.show()


if __name__ == '__main__':
    nodos = ['A', 'B', 'C', 'D', 'E', 'F']
    adyacencia = [('A', 'B'), ('A', 'D'), ('B', 'C'), ('B', 'E'), ('B', 'F'), ('C', 'D'), ('D', 'B'), ('E', 'D'), ('E', 'F'), ('F', 'D'), ('F', 'A')]

    grafo = GrafoEncadenado(nodos, adyacencia)

    print(grafo.camino('A', 'D', []))
    print(grafo.camino('A', 'E', []))
    print(grafo.camino('C', 'F', []))
    print(grafo.esConexo())
    grafo.graficar(nodos, adyacencia)
