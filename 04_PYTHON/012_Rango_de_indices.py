# Rango de indices. Ej Crear una lista de elementos y devolver el segundo, tercer y cuarto elemento.

thislist = ["Manzana", "plátano", "cereza", "naranja", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Nota: La búsqueda comenzará en el índice 2 (incluido) y finalizará en el índice 5 (no incluido). Recordemos que el primer elemento tiene el índice 0.

# Rango de indices negativos

thislist = ["Manzana", "plátano", "cereza", "naranja", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Este ejemplo devuelve los elementos del índice -4 (incluido) al índice -1 (excluido)

# Cambiar valor del elemento

thislist = ["Manzana", "plátano", "cereza"]
thislist[1] = "Pera"
print(thislist)

# Cambiar el segundo elemento

# Recorrer una lista

thislist = ["Manzana", "plátano", "cereza"]
for x in thislist:
   print (x)

# Imprima todos los elementos de la lista, uno por uno

# Comprobar si el elemento existe

thislist = ["Manzana", "plátano", "cereza"]
if "Manzana" in thislist:
  print("Sí, 'Manzana' se encuentra en la lista.")

# Compruebe si "manzana" está presente en la lista

# Longitud de la lista: Para determinar cuántos elementos tiene una lista, use el método lenO :

thislist = ["Manzana", "plátano", "cereza"]
print (len(thislist))

# Imprima el número de elementos en la lista

# Copiar una lista: 

# 1.- usar el método de lista incorporado copy()

thislist = ["Manzana", "plátano", "cereza"]
mylist = thislist. copy()
print(mylist)

# 2.- usar la listO métodos incorporada listO

thislist = ["Manzana", "plátano", "cereza"]
mylist = list(thislist)
print(mylist)