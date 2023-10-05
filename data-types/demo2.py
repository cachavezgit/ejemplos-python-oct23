class Persona:
    def __init__(self, edad): #constructor
        self.edad = edad

persona1 = Persona(45)
persona2 = Persona(30)

print(id(persona1))
print(id(persona2))

persona1.edad = 50
persona2.edad = 20

print(id(persona1))
print(id(persona2))

print(id(persona1.edad))
print(id(persona2.edad))