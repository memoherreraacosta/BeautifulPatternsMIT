lista1=["HOLA", "Mundo"]
lista2=[2,0,2,0]
lista3=[1,2,3,"probando...","accion!"]

def imprimir(lista):
    for x in range(len(lista)):
        print(lista[x],end="  ")

imprimir(lista1)
print(" ")
imprimir(lista2)
print(" ")
imprimir(lista3)