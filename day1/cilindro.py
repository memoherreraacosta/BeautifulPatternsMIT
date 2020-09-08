# Patrones hermosos
import math

"""
CILINDRO
"""

altura = float(input('Altura: '   ))
diam = float(input('Diametro: '   ))
res = altura * math.pi * math.pow(diam/2, 2)

print("El volumen del cilindro de  " + str(diam) + "de diametro y " + str(altura) + " de altura es de " + str(res))
