def busca_multiples_palabra_en_archivo(*palabras):
    archivo = "divinacomedia.txt"

    with open(archivo, 'r') as input_file:
        lineas = input_file.readlines()
        for linea in lineas:
            for palabra in palabras:
                veces = linea.count(palabra)
                if veces > 0:
                    print(f"La palabra '{palabra}' aparece {veces} veces en la linea {lineas.index(linea)+1}")

busca_multiples_palabra_en_archivo("the", "I", "sea", "swift")

