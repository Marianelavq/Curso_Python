# Para crear una nueva lista 

thislist = list(["Manzana", "plátano", "cereza"])
print (thislist)

# Operaciones con listas: Las listas soportan muchos de los operadores y funciones de Python por defecto. 

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista1 + lista2
print(lista1 + lista2)
# out [51]: [1, 2, 3, 4, 5, 6]

lista1 * 2
print(lista1*2)
# Out [53]: [1, 2, 3, 1, 2, 3]


len(lista1)
print(len(lista1))
# Out [52]: 3

min(lista1)
print(min(lista1))
# Out [54]: 1

max(lista2)
print(max(lista2))
# Out [55]: 6
# [1, 2, 3] + 4

# TypeError Traceback (most recent call last)
# cipython-input-95-5842ff442cc5› in ‹module ›
# ..> 1 [1, 2, 3] + 4
# TypeError: can only concatenate list (not "int*) to list 

# [1, 2, 3] + [4]
# Out [96]: [1, 2, 3, 4]