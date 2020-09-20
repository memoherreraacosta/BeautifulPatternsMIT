"""
Conditionals programming exercises
For loop
"""

x = int(input("Escoge un numero positivo 'x': "))
print("La serie del 0 al 50 con saltos '{0}' es:".format(x))
for number in range(0, 51):
    if number % x == 0:
        print("El numero '{0}' es multiplo de {1}".format(number, x))
    else:
        print(number)
