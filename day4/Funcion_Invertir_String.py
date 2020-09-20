####### INTERMEDIO
# Crea una funcion que reciba un string y lo regrese inviertido

def reverse1(string):
    rev = ''
    length = len(string)
    for i in range(length):
        rev += string[length-1-i]
    return rev

def reverse2(string):
    rev = ''
    length = len(string)
    for i in range(length):
        rev += string[-(i+1)]
    return rev

def reverse3(string):
    return string[::-1]

print(reverse1(string))
print(reverse2(string))
print(reverse3(string))

