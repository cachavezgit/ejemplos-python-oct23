from mysql.connector import connect, Error
import json

def conectar_mysql():
    conexion_mysql = None

    try:
        conexion_mysql = connect(
            host="24.199.90.148",
            user="wilson",
            password="password",
            database="world"
        )
    except Error as e:
        print(e)

    return conexion_mysql

def ciudades_del_pais(cualpais):
    conexion_mysql = conectar_mysql()
    lista_ciudades = []
    if conexion_mysql is not None:
        try:
            cursor = conexion_mysql.cursor()
            query = f"Select Code from country where Name='{cualpais}'"
            cursor.execute(query)
            info_pais = cursor.fetchone()
            if info_pais is not None:
                codigo_pais = info_pais[0]
                queryCiudades= f"Select * from city where countrycode='{codigo_pais}'"
                cursorciudades = conexion_mysql.cursor()
                cursorciudades.execute(queryCiudades)
                resultado = cursorciudades.fetchall()
                for ciudad in resultado:
                    lista_ciudades.append(ciudad)
            return lista_ciudades
        except Error as e:
            print(e)


def consulta_info_pais(cualpais):
    conexion_mysql = conectar_mysql()

    if conexion_mysql is not None:
        try:
            cursor = conexion_mysql.cursor()
            query = f"Select Continent, Population, LifeExpectancy from country where Name='{cualpais}'"
            cursor.execute(query)
            info_pais = cursor.fetchone()
            if info_pais:
                return {
                    'continente':info_pais[0],
                    'poblacion':info_pais[1],
                    'expectativa':info_pais[2],
                }
            else:
                return None
        except Error as e:
            print(e)



