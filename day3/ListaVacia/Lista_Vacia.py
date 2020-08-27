list=[]

respuesta="si"
while respuesta=="si":
    cadena=input("Introduce lo que gustes a tu lista: ")
    list.append(cadena)
    respuesta=input("Quieres agregar otro valor a la lista?")

print(list)