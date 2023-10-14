import random

def multiplica_al_azar(numero):
    if numero < 0:
        raise ValueError
    
    factor = random.randint(0,1000)
    
    import pdb;	pdb.set_trace() #breakpoint()

    return numero *factor

z = 8
print(multiplica_al_azar(z))