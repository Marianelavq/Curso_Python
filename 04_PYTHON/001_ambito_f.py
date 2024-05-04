a = 'Python' # Scope global (al módulo)
print('Valor fuera:', a)

def funcion():
    # global a
    a = 33
    print('Valor dentro' , a) #Scope local a la función 
    
funcion()
# a = "me la machaco"
print('Valor fuera', a)