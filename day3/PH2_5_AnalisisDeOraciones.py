print("Analizador de oraciones")
cadena = input("Ingresa una oración: ")
voc = 0
a = 0
e = 0
i = 0
o = 0
u = 0
cons = 0
letras = 0
espacios = 0

for y in cadena:
    if y=="a":
        voc+=1
        a+=1
        letras+=1
    elif y=="e":
        voc+=1
        e+=1
        letras+=1
    elif y=="i":
        voc+=1
        i+=1
        letras+=1
    elif y=="o":
        voc+=1
        o+=1
        letras+=1
    elif y=="u":
        voc+=1
        u+=1
        letras+=1
    elif y==" ":
        espacios+=1
    else:
        cons+=1
        letras+=1
        
print(f"El número total de letras es {letras}\nEl número total de espacios es {espacios}\nEl número total de consonantes es {cons}\nEl numero total de vocales es: {voc}\na: {a}\ne: {e}\ni: {i}\no: {o}\nu: {u}")
