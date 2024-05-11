# DEL: La palabra clave del elimina el índice especificado en una posición.

thislist = ["Manzana", "plátano", "cereza"]
del thislist[0]
print (thislist)

# también puede eliminar la lista por completo:

thislist = ["Manzana", "plátano", "cereza"]
del thislist

# El método clear) vacía la lista:

thislist = ["Manzana", "plátano", "cereza"]
thislist.clear()
print(thislist)

# Podemos utilizar otros conceptos de indexación, como el slicing o el stride para modificar varios elementos de una lista

lista = ['texto2', 'texto3']
# Out[82]: ['texto2', 'texto3']

# lista = lista + ["texto4", "texto5", "texto6"]
lista += ["texto4", "texto5", "texto6"]

# Out[84]: ['texto2', 'texto3', 'texto4', 'texto5', 'texto6']

lista[0:3]
# Out[85]: ['texto2', 'texto3', 'texto4']

lista[0:3] = [1, 2, 3]

# Out[87]: [1, 2, 3, 'texto5', 'texto6']

# El número de elementos seleccionados no tiene que ser igual a los asignados

lista[0:3]
# Out[88]: [1, 2, 3]

lista[0:3] = [1, 2]
# Out [90]: [1, 2, 'texto5', 'texto6']

lista[2:2] = [3, 4, 5]
# Out[92]: [1, 2, 3, 4, 5, 'textos', 'texto6']

lista[0:6] = []
# Out[94]: ['texto6']