def retorna_varios_elementos():
    return 'Carlos Ivan', 'Hermosillo', '83293'

elemento1, elemento2 = 1000, 2000

print(elemento1)
print(elemento2)

tempo = elemento1
elemento1 = elemento2
elemento2 = tempo

print(elemento1)
print(elemento2)

elemento1, elemento2 = elemento2, elemento1

print(elemento1)
print(elemento2)

nombre, ciudad, cp = retorna_varios_elementos()
print(nombre)
print(ciudad)
print(cp)
