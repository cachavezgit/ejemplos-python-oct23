z = "mensaje"
lista = [1,2,3]

def cambia(x):
    print(x)
    x = "otra cosa"
    print(x)

def cambiamutable(x):
    print(x)
    #x = [1000,2000,3000]
    x[1] = 1000
    print(x)

cambia(z)
print(z)

cambiamutable(lista)
print(lista)

