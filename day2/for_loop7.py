"""

Conditionals programming exercises

For loop
"""

x = int(input("Escoge un numero positivo 'x': "))
y = int(input("Escoge un numero positivo 'y' que sera el tope de la iteracion: "))

print("La serie del 0 al 50 con saltos 'x' es:")
for number in range(0, 50):
    if number % 5 == 0:
        print("El numero '{0}' es multiplo de 5".format(number))
    else:
        print(number)

    if number == y:
        break
