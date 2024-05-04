print('Hello World! nela')

# Sintaxis básica de una función en Python

def suma(a, b): # Definimos la función "suma". Tiene 2 parámetros.
    return a+b # "return" devuelve el resultado de la función.

suma(2, 3) # Llamada a la función. Hay que pasarle dos parámetros.

# Resultado: 5

def en_pantalla(frase1, frase2):
    print(frase1, frase2) # "return" no es obligatorio

en_pantalla('Me gusta', 'Python')

# Resultado: Me gusta Python

def suma(a, b): # Definimos la función "suma". Tiene 2 parámetros.
    return a+b # "return" devuelve el resultado de la función.

x = suma(2, 3)
print (x) # Guardamos el resultado en x

# -------------------------------------

# Funciones y polimorfismo

def suma(a, b): # Definimos la función "suma". Tiene 2 parámetros.
    return a+b # "return" devuelve el resultado de la función.

suma (2, 3) # Función con ints
# Resultado = 5

suma (2.7, 4.0) # Función con floats
# Resultado = 6.7

suma('Me gusta', 'Python') # Función con strings

# -------------------------------------

# Funciones anidadas

def f1(a): # Función que "encierra" a f2 (enclosing)
    print(a)
    b = 100
    def f2(x): # Función anidada
        print (x) # Llamamos a f2 desde f1
    f2 (b)

f1 ( 'Python') # Llamamos a f1

# -------------------------------------

# Recursividad
# función que calcula el factorial de un número (recordemos que el factorial de x es igual a x * (x-1) * (x-2) * … * 1

def factorial(x):
    if x>1:
        return x*factorial (x-1)
    else:
        return 1
factorial(5)

# la condición de salida de la recursividad se cumple cuando x es igual a 1.
# -------------------------------------

# Devolviendo múltiples valores simultáneamente

def maxmin(lista):
    return max(lista), min(lista) # Devielveuna tupla de 2 elementos

l = [1, 3, 5, 6, 0]
maximo, minimo = maxmin (l) # Desempaqueta la tupla en 2 variables

print(minimo, maximo, sep= ' ')

# -------------------------------------

# Realiza una función que realice la descomposición en factores de un número. Deberá devolver una lista con los factores de dicho número.

def descomponer_en_factores(numero):
    # Inicializamos una lista vacía para almacenar los factores
    factores = []
    
    # Empezamos desde 2, ya que 1 es un factor de cualquier número
    divisor = 2
    
    # Mientras el número sea mayor que 1, seguimos buscando factores
    while numero > 1:
        # Si el número es divisible por el divisor actual, es un factor
        while numero % divisor == 0:
            # Añadimos el divisor a la lista de factores
            factores.append(divisor)
            # Dividimos el número por el divisor para encontrar los siguientes factores
            numero //= divisor
        # Incrementamos el divisor para buscar el siguiente factor
        divisor += 1
    
    # Devolvemos la lista de factores una vez que el número se ha descompuesto completamente
    return factores

# Ejemplo de uso

numero = 100

print(f"Los factores de {numero} son: {descomponer_en_factores(numero)}")

# -------------------------------------

# Ámbito de una función

a = 'Python' #Scope global (al módulo)

print('Valor fuera:', a)

def funcion():
    a=33
    print('Valor dentro', a) #Scope local a la función

funcion()

print('Valor fuera', a)

# -------------------------------------

# Resolución de nombres. La regla LEGB

G = 'Esta variable es de ámbito Global'
def f1():
    E='Esta variable es local a f1. Enclosing a f2'
    def f2():
        L = 'Esta variable es local a f2'
        print(L, E, G, sep = '\n')
        f2()
f1()

# -------------------------------------

# Parámetros y argumentos

def suma(a, b):
    return a+b

suma(2, 3)

suma(40, 30)


# -------------------------------------

#

# -------------------------------------

a = "modulo"