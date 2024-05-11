# Unir dos listas o concatenar: 
# 1.- Usando el operador +

list1 = ["a","b","c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print (list3)

# Agregando todos los elementos de list2 a listi, uno por uno

list1 = ["a","b","c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print (list1)

# Método extend(), propósito es agregar elementos de una lista a otra lista

list1 = ["a","b","c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)