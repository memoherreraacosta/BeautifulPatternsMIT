"""
Conditionals programming exercises
While loop

Escribe un codigo de tal forma que te de el patron
de imagen:
The pattern like :

1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1

n: numero de niveles
"""

x = 5

for i in range(1, x):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()