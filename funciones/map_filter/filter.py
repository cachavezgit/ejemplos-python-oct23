def es_numero_primo(num):
    if num < 2: #si es menor de 2 no es primo, devolverá Falso
        return False
    for i in range(2, num): #un ciclo desde el 2 hasta el num de entrada
        if num % i == 0: #si el resto da 0 no es primo, devuelve Falso
            return False
    return True #de lo contrario devuelve Verdadero
print(es_numero_primo(5))

lista_de_numeros = [1,5,8,9,11,14,18,23]

lista_de_numeros2 = [n*2 for n in lista_de_numeros]

solo_numeros_primos = list(filter(es_numero_primo,lista_de_numeros))
print(solo_numeros_primos)

solo_numeros_menores_de_10 = set(filter(lambda num: num<10, lista_de_numeros2))
print(solo_numeros_menores_de_10)



