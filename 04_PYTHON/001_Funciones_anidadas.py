# def f1(a): # Función que "encierra" a f2 (enclosing)
#     print(a)
#     def f2(x): # Función anidada
#         print(x) # Llamamos a f2 desde f1
#     b = 100
#     f2(b)

# f1 ('Python') # Llamamos a f1
# f2('5') # No puedo acceder a ella por que esta dentro de otra función

G = 'Esta variable es de ámbito Global'
def f1():
    E= 'Esta variable es local a f1. Enclosing a f2'
    def f2():
        # L = 'Esta variable es local a f2'
        L = 'L es local a f2'
        E = 'E también es local a f2'
        G = 'G también es local a f2'
        print(L, E, G, sep = '\n')
        # def f3():
        #     print(L)
        # f3()
    f2()
    # f3() 
f1()

# uso de variables con valores con defecto
# def concatena(x,y, sep=" "):
#     print(x + sep + y)

# concatena("hola", "mundo", sep="\n")
