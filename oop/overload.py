# No hay overloading en Python, se ignoran todas, si es que las hay, menos la última
class Persona:
    nombre = ''
    apellido = ''
    def __init__():
        nombre = "No definido"
        apellido = "No definido"

    def __init__(self,n,a):
        self.nombre = n
        self.apellido = a

    def devuelveNumero(self):
        print(8)
    
    def devuelveNumero(self,x):
        print(x)
    
persona1 = Persona('wilson', 'perez')
#persona2 = Persona()
persona1.devuelveNumero()
print(f"Nombre: {persona1.nombre}, Apellido: {persona1.apellido}")
#print(f"Nombre: {persona2.nombre}, Apellido: {persona2.apellido}")
