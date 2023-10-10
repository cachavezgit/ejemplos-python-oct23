from datetime import date

def multiples_retornos():
    return 'Test', 45.56, date.today()

a,b,c = multiples_retornos()

print(a)
print(b)
print(c)