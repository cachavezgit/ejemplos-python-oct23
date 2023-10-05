from random import randint

numero = int(input('numero:'))
print(numero)

value = randint(1,3)
print(value)

print(type(numero))
print(type(value))

if numero == value:
    print("Son iguales")
else:
    print("Son diferentes")