"""
Conditionals programming exercises
For loop
"""

x = int(input("Escoge un numero positivo 'x': "))
y = int(input("Escoge un numero positivo 'y' que sera el tope de la iteracion: "))

print("La serie del 0 al '{0}' con saltos '{1}' es: ".format(y, x))
for number in range(0, y):
    if number % x == 0:
        print("El numero '{0}' es multiplo de '{1}'".format(number, x))
    else:
        print(number)

    if number == y:
        break