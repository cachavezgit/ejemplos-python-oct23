def cuatro_parametros(a, b, /, c, d):
    print(a,b,c,d)

cuatro_parametros(1,2,3,4)

cuatro_parametros(5,3, d=1000, c=2000)

#cuatro_parametros(b=1,a=2,d=3,c=4) #error por posicional only Python 3.8 en adelante