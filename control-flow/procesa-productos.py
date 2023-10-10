from datetime import date, timedelta
from random import randint

def return_current_day():
    today = date.today()
    days_to_be_added = randint(0,6)
    new_date = today + timedelta(days=days_to_be_added) # today + 1 day is tomorrow
    return new_date.weekday()

def calcula_precio_descontado(precio, operation_day):
    if operation_day in [0,2,4]:
        nuevo_precio = float(precio) * 0.90
    elif operation_day in [1,3]:
        nuevo_precio = float(precio) * 0.85
    else:
        nuevo_precio = precio
    return nuevo_precio

operation_day=return_current_day()

with open('productos.txt', 'r') as input_file:
        lineas = input_file.readlines()
        for linea in lineas:
            producto, precio = linea.split(",")
            nuevo_precio = calcula_precio_descontado(precio, operation_day)

            print(f"Dia actual: {operation_day} Producto: {producto} Precio original: {precio} Precio descontado: {nuevo_precio}")