from math import prod
lista = []
lista.append("Ivan")
lista.append("Maria")
lista.append(56)

lista = list("Parangaricutirimicuaro")
lista.pop(2)
lista.remove('i')
print(lista)
print(type(lista))

lista = [10,20,30,40,50]
print(id(lista))
lista = [1,2,3,4,5]
print(id(lista))

numeros = [9,8,2]
print(prod(numeros))
print(numeros)
print(sorted(numeros))

lista_combinada = [(2,3),(9,8),(1,3),(7,5),(1,9),(9,1)]
print(lista_combinada)
print(min(lista_combinada))
print(max(lista_combinada))
print(sorted(lista_combinada))
