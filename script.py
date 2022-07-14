# pip install jsonschema
"""
tipo de cliente: CLASSIC, GOLD, BLACK
tipo de cuenta: Caja de ahorro en pesos, Caja de ahorro en dólares, Cuenta corriente
"""

"""
classic:
    1 sola tarjeta de credito
    1 sola caja de ahorro
    No puede comprar/vender dolares, no tiene cuenta en dolares
    maximo de retiro: 10.000
    no tiene tarjeta de credito ni chequera
    comision por transferencia: 1%
    maximo transferencia recibida: 150.000
"""

# leo el json y lo valido
# por cada transaccion agrego al reporte con los siguientes datos:
    # nombre de cliente, número, DNI, dirección y para cada transacción la fecha , el tipo de operación, el estado, el monto y razón por la cual se rechazó (vacío en caso de ser aceptada).
# el reporte es una lista en html

from funciones import *
from clases import *

def main():
    rechazo = []
    nombreJSON = input("Ingrese el nombre del archivo: ")
    tps = leerJSON(nombreJSON)
    cliente = handlerTipoCliente(tps["tipo"] ,tps)
    # print(cliente.transacciones)
    for transaccion in cliente.transacciones:
        if transaccion["estado"] == "RECHAZADA":
            rechazo.append(handlerTipoTransaccion(transaccion, cliente))
        else:
            rechazo.append("-")

    print(rechazo)
    generarHTML(tps, rechazo)


main()


