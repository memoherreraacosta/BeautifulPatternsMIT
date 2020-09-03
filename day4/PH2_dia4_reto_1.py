#Busqueda binaria
def busqueda_binaria(lista, elemento):
    primero = 0
    ultimo = len(lista)-1
    while(primero <= ultimo):
        mitad = primero + (ultimo - primero)//2
        if(lista[mitad] == elemento):
            return mitad
        elif(elemento < lista[mitad]):
            ultimo = mitad-1
        else:
            primero = mitad+1
    return -1

#Llamada para probar la funcion
lista1 = [1,2,3,4,5,6,7,8,9,10]
busca = 1
print(busqueda_binaria(lista1,busca))

