dict1 = {'A':1,'B':2}
dict2 = dict(A=1,B=2)

dict2['A'] = 1000

print(type(dict1))
print(dict1)

print(type(dict2))
print(dict2)

if 'A' in dict2:
    print("si está la A")
else:
    print("no está")

texto="Esta cadena contiene varias palabras"
for palabra in texto.split():
    print(palabra)

