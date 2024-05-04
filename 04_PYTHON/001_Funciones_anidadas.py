def f1(a): # Función que "encierra" a f2 (enclosing)
    print(a)
    def f2(x): # Función anidada
        print(x) # Llamamos a f2 desde f1
    b = 100
    f2(b)

f1 ('Python') # Llamamos a f1
# f2('5') # No puedo acceder a ella por que esta dentro de otra función