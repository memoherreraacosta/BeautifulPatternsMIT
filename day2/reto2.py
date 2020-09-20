"""
Conditionals programming exercises
While loop

Escribe un codigo de tal forma que te de el patron
de imagen:
The pattern like :

1
22
333
4444

n: numero de niveles
"""

y = int(input("Escoge un numero 'y' de niveles a imprimir: "))
idx = 0

while idx < y:
   idx += 1
   print(str(idx) * idx)

for i in range(y + 1):
   print(str(i) * i)
