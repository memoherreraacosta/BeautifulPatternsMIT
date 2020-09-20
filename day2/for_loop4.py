"""
Conditionals programming exercises
For loop
"""

x = int(input("Escoge un numero positivo 'x': "))
print("La serie del 0 al 50 con saltos 'x' es:")
for number in range(0, 50, x):
    print(number)
