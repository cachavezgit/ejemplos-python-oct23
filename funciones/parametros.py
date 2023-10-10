def calculaArea(base=1, altura=1):
    return (base*altura)/2

print(calculaArea(10,5))
print(calculaArea(10))

triangulo=(8,4)
print(calculaArea(*triangulo))