"""
Conditionals programming exercises
While loop

Escribe un codigo de tal forma que te de el siguiente patron

*
**
***
****

Tu programa debe de formar el patron con la siguiente informacion solicitada
x: caracter a imprimir
n: numero de niveles
"""

x = input("Escoge un caracter 'x' a imprimir: ")
y = int(input("Escoge un numero 'y' de niveles a imprimir: "))
idx = 0

while idx < y:
   idx += 1
   print(x * idx)

for i in range(y + 1):
   print(x * i)