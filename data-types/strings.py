mensaje1 = "El siguiente texto 'abc' está entrecomillado"
mensaje2 = 'El siguiente texto "abc" está entrecomillado'

#mensaje1 = 10

print(mensaje1.removeprefix('El '))
print(mensaje1.removesuffix('ado'))
print(len(mensaje1))
print(len(mensaje2))

print(mensaje1)
print(mensaje2)

trabalenguas = "Parangaricutirimicuaro"

print(trabalenguas[:7])
print(trabalenguas[7:])
print('----------')
for i in range(len(trabalenguas)):
    print(trabalenguas[i])
