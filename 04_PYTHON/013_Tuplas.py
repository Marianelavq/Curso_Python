


#   TUPLAS

"""Una tupla es una colección ordenada e inmutable. 
En Python, las tuplas se escriben entre paréntesis.
"""

#       Declaración de una tupla

miTupla = ("manzana", "banana", "cereza")
print(miTupla[1])

#   Otra forma de declararla

miTupla = tuple(("manzana", "banana", "cereza"))
print(miTupla)


#   Indexación Negativa

miTupla = ("manzana", "banana", "cereza")
print(miTupla[-1])

#   Rango de índices
#   Devuelve el tercer, cuarto y quinto elemento:

miTupla = ("manzana", "banana", "cereza", "naranja", "kiwi", "melon", "mango")
print(miTupla[2:5])

#   Convierta la tupla en una lista para poder cambiarla:

miTupla = ("manzana", "banana", "cereza")
miLista = list(miTupla)
miLista[1] = "kiwi"
miTupla = tuple(miLista)

print(miTupla)

#   Recorrer una tupla

miTupla = ("manzana", "banana", "cereza")
for x in miTupla:
  print(x)

#   Comprobar si existe un elemento
#   Compruebe si "manzana" está presente en la tupla:

miTupla = ("manzana", "banana", "cereza")
if "manzana" in miTupla:
  print("Sí, 'manzana' está en la tupla.")

#   Otra forma, simplemente con un boolean

print("manzana" in miTupla) 

#   Longitud de la tupla

miTupla = ("manzana", "banana", "cereza")
print(len(miTupla))


# Unir dos tuplas

tupla1 = ("a", "b" , "c")
tupla2 = (1, 2, 3)

tupla3 = tupla1 + tupla2
print(tupla3)

#   Cuantas veces se encuentra el elemento 4 en miTupla?

miTupla = ("manzana", "banana", "cereza" , "manzana")
print(miTupla.count("manzana"))	

#   Desempaquetdo de tupla

miTupla=("Angel", 4, 5.345, True, 4)
nombre, num1, num2, valor1, num3=miTupla

print(nombre)
print(num1)
print(num2)
print(valor1)
print(num3)

# Si definimos una tupla con un único elemento de tipo númerico debemos tener cuidado
# Python puede interpretar los paréntesis como parte de la expresión matemática y definir un tipo numérico, en lugar de una tupla

tupla = (2)
print(tupla)
# 2

print(type(tupla))
# int

# efectivamente me lo esta reconociendo como una operación y no como una tupla

# Para solucionarlo utilizamos la sintaxis (num,)

tupla = (2,)
print(tupla)
# (2,)

print(type(tupla))
# tuple

# Un tupla con varios elementos puede asignarse a una única variable

tupla = (1, 2, 3, 4)

# Una tupla permite asignar su contenido a varias variables simultaneamente

tupla = (num1, num2, num3)

Var1=num1
# 2

Var2=num2
# 3

Var3=num3
# 4

# El numero de varables debe concidir con el numero de elementos de la tupla
# numl, num2, num3 = tupla

# ValueError Traceback (most recent call last)
# ‹ipython-input-22-da3d6962b821> in ‹module›
# ---› 1 num1, num2, num3 = tupla

# ValueError: too many values to unpack (expected 3)

 # Este mecanismo de desempaquetado 

def func():
  return (5,6) # Los parentesis no son necesarios para indicar que es una tupla en el return

func ()
#(5, 6)

num1, num2 = func()
print(num1)
# 5

print(num2)
# 6

