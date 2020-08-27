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
        
print("El número total de letras es " ,letras,'\n',"El número total de espacios es ",espacios,'\n',"El número total de consonantes es " ,cons,'\n',"El numero total de vocales es: " ,voc,'\n',"a: ",a,'\n',"e: ", e,'\n',"i: ",i,'\n',"o: ",o,'\n',"u: ",u)

