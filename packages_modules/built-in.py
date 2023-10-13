import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--usuario")
parser.add_argument("--password")
argumentos = parser.parse_args()

print(f"El nombre del usuario es: {argumentos.usuario} y el password es {argumentos.password}")

def matematica(num):
    resultado = num / 2

try:
    os.chdir("c:\\users\\cachavez")
    os.mkdir("python1")
    print("Se creo exitosamente")
    z = matematica(5)
except ZeroDivisionError:
    print("Posible division entre cero")
except FileExistsError:
    print("El directorio python1 ya ha sido creado...")
else:
    print("No se disparo alguna exception")

