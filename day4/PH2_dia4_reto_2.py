#Empieza con
def empiezan_con(lista, letra):
    suma = 0
    for palabra in lista:
        if palabra[0] == letra:
            suma += 1
    return suma

#Llamada de prueba para la funcion
lista1 = ["andorra","andador","barco","tronco","alabama"]
print(empiezan_con(lista1,"s"))