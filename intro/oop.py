class Empleado:

    def __init__(self, nombre, direccion):  #constructor
        self.nombre = nombre
        self.direccion = direccion

    def mensajeNombre(self):
        print(self.nombre)
        print(self.direccion)

empleado1 = Empleado('Ivan','Calle 13 #174')
empleado2 = Empleado('Maria','Calle 1 #17')

empleado1.mensajeNombre()
empleado2.mensajeNombre()


