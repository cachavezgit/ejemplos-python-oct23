def local():    # def define una funcion
    m = 7   # local scope
    print(m)

m = 5  # global scope

local()

print(m)
