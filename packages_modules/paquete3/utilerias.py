import shutil
import os

class UtileriaArchivos:
    @staticmethod
    def copia_archivo(cualfolder,nombre_copia,original):
        print(f"Copiando el archivo {original} en el folder: {cualfolder} a partir de: {original}")

        try:
            os.chdir(f"c:\\users\\cachavez\\{cualfolder}")
            shutil.copyfile(original,nombre_copia)
        except FileNotFoundError:
            print("El folder no existe")
