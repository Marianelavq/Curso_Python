# def suma(a, b): # Modificamos a y b en el scope de suma)
#     a = 3
#     b = 4
#     return a+b

# a, b = 5, 10
# print(suma(a, b))
# print(a, b) # a y b no han cambiado fuera de la función

# def minimo(l):
#     l[0] = 1000 # Modificamos la lista en el interior
#     return min(l)

# l = [1, 2, 3]
# print(l)
# print (minimo(l)) # Modifica la lista aqui
# print(l)

# Explicación de que unstring es inmutable
# nombre = ["T", "o", "m"]
# nombre = "Tom"
# print(nombre[0])
# nombre[0] = "N"

# def sumalos_todos(*args):
#     # print(args)
#     total = 0
#     for arg in args:
#         total = total + arg
#     print(total)

# sumalos_todos(5, 5, 20)

# t = (5, 5, 20)
# print(t)

# def f(**kargs):
#     print(kargs)
#     for key, value in kargs.items():
#         # print(key)
#         # print(value)
#         if key == "saludo":
#             print(value)
        

# def f(**kargs):
#     print(kargs)
# f()
# f(a=1)
# f(a=1, b=2)
# f(a=1, c=3, b=2, saludo='hola')

def f(a, b, c, d):
    print(a, b, c, d)

argumentos = {'b':20, 'a':1, 'c' :300, 'd': 4000}

f(**argumentos) # Desempaquetando diccionario argumentos con **

argumentos = {'b':200, 'c':300, 'd' :400}

f(10, **argumentos) # Podemos combinar argumentos posicionales con dict

