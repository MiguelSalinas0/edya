import numpy as np


class Cola:

    __max = 0
    __pr = 0
    __ul = 0
    __cant = 0
    __items = None
    __medico = 0
    __tiempo = 0
    __cola = 0

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
            self.__cola += 1

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
        if (not self.vacia()):
            i = self.__pr
            while j < self.__cant:
                print(self.__items[i])
                i = (i + 1) % self.__max
                j += 1




    def getMedico(self):
        return self.__medico

    def setMedico(self):
        self.__medico = 20

    def decremetarMedico(self):
        self.__medico = self.__medico-1

    def getTiempo(self):
        return self.__tiempo

    def setTiempo(self, x):
        self.__tiempo = self.__tiempo+x

    def obtenerPromedio(self, i):
        promedio = self.getTiempo()/self.__cola
        print("Tiempo promedio de espera de especialidad", i+1, ":", promedio)
