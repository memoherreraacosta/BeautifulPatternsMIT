#Funcion para calcular el volumen de una esfera dado su radio
import math
def calcular_volumen_esfera(r):
    volumen = (math.pi - 4/3) * r**3
    # Opcion 1. Se imprime el resultado desde la funcion (Comentar la opcion que no se va a usar)
    print("%.2f" % volumen)
    #Opcion 2. Se retorna el valor, se tiene que imprimir desde la llamada a la funcion
    return volumen


#Llamada para probar la funcion
calcular_volumen_esfera(float(input("Ingresa el radio de la esfera")))

