print("Analizador de palíndromos")
p = input("Ingresa una palabra: ")


def palindromo(p):
    if len(p)<= 1:
        return True
    else:
        if p[0]==p[-1]:
           return palindromo(p[1:-1])
        else:
           return False

if palindromo(p) is True:
    print("la palabra: ",p, "es palindromo")
else:
    print("la palabra: ",p, "no es palindromo")