#Multiplos comunes
def multiplos_comunes(num1,num2,lim):
    multiplos = []
    for indice in range(0, lim):
        if indice % num1 == 0:
            if indice % num2 ==0:
                multiplos.append(indice)
    return multiplos


#Impresion para probar la funcion
num1 = int(input("Ingresa el primer numero \n"))
num2 = int(input("Ingresa el segundo numero \n"))
lim = int(input("Ingresa el limite \n"))
print(f"Los multiplos comunes entre {num1} y {num2} menores que {lim} son: \n")
print(multiplos_comunes(num1,num2,lim))
