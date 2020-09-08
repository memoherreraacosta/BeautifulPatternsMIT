# Patrones hermosos

"""
RESTAURANT
"""

edad = int(input('¿Qué edad tiene? '   ))

if (edad <= 10 and edad > 0):
    print("Menú infantil")
elif (edad > 10 and edad <=18):
    print("Postre gratis")
elif edad > 18:
    print("Promoción 2x1")
else:
    print("Por favor introduzca un número válido")
