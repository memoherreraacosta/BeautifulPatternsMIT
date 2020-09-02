# Patrones hermosos
import math

"""
OPERACIONES 2
"""

print("Ingresa un número con decimal: ")
n1 = float(input())
print("Ahora un número entero: ")
n2 = int(input())

print("Resultados: ")

print ("Potencia: " + str(n1 ** n2))
print ("Division enteros: " + str(int(n2 // n1)))
print ("Módulo residuo: " + str(n2 % n1))
print("Division y suma: " + str(n1 * n2 + n1))
print("Division y suma con paréntesis: " + str(n1 * (n2 + n1)))

"""
Extra: utiliza la librería de Math
"""
print("\nPotencia pero cool: " + str(math.pow(n1, n2)))
print("Primer número multiplicado por pi: " + str(n1 * math.pi))
print("Raiz cuadrada: " + str(math.sqrt(n2)))
print("Ceil: " + str(math.ceil(n1)))
print("Floor: " + str(math.floor(n1)))
