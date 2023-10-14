"""
" En este modulo se devuelve la informacion de un pais:
" continente, poblacion, expectativa de vida
"""
import argparse
from conexion_mysql import consulta_info_pais, ciudades_del_pais

parser = argparse.ArgumentParser()
parser.add_argument("--pais")
argumentos = parser.parse_args()

pais_solicitado = argumentos.pais

json_result = consulta_info_pais(pais_solicitado)
if json_result:
    print(json_result)
else:
    print(f"No hay informacion del pais: {pais_solicitado}")

ciudades = ciudades_del_pais(pais_solicitado)
print(ciudades)
