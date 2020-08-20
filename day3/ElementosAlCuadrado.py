print("Todos los elementos al cuadrado")
lista=[]
valor=""
while valor!=0:
    valor=int(input("Ingresa un número entero para agregar a la lista, para terminar ingrese \"0\": "))
    lista.append(valor)
print("La lista ingresada es:             ", lista)

for i in range(len(lista)):
    lista[i]=lista[i]**2
print("La lista ingresada al cuadrado es: ", lista)

#Elementos al cuadrado
#Crea un programa donde ingreses datos a una lista, después recorre esta lista y eleva cada elemento al cuadrado
#PISTAS:
#Para determinar cuándo el usuario déje de ingresar datos a la lista puedes poner un mensaje como este:
# "Ingresa un número entero para agregar a la lista, para terminar ingrese 0: ", o alguna otra forma que tu gustes
# El operador para elevar un num. al cuadrado es: "num**exp"
