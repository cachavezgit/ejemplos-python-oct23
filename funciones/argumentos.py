from datetime import date

def imprime_datos(nombre, numero, fecha):
    print(f"Nombre: {nombre} - Numero: {numero} Fecha: {fecha}")

imprime_datos("Wilson", 1023, date.today()) # Posicional

imprime_datos(fecha=date.today(), nombre="Maria", numero=12.34) #Keyword

info_para_la_funcion = ("Maria", 123, date.today())
imprime_datos(*info_para_la_funcion) #Iterable unpacking *

diccionario_argumentos = {'nombre':'Wilson', 'numero':123,'fecha':date.today()}
imprime_datos(**diccionario_argumentos) #Dictionary unpacking **




