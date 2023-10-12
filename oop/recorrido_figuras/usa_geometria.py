import geometria

def esTriangulo(figura):
    return isinstance(figura, geometria.Triangulo)

cuad1 = geometria.Cuadrado()
cuad2 = geometria.Cuadrado()

circ1 = geometria.Circulo()

triang1 = geometria.Triangulo(10,5)
triang2 = geometria.Triangulo(10,8)
triang3 = geometria.Triangulo(10,12)
triang3.nombre = "Triangulo 3"

figuras = [cuad1, circ1, triang1, cuad2, triang2, triang3]

triangulos = list(filter(esTriangulo,figuras))
area_triangulo = [triangulo.calcula_area() for triangulo in triangulos]

print(area_triangulo)
print(triang3.nombre)
print(triang3.__class__.__name__)

              


                  


