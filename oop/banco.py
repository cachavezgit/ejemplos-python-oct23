class Cuenta:
    numero_de_cuenta=''

class Tarjeta(Cuenta):
    _limite_de_credito = 0

    def __init__(self,limite):
        self._limite_de_credito = limite

    @property
    def limite_de_credito(self):
        return self._limite_de_credito
    
    @limite_de_credito.setter
    def limite_de_credito(self,limite):
        if limite < 0:
            raise ValueError('Limite de crédito debe de ser positivo')
        self._limite_de_credito = limite

class Chequera(Cuenta):
    _linea_de_sobregiro = 0

    def __init__(self,linea):
        self._linea_de_sobregiro = linea

    @property
    def limite_de_sobregiro(self):
        return self._linea_de_sobregiro
    
tc1 = Tarjeta(1000)
print(tc1.limite_de_credito)
tc1.limite_de_credito = 2000
print(tc1.limite_de_credito)
cc1 = Chequera(5000)