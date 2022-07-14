# Prerequisitos: 
# pip install jsonschema
# pip install Jinja2

from funciones import *
from clases import *

def main():
    rechazo = []
    nombreJSON = input("Ingrese el nombre del archivo: ")
    tps = leerJSON(nombreJSON)
    cliente = handlerTipoCliente(tps["tipo"] ,tps)
    
    for transaccion in cliente.transacciones:
        if transaccion["estado"] == "RECHAZADA":
            rechazo.append(handlerTipoTransaccion(transaccion, cliente))
        else:
            rechazo.append("-")

    generarHTML(tps, rechazo)


main()


