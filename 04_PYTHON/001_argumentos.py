# def suma(a, b): # Modificamos a y b en el scope de suma)
#     a = 3
#     b = 4
#     return a+b

# a, b = 5, 10
# print(suma(a, b))
# print(a, b) # a y b no han cambiado fuera de la función

def minimo(l):
    l[0] = 1000 # Modificamos la lista en el interior
    return min(l)

l = [1, 2, 3]
print(l)
print (minimo(l)) # Modifica la lista aqui
print(l)

# Explicación de que unstring es inmutable
# nombre = ["T", "o", "m"]
# nombre = "Tom"
# print(nombre[0])
# nombre[0] = "N"