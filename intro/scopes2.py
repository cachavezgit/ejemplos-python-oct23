def local():
    print(m, 'Imprimiendo la variable desde el scope local')

m = 5
print(m, 'Imprimiendo la variable desde el scope global')

local()

