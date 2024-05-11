# Una lista puede contener cualquier tipo de objeto. Esto incluye otra lista.
# Una lista puede contener sublistas, que a su vez pueden contener sublistas, y así hasta una profundidad arbitraria.

thislist = [["a1", "a2", "a3"],
            ["b1", "b2", "b3"],
            ["c1","C2","c3"]]

print(thislist)

# Las listas soportan anidamiento arbitrario. Esto significa que podemos crear combinaciones anidadas de listas (listas dentro de listas) tan profundas como necesitemos. Es decir, una lista formada por listas. Esta característica puede utilizarse para crear matrices.

# El indexado es igual que en una lista plana, pero ahora podemos anexar más índices para seleccionar elementos individuales.

thislist = [["a1", "a2", "a3"],
            ["b1", "b2", "b3"],
            ["c1","C2","c3"]]

thislist[1:] # Indexamos La segundo fila

thislist = [["a1", "a2", "a3"],
            ["b1", "b2", "b3"],
            ["c1","C2","c3"]]

thislist[0][-1] # Indexamos la segunda y tercera fila

# Estas operaciones sirven para matrices pequeñas y operaciones sencillas.

# Sin embargo, si queremos operar con matrices grandes o en problemas complejos, Python dispone de librerías para este tipo de usos. El principal ejemplo es Numpy, un proyecto de código abierto con gran respaldo de la comunidad científica y de numerosas organizaciones privadas. El proyecto Numpy es uno de los principales responsables del tremendo éxito de Python en el campo de Data Science.

# Además de crear matrices, el anidamiento de listas nos permite crear anidamientos no homogéneos:

thislist = [["a1", "a2", "a3"],
            ["b1", "b2"],
            ["c1","C2","c3","c4","C5","c6"]]

print(thislist)

# Para acceder a los elementos de una sublista utilizamos la sintaxis [][]

thislist[1][0]
print(thislist[1][0])
# Out[59]: 2
thislist[1][1]
# Out[60]: [3, 4]
thislist[1][1][0]
# Out[61]: 3

# No hay límite en la cantidad de listas que podemos anidar, pueden ser tantas como soporte la memoria de nuestro sistema.

# Es importante entender que los operadores aplicarán sobre la primera lista y no aplicarán de manera recursiva.

thislist
# Out [62]: [1, [2, [3, 4], 5], 6]
[3, 4] in thislist
# Out[63]: False
thislist[1]
# Out[64]: [2, [3, 4], 5]
[3, 4] in thislist[1]
# Out[65]: True

