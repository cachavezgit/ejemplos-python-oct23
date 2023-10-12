class Parent:
    color_de_cabello = 'negro'

class Child(Parent): #Child inherits from Parent
    pass

c = Child
print(c.color_de_cabello)