class Cliente:
    def __init__(self,nombre, apellido, numero, dni, transacciones):
        self.nombre = nombre
        self.apellido = apellido
        self.numero = numero
        self.dni = dni
        self.transacciones = transacciones

class Classic(Cliente):
    comision = 0.01
    maximoDiario = 10000
    transferenciaMaxima = 150000

    def puedeCrearChequera(self, cantChequeras):
        return "Un cliente classic no puede tener chequera"

    def puedeCrearTarjeta(self, cantTarjetas):
        return "Un cliente classic no puede tener tarjeta de credito"

    def puedeComprarDolar(self, monto, saldoEnCuenta):
        return "Un cliente classic no puede comprar dolares"

    def puedeHacerTransferencia(self, saldoEnCuenta, monto):
        if saldoEnCuenta >= (monto + monto*self.comision):
            return True
        return "El saldo en cuenta es menor al monto requerido para transferir"
    
    def puedeRecibirTransferencia(self, monto):
        if monto > self.transferenciaMaxima:
            return "El monto es mayor al limite por transferencias ($150000)"

    def puedeRetirar(self, monto, saldoEnCuenta, cupoDiarioRestante):
        if monto > saldoEnCuenta:
            return "El monto execede el dinero en cuenta"
        if monto > cupoDiarioRestante:
            return "El monto execede el cupo diario restante"
        return True

 
class Gold(Cliente):
    comision = 0.005
    maximoDiario = 20000
    descubierto = 10000
    transferenciaMaxima = 500000

    def puedeCrearChequera(self, cantChequeras):
        if(cantChequeras < 1):
            return True
        return "Ya superas el limite de chequeras (1)"

    def puedeCrearTarjeta(self, cantTarjetas):
        if(cantTarjetas < 1):
            return True
        return "Ya superas el limite de tajetas de credito (1)"
    
    def puedeHacerTransferencia(self, saldoEnCuenta, monto):
        if saldoEnCuenta >= (monto + monto*self.comision):
            return True
        return "El saldo en cuenta es menor al monto requerido para transferir"
    
    def puedeRecibirTransferencia(self, monto):
        if monto > self.transferenciaMaxima:
            return "El monto es mayor al limite por transferencias ($500000)"
        
    def puedeRetirar(self, monto, saldoEnCuenta, cupoDiarioRestante):
        if monto > (saldoEnCuenta + self.descubierto):
            return "El monto execede el dinero en cuenta"
        if monto > cupoDiarioRestante:
            return "El monto execede el cupo diario restante"
        return True

    def puedeComprarDolar(self, monto, saldoEnCuenta):
        if saldoEnCuenta >= monto:
            return True
        return "No tiene saldo suficiente"


class Black(Cliente):
    maximoDiario = 100000
    descubierto = 10000

    def puedeCrearChequera(self, cantChequeras):
        if(cantChequeras < 2):
            return True
        return "Ya superas el limite de chequeras (2)"

    def puedeCrearTarjeta(self, cantTarjetas):
        if(cantTarjetas < 5):
            return True
        return "Ya superas el limite de tajetas de credito (5)"

    def puedeHacerTransferencia(self, saldoEnCuenta, monto):
        if saldoEnCuenta >= monto:
            return True
        return "El saldo en cuenta es menor al monto requerido para transferir"
    
    def puedeRetirar(self, monto, saldoEnCuenta, cupoDiarioRestante):
        if monto > (saldoEnCuenta + self.descubierto):
            return "El monto execede el dinero en cuenta"
        if monto > cupoDiarioRestante:
            return "El monto execede el cupo diario restante"
        return True

    def puedeComprarDolar(self, monto, saldoEnCuenta):
        if saldoEnCuenta >= monto:
            return True
        return "No tiene saldo suficiente"
    
