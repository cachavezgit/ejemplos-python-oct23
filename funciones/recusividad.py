def factorial(n):
    if n in (0, 1): # base case
        return 1
    resultado = factorial(n - 1) * n # recursive case
    print(resultado)
    return resultado

resultado = factorial(5)
#print(resultado)