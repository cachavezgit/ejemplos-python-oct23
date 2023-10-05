with open(r'C:\Users\cachavez\curso-python\extras\frutas.txt') as frutas_file:
    frutas = frutas_file.readlines()
    for fruta in frutas:
        print(fruta)