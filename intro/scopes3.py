def enclosing_func():
    m = 13

    def local():
        print(m, 'Imprimiendo desde el local scope')

    local()

m = 5
print(m, 'Imprimiendo desde el global scope')

enclosing_func()