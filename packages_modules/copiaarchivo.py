import argparse
from paquete3.utilerias import UtileriaArchivos

parser = argparse.ArgumentParser()
parser.add_argument("--folder")
parser.add_argument("--origen")
parser.add_argument("--nuevoarchivo")
argumentos = parser.parse_args()

UtileriaArchivos.copia_archivo(argumentos.folder, argumentos.nuevoarchivo,argumentos.origen)

