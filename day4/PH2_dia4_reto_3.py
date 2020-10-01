####### AVANZDO
# Crea una funcion que reciba dos strings y regrese true si ambos strings son iguales o estan a una edicion de distancia,
# siendo las edidiciones borrar un caracter, insertar un caracter o cambiar un caracter. Si esta a mas de una edicion de 
# distancia regresa False
"""
Ejemplo:
    'hola', 'ola'  regresa True
    'hola', 'bola' regresa True
    'hola', 'ela' regresa False
"""

def one_away(str1, str2):
    if abs(len(str1)-len(str2))>1:
        return False
    count1 = count2 = 0
    diff = 0
    while count1 < len(str1) and count2 < len(str2):
        if diff > 1:
            return False
        if str1[count1] == str2[count2]:
            count1 += 1
            count2 += 1
        else:
            if str1[count1+1] == str2[count2+1]:
                count1 += 1
                count2 += 1
                diff += 1
            elif str1[count1+1] == str2[count2]:
                count1 += 1
                diff += 1
            elif str1[count1] == str2[count2+1]:
                count2 += 1
                diff += 1
            else:
                return False
    return True

str1 = input("Introduce first string\n")
str2 = input("Introduce second string\n")
is_one = one_away(str1, str2)
if is_one:
    print("True")
else:
    print("False")