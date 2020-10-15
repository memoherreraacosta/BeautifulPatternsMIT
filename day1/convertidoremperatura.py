# Patrones hermosos

"""
CONVERTIDOR
"""
print("Seleccione una opción: \n1) Celsius a Fahrenheit \nFahrenheit a Celsius")
opt = int(input('(1 o 2): ' ))

if opt == 1:
    temp = float(input('Introduzca aqui la temperatura en celsis: '))
    print(str(temp) + " Celsius son " + str((temp * 9/5) + 32) + " Fahrenheit")
elif opt == 2:
    temp = float(input('Introduzca aqui la temperatura en fahrenheit: '))
    print(str(temp) + " Fahrenheit son " + str((temp - 32 ) * 5/9) + " Celsius")
