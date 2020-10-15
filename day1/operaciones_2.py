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
print("Division y suma: " + str(n1 / n2 + n1))
print("Division y suma con paréntesis: " + str(n1 / (n2 + n1)))
