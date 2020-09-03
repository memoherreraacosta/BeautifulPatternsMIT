numero=int(input("Introduce el numero de elementos que quieras añadir a tu lista: "))
lista=[]

for i in range(numero):
    cadena=input("Introduce el valor")
    lista.append(cadena)

print(lista)
