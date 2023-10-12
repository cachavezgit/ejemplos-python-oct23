import clases1

demo1=clases1.Demo()
print(type(demo1))

if isinstance(demo1,clases1.Demo):
    print("Es de tipo clases1.Demo")

coord1 = clases1.Coordenada(0,0)
coord1.x=10
coord1.y=20
coord1.z=30
print(coord1.x)
print(coord1.y)
print(coord1.z)

coord2 = clases1.Coordenada(100,200)
print(coord2.x)
print(coord2.y)
