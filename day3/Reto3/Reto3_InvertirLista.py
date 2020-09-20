lista = [2, 5, 8, 9, 12, 19, 25, 27, 32, 60, 65, 1, 7, 24, 124, 654,1]

print ("lista original ",lista)                 
tamanio = len(lista)             
contador_inverso = tamanio - 1
punto_medio = round(tamanio/2)                
for i in range(0, punto_medio):   
    temp = lista[contador_inverso]     
    lista[contador_inverso] = lista[i]
    lista[i] = temp
    contador_inverso -= 1    
print ("lista inversa ",lista)                    
