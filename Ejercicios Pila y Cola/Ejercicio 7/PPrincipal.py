from ColaSecuencial import Cola
from ColaEncadenada import ColaEncadenada
import random

if __name__ == '__main__':
    turnos = ColaEncadenada()
    colaGinecologia = Cola(10)
    colaPediatria = Cola(10)
    colaClinica = Cola(10)
    colaOftalmologia = Cola(10)
    colas = [colaGinecologia, colaPediatria, colaClinica, colaOftalmologia]
    frecCliente = 1
    simulacion = 240
    reloj = 0
    cantCola = 0
    medico = 20
    tiempoEspera = 0
    atendidos = 0
    atencion = 0
    while reloj < simulacion:
        nro_aleatorio = random.random()
        if nro_aleatorio <= 1 / frecCliente:
            turnos.insertar(reloj)
            cantCola += 1
        if atencion == 0 and reloj < 60:
            if not turnos.vacia():
                tiempo = turnos.suprimir()
                espera = reloj - tiempo
                tiempoEspera += espera
                atendidos += 1
                atencion = 2
                op = random.randint(1, 4)
                if op == 1:
                    colas[0].insertar(reloj)
                elif op == 2:
                    colas[1].insertar(reloj)
                elif op == 3:
                    colas[2].insertar(reloj)
                elif op == 4:
                    colas[3].insertar(reloj)
        for i in range(4):
            if colas[i].getMedico() == 0:
                if colas[i].vacia() != True:
                    x = colas[i].suprimir()
                    x = reloj-x
                    colas[i].setTiempo(x)
                    colas[i].setMedico()
            if colas[i].getMedico() > 0:
                colas[i].decremetarMedico()
        reloj += 1
        if atencion > 0:
            atencion -= 1
    prom = tiempoEspera/atendidos
    print("Tiempo promedio de espera en la cola de turnos: {} minutos".format(prom))
    print("Personas que no pudieron obtener turno: ", cantCola-atendidos)
    for h in range(4):
        colas[h].obtenerPromedio(h)
