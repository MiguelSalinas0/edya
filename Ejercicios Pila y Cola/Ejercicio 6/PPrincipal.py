from ColaEncadenada import Cola
import random

if __name__ == '__main__':
    cola = Cola()
    frecCliente = int(input('Ingrese la frecuencia de llegada del cliente: '))
    caOcupado = cajero = int(input('Ingrese tiempo de atención de cajero: '))
    simulacion = int(input('Tiempo máximo de simulación: '))
    reloj = 0
    tiempoAcumulado = 0
    clienteAtendido = 0
    while reloj < simulacion:
        nro_aleatorio = random.random()
        if nro_aleatorio <= 1 / frecCliente:
            cola.insertar(reloj)
        if cajero == 0 and not cola.vacia():
            num = cola.suprimir()
            tiempo_espera = reloj - num
            tiempoAcumulado += tiempo_espera
            clienteAtendido += 1
            cajero = caOcupado
        reloj += 1
        if cajero > 0:
            cajero -= 1
    print('Tiempo promedio de espera: {}'.format(tiempoAcumulado/clienteAtendido))
    print('Cantidad de clientes atendidos: {}'.format(clienteAtendido))