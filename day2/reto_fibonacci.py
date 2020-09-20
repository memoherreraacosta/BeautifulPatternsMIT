"""
Conditionals programming exercises
Fibonacci series
If conditionals
"""

def fibonacci(n): 
    if n<0: 
        print("El numero tiene que ser mayor que 0")
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return fibonacci(n-1)+fibonacci(n-2) 

x = int(input("Escoge un numero 'x' al cual se le hara la serie de Fibonacci: "))
print(fibonacci(x)) 
  