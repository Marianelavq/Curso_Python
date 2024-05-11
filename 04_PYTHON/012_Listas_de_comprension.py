# Listas de comprensión: Permiten crear listas a partir de unos valores que tenemos almacenados

# Una lista por comprensión es una expresión con una notación particular que genera una lista

miLista=[1,2,3,4,5,6,7]
print(miLista)

# milista2 tiene los valores (2*elemento) siendo elemento los valores de la l
miLista2 = [2*elemento for elemento in miLista]
print(miLista2)

# Crear una Lista solo con los elementos pares
listaPares = [elemento for elemento in miLista if elemento%2==0]
print(listaPares)

# A La manera tradicional seria:
listaPares=[]
for i in miLista:
    if i%2==0:
        listaPares.append(i)
print(listaPares)

# Anidar iteraciones dentro de la liata
a=["a","b","C"]
b=[1,2,3]

# Para cada elemento de a me recorre todos los elmentos de b
c=[elemento1*elemento2 for elemento1 in a for elemento2 in b]
print(c)

# Puedo incluso poner alguna condicion
c=[elemento1*elemento2 for elemento1 in a for elemento2 in b if elemento2!=2]
print(c)

# 
matrix = [
    ['a1', 'a2', 'a3'], 
    ['b1', 'b2', 'b3'], 
    ['c1', 'c2', 'c3']
    ]

col_tom = []
for row in matrix:
    col_tom.append(row[1])
print(col_tom)

# Arriba y abajo son el mismo algoritmo solo que el de abajo es mas resumido, es una lista de comprensión 

co12 = [row[1] for row in matrix] # Obtiene la segunda columna
print(co12)
# ['a2', 'b2', 'c2']

# m no se ha modificado
[['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3']]



