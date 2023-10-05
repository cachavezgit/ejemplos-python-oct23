def elementos_comunes(list1, list2):
    resultado = []
    for elemento in list1:
        if elemento in list2:
            resultado.append(elemento)
    return resultado, len(resultado)

def elementos_comunes_simplificado(list1,list2):
    resultado = [elemento for elemento in list1 if elemento in list2]
    return resultado, len(resultado)

lista1 = [10,20,30,40,50,60]
lista2 = [20,90,60]

print(elementos_comunes(lista1,lista2))
print(elementos_comunes_simplificado(lista1,lista2))