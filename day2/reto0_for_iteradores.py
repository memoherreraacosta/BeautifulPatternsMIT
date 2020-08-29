"""
Conditionals programming exercises
For loop and iterators
"""

x = [1,2,3,4,5,6,7,8,9,10]
print(x)

y = [numero for numero in range(10)]
print(y)

z = [
    numero
    for numero in range(10)
    if numero % 2 == 0
]
print(z)

a = next(
    numero
    for numero in range(10)
    if numero % 2 == 0
    and numero > 0
)
print(a)