# Como las listas son colecciones mutables, muchos de los métodos de éstas la modifican in-place en lugar de crear una lista nueva, como por ejemplo sort o reverse.

miLista=["Angel", "Maria", "Manolo", "Antonio", "Pepe"]
miLista2=["nombre", 2, 5.56, True] # Se pueden mezclar diferentes elementos.

print(miLista[1]) # Para un eLemento en concreto, se empieza a contar desde la posición cero.
print(miLista[0:2]) # Empezando desde cero incluido hasta el dos sin incluir, esto es, "Angel y María".

# Si escribimos tres números (inicio:fin:salto) en lugar de dos, el tercero se utiliza para determi nar cada cuantas posiciones añadir un elemento a la lista, Ejemplo

l = [99, True, "una lista", [1, 2]]

mi_var = l[0:2] # mi_ var vale [99, True]

mi_var = l[0:4:2] # mi_var vale [99, "una lista"]

print(l[:2]) # Como en el ejemplo anterior, pero en el caso de que sea cero, si no pongo se sobreentiende.

print(l[1:3]) #Desde el elemento [1] incluido, hasta el tres sin incluir, es decir "María y Manolo".

print(l[2:]) # Desde el elemento [2] hasta el final, es decir "Manolo, Antonio, Pepe".

print(l[-2]) # Desde el final, la segunda posición, es decir "Antonio".

print(l[:]) # Lista completa.

# ________________________________________________________

miLista.append("Antonio") # Añade el elemento al final de la Lista.

miLista. insert(2, "Sandra") # Añade el elemento en la posición [2].

miLista.extend(["Sara", "Diego"]) # Concatena la nueva lista a la anterior.

print(miLista.index("Antonio")) # Me dice en qué posición está "Antonio", en este caso 3, si hay más elementos "Antonio", nos da el primero.

print("pepe" in miLista) # Está este elemento en la Lista?. Imprime true o false.

miLista.remove("Angel") # ELimina un elemento de la lista, NO LO DEVUELVE.

miLista.pop() # ELimina el último elemento de una lista Y LO DEVUELVE.

# ______________________________________________________

# Puedo crear una lista concatenando los elementos de otras listas:

miLista3=miLista+miLista2 # Crea una Lista nueva que es el resultado de concatenar Las dos anteriores.
miLista4=[4, 6, 7]*2 # Me crearía una Lista como esta [4, 6, 7, 4, 6, 7]

print(miLista[:])
print(miLista2[:])
print(miLista3[:])
print(miLista4[:])

Lista5=[l, miLista2]

lista3=[2,5, 32,8,45,3,1] # Para ordenar listas
lista3.sort()

lista3.reverse() # Para ordenar listas en orden contrario o reverso