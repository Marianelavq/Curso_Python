

#   LISTAS

"""
La lista es un tipo de colección ordenada y modificable. 
Es decir, una secuencia de valores de cualquier tipo, ordenados y de tamaño variable.
Se escriben entre corchetes. []
"""

miLista=["Angel", 43, 667767250] 
miLista2 = [22, True, "una lista", [1, 2]]

#   MÉTODOS DE LAS LISTAS

#   Hacer una lista de una cadena
miLista = list("PYTHON")
print(miLista)

#   Acceder a los elementos de una lista
miLista = [22, True, "una cadena", [1, 2]]
print(miLista[0])

miLista = [[1,2] , [3,4] , [5,6]]
miVar = miLista[1,1]
print(miVar)

#   Función con una lista como parámetro

def miFunccion(listaFrutas):
      for x in listaFrutas:
        print(x)

frutas = ["Manzana", "banana", "cereza"]

miFunccion(frutas)

# Podemos utilizar los operadores vistos en el tema anterior para comparar listas
lista2 = ['t2', 't1', 't3']
lista1 == lista2
# Out[17]: False

lista1 in lista2
# Out[20]: False

lista1 == ['t1', 't2', 't3']
# Out [18]: True

listal is ['t1', 't2', 't3']
# Out [19]: False

# Una cosa interesante es que una lista puede llegar a contener una función.

def func():
  print("Hola mundo")

func
# Out [24]: ‹function main .. func() >

lista = ["texto1", "texto2", func]
print(lista)

# ['texto1', 'texto2', ‹function func at 0x0000012D476D0EE0>]# 

# Los elementos de una lista no tienen que ser únicos. Puede repetirse el mismo elemento varias veces en la misma lista
lista = ["texto", "texto", "texto"]
print(lista)

# ['texto', 'texto', 'texto']