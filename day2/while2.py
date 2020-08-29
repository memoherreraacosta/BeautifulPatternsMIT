"""
Conditionals programming exercises
While loop
"""

def binary_search(a_list, key):
       low = 0
       high = len(a_list)-1
       mid = (low + high)//2
       while low <= high:
          mid = (low + high)//2
          if a_list[mid] == key:
             return "El numero {0} existe en el rango indicado"
          if a_list[mid] > key:
             high = mid - 1
          else:
             low = mid + 1
       return "No existe el numero {0} en el rango indicado"

x = int(input("Escoge un rango de numeros 'x' (ejemplo, del 0 al 'x'): "))
y = int(input("Escoge un numero 'y' a encontrar en la lista: "))

a_list = [i for i in range(x)]
print(binary_search(a_list, y))