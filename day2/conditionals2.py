"""

Conditionals programming exercises

Numero mas grande
"""

"""
If statements

if, else, elif, continue, break
"""

x = int(input("Escoge un numero 'x': "))
y = int(input("Escoge un numero 'y': "))

if x > y:
    print("El numero x: {0} es mayor".format(x))
elif x < y:
    print("El numero y: {0} es mayor".format(y))
else:
    print("Ambos numeros 'x' y 'y' son iguales: {0}".format(y))
