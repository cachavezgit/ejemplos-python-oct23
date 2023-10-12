class CuentaBancaria:
    numero_de_cuenta = ''

    def __init__(self,no_cuenta):
        self.numero_de_cuenta = no_cuenta

class CuentaDeCheques(CuentaBancaria):
    linea_de_sobregiro = 0.0

    def __init__(self, no_cuenta, sobregiro):
        super().__init__(no_cuenta)
        self.linea_de_sobregiro = sobregiro

class TarjetaDeCredito(CuentaBancaria):
    limite_de_credito = 0.0

    def __init__(self, no_cuenta, limite):
        super().__init__(no_cuenta)
        self.limite_de_credito = limite

tc1 = TarjetaDeCredito('370787113603009',100000)
cc1 = CuentaDeCheques('370787113603987',10000)
print(f"Numero de cuenta: {tc1.numero_de_cuenta}, Limite de Credito: {tc1.limite_de_credito}")
print(f"Numero de cuenta: {cc1.numero_de_cuenta}, Limite de Credito: {cc1.linea_de_sobregiro}")

