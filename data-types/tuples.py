demo_tupla = (10, 'abc', 3.56)

print(type(demo_tupla))
print(id(demo_tupla))

demo_tupla = (20, 'xyz', 8.56)
print(id(demo_tupla))

print(demo_tupla)

a, b, c = demo_tupla

print(b)

tupla_vacia = ()

num1, num2, num3, num4 = 10, 65, 78, 102

print(num2)

if 20 in demo_tupla:
    print("El 10 esta incluido...")

tupla_de_un_solo_elemento = (89,) # Si quiero que sea tupla debe llevar una coma al final si es un sólo elemento
print(type(tupla_de_un_solo_elemento))