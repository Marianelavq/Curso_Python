# Indexing

lista = ["text1", "text2", "text3", "text4", "text5"]

lista[0]
print(lista[0])
# 'text1'

lista[-1]
print(lista[-1])
# 'text5'

# Slicing

lista[2:4]
# ['text3', 'text4']

lista[:3]
# ['text1', 'text2', 'text3']

lista[2:]
# ['text3', 'text4', 'text5']

# Stride

lista[0:4:2]
# ['text1', 'text3']

# Mediante el concepto de stride se puede dar la vuelta a una lista

lista
# ['text1', 'text2', 'text3', 'text4', 'text5']

lista[:: -1]
# ['text5', 'text4', 'text3', 'text2', 'text1']

texto = "Hola mundo"

texto[:] # Simbolo es la diferente entre los string y las listas 
# 'Hola mundo'

texto[:] is texto
# True

lista = [1, 2, 3, 4]

lista[:]
# [1, 2, 3, 4]

lista[:] is lista
False

