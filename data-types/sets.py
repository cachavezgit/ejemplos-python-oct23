conjunto1 = set()

conjunto1.add(1000)
conjunto1.add(2000)
conjunto1.add(3000)

print(type(conjunto1))
print(conjunto1)

conjunto1.add(2000)
conjunto1.add(1000)

print(conjunto1)

conjunto2 = {20,40,60,20,40,80,100}
print(type(conjunto2))
print(conjunto2)

nombres1={"Ana", "Hugo", "Ivan","Mau"}
nombres2={"Mariel", "Mau", "Ana"}
nombres1.add("Juan")
print(nombres1.intersection(nombres2))

todos_los_nombres = nombres1.union(nombres2)
print(sorted(todos_los_nombres))
todos_los_nombres.remove('Mariel')
for nombre in todos_los_nombres:
    print(nombre)

