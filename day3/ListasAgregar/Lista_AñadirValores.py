
numero=int(input("Introduce el numero de elementos que quieras añadir a tu lista"))
lista=[]

def añadir(cadena):
    lista.append(cadena)

for i in range(numero):
    cadena=input("Introduce el valor")
    añadir(cadena)

print(lista)