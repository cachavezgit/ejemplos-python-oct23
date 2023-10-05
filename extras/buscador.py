def busca_palabra_en_archivo(palabra, archivo):
    with open(archivo, 'r') as input_file:
        lineas = input_file.readlines()
        print(type(lineas))
        for linea in lineas:
            if linea.find(palabra)!=-1:
                print(f"La palabra {palabra} si esta en el archivo en la linea {lineas.index(linea)+1}")

palabra_a_buscar = input('Que palabra se busca: ')
busca_palabra_en_archivo(palabra_a_buscar,r'C:\Users\cachavez\curso-python\extras\carbohidratos.txt')
            