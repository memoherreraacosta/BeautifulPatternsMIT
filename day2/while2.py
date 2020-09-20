"""
Conditionals programming exercises
While loop
"""

x = int(input("Escoge un numero positivo 'x': "))

n = 0
while n < 15:
    if n % x == 0:
        print(n, end=" ")
    n+=1
print()
