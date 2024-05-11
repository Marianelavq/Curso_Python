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

co12 = [row[1] for row in matrix] # Esta expresion se lee: deme row 1 para cada row en m y se obtiene la segunda columna
print(co12)                       # Esta expresión recorre la matriz m fila a fila, guardando cada fila en la variable row y, en cada iteración, obtiene el segundo elemento de la fila

# ['a2', 'b2', 'c2']

# m no se ha modificado
[['a1', 'a2', 'a3'], ['b1', 'b2', 'b3'], ['c1', 'c2', 'c3']]

# 

[matrix[i][i] for i in [0, 1, 2]] # Extrae la diagonal de la matriz

# ['a1', 'b2', 'c3']

# Extraemos las longitudes de los elementos de n1

[len(row) for row in matrix] # Pueden haber expresiones dentro
# [3, 2, 6]

[len(row) for row in matrix if len(row) > 2] # Filtramos elementos
# [3, 6]

squares = [n ** 2 for n in range(10)] # Más expresiones dentro
# squares [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Cómo copiar listas

la = [1, 2, 3]
lb = la[:] # Copiamos la lista
lc = list(la) # otra manera de hacer una copia
la[2] = 'z'

print (la) # hemos modificado ''la''
# [1, 2, 'z']

print (lb) # pero no "'1b''
# [1, 2, 3]

print(lc) # ni ''1c''
# [1, 2, 3]

# Aislar una variable de cambios externos 

import copy                 # importamos modulo copy
la = [1, 2, [31, 32, 33]]   # Lista anidada
lb = copy.copy(la)         # Copia 'plana' (igual que 1b = la[:]) 'plana'
lc = copy.deepcopy(la)      # Copia profunda. Por si hay elementos anidados
la[1] = 'z'
la[2][2] = 'zz'

print (la)
# [1,'z', [31, 32,'zz']]

print(lb)                   # Copia plana solo copia elementos de el nivel
# [1, 2, [31, 32, 'zz']]

print(lc)                   # Copia profunda copia a todos los niveles
# [1, 2, [31, 32, 33]]

