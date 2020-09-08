# Patrones hermosos

"""
Máxi mo y mínimo
"""

print("Ingresa un número entero: ")
n1 = int(input())
print("Ingresa otro  número entero: ")
n2 = int(input())
max, min

if(n1 == n2):
    print("Números iguales ")
else:
    if(n1 > n2):
        max = n1
        min = n2
    else:
        max = n2
        min = n1

imprimir = str(input("\nMáximo o mínimo(min/max): "))
if (imprimir == 'min'):
    print("\nEl número mímino es: " + str(min))
elif(imprimir == 'max'):
    print("\nEl número máximo es: " + str(max))
else:
    print("\nPor favor, ingrese solo 'min' o 'max'")
