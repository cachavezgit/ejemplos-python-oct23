import sys
#import mod
import mod as modulo_funcional
#from mod import mensaje, lista, Gato, eleva_al_cuadrado
#from mod import mensaje, lista, Gato as Minimo, eleva_al_cuadrado
#from mod import *
#import paquete1.mod2
import paquete1
from paquete1.mod1 import Cuenta as CuentaBancaria
from paquete1.mod2 import Triangulo as Triang
from paquete2.sub_paquete2.mod5 import mayor_de_dos_numeros
#from ..oop.recorrido_figuras import triangulo

sys.path.append('C:\\Users\\cachavez\\demopath')
print(sys.path)
print(modulo_funcional.mensaje)

nueva=list(filter(lambda x:x>50,modulo_funcional.lista))
print(nueva)

mizifu = modulo_funcional.Gato()
print(mizifu.maullar("Miau"))

print(modulo_funcional.eleva_al_cuadrado(10))

triang1 = Triang(10,100)
print(triang1.calcula_area())

print(paquete1.lista_del_paquete)

from paquete1.mod1 import *

print(mayor_de_dos_numeros(6,2))
#print(dir()) # <--- nos deja visualizar cuáles elementos se han importado