with open(r'C:\Users\cachavez\curso-python\data-types\texto-con-repetidas.txt') as archivo:
    lineas = archivo.readlines()
    info_palabras = {}

    for linea in lineas:
        palabras_encontradas = linea.split()
        for palabra in palabras_encontradas:
            if palabra in info_palabras:
                info_palabras[palabra] += 1
            else:
                info_palabras[palabra] = 1

    #info_palabras = {k:v for k,v in info_palabras.items() if v>1}

    for k, v in list(info_palabras.items()):
        if v <= 1:
            del info_palabras[k]

    
    print(info_palabras)