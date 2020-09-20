"""
Conditionals programming exercises
While loop

Escribe un codigo de tal forma que te de el patron
de imagen:
The pattern like :

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

n: numero de niveles
"""

y = int(input("Escoge un numero 'y' de niveles a imprimir: "))

idx = 0
while idx < y:
   idx += 1
   idx_2 = 1
   while idx_2 < idx + 1:
       print(str(idx_2), end=" ")
       idx_2 += 1
   print()

for i in range(y + 1):
   for j in range(1, i + 1):
       print(j, end=" ")
   print()
