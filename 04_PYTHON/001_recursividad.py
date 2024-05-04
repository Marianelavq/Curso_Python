def factorial(x):
    if x>1:
        print("x: ", x) # muestra el valor de x en ese momento
        resultado_interno = x * factorial(x-1)
        print("resultado_interno: ", resultado_interno)
        return resultado_interno
    else:
        print(x)
        return 1

resultado = factorial(4)
print(resultado)
