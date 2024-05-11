# Para crear una nueva lista 

thislist = list(("Manzana", "plátano", "cereza"))
print (thislist)

# Operaciones con listas: Las listas soportan muchos de los operadores y funciones de Python por defecto. 

In [50]:lista1 = [1, 2, 3]
        lista2 = [4, 5, 6]

In [51]:lista1 + lista2
out [51]: [1, 2, 3, 4, 5, 6]

In [53]: lista1 * 2
Out [53]: [1, 2, 3, 1, 2, 3]

In [52]: len(lista1)
Out [52]: 3

In [54]: min(lista1)
Out [54]: 1

In [55]: max(lista2)
Out [55]: 6
In [55]: [1, 2, 3] + 4

# TypeError Traceback (most recent call last)
# cipython-input-95-5842ff442cc5› in ‹module ›
# ..> 1 [1, 2, 3] + 4
# TypeError: can only concatenate list (not "int*) to list 

In [96]: [1, 2, 3] + [4]
Out [96]: [1, 2, 3, 4]