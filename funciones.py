import json
from jsonschema import ValidationError, validate
from jinja2 import Environment, PackageLoader, select_autoescape
from clases import *

def leerJSON(nombreJSON):
    try:
        with open(nombreJSON, "r") as file:
            tps = json.load(file)
            validate(instance=tps, schema=schema)
            return tps
    except FileNotFoundError:
        print("No se encontró el archivo JSON")
        exit(0)

    except ValidationError as e:
        print("El JSON esta mal formado,", e)
        exit(1)

def handlerTipoCliente(tipo, tps):
        if tipo=="CLASSIC":
            cliente = Classic(tps["nombre"], tps["apellido"], tps["numero"], tps["dni"],tps["transacciones"])
        if tipo == "BLACK":
            cliente = Black(tps["nombre"], tps["apellido"], tps["numero"], tps["dni"],tps["transacciones"])
        if tipo == "GOLD":
            cliente = Gold(tps["nombre"], tps["apellido"], tps["numero"], tps["dni"],tps["transacciones"])
        return cliente

def handlerTipoTransaccion(transaccion, cliente):
    if transaccion["tipo"] == "RETIRO_EFECTIVO_CAJERO_AUTOMATICO":
        return cliente.puedeRetirar(transaccion["monto"], transaccion["saldoEnCuenta"], transaccion["cupoDiarioRestante"])

    if transaccion["tipo"] == "ALTA_CHEQUERA":
        return cliente.puedeCrearChequera(transaccion["totalChequerasActualmente"])
    
    if transaccion["tipo"] == "ALTA_TARJETA_CREDITO":
        return cliente.puedeCrearTarjeta(transaccion["totalTarjetasDeCreditoActualmente"])

    if transaccion["tipo"] == "COMPRA_DOLAR":
        return cliente.puedeComprarDolar(transaccion["monto"], transaccion["saldoEnCuenta"])

    if transaccion["tipo"] == "TRANSFERENCIA_ENVIADA":
        return cliente.puedeHacerTransferencia(transaccion["saldoEnCuenta"], transaccion["monto"])

    if transaccion["tipo"] == "TRANSFERENCIA_RECIBIDA":
        return cliente.puedeRecibirTransferencia(transaccion["monto"])
    

def generarHTML(tps, rechazo):
    env = Environment(
    loader=PackageLoader("paquete"),
    autoescape=select_autoescape()
    )

    template = env.get_template("template.html")

    with open("reporte.html", "w") as file:
        file.write(template.render(tps=tps, rechazo=rechazo))
        

schema = {
    "type": "object",
    "properties":{
        "numero": {"type": "number"},
        "nombre": {"type": "string"},
        "apellido": {"type": "string"},
        "DNI": {"type": "string"},
        "tipo": {"enum": ["BLACK", "CLASSIC", "GOLD"]},
        "transacciones": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "estado": {"enum": ["ACEPTADA", "RECHAZADA"]},
                    "tipo": {"type": "string"},
                    "cuentaNumero": {"type": "number"},
                    "cupoDiarioRestante": {"type": "number"},
                    "monto": {"type": "number"},
                    "fecha": {"type": "string"},
                    "numero": {"type": "number"},
                    "saldoEnCuenta": {"type": "number"},
                    "totalTarjetasDeCreditoActualmente": {"type": "number"},
                    "totalChequerasActualmente": {"type": "number"}
                }
            }
        }
    }
}