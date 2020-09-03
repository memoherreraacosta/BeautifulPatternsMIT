####### INTERMEDIO
# Crea una funcion is_substring que reciba dos strings, y detecte si el segundo es un subtring del primero.
# Regresa true o false dependiendo el caso

"""
Ejemplo:
    'bot' es un substring de 'bottle' 
"""

def is_substring(str1, str2):
    count = 1
    for i in range(len(str1)-len(str2)):
        if str1[i] == str2[0]:
            for j in range(1,len(str2)):
                if str1[i+j]==str2[j]:
                    count+=1
                else:
                    count=1
                    break
            if count == len(str2):
                return True
    return False

is_sub = is_substring('bottle', 'bot')
if is_sub:
    print("It is")
else:
    print("It is not")

