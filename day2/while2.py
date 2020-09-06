"""
Conditionals programming exercises
While loop
"""

x = int(input("Escoge un numero positivo 'x': "))

n = 0
while n < 100:
    if n % x == 0:
        print(n)
    n+=1

