from enum import Enum

class EstadosProceso(Enum):
    APAGADO = 0
    ENCENDIDO = 2
    PAUSADO = 4

estado = EstadosProceso.ENCENDIDO
if estado == EstadosProceso.APAGADO:
    print("Apagado")
else:
    print("Encendido")
