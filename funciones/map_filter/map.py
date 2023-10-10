def eleva_al_cubo(num):
    return num**3

print(eleva_al_cubo(3))
lista_de_numeros = [2,3,4,5,6,7,8,9,10]

resultado = list(map(eleva_al_cubo, lista_de_numeros))

resultado2 = list(map(lambda gato: gato**3, lista_de_numeros))

print(resultado2)