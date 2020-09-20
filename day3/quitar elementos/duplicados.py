#Elimina los elementos duplicados en una lista ordenada
lista=[1,2,2,3,4,5,6,6,6,6,7,7,8,8,9,10,11,12,13,14,15,15,16,16,16,16,16,17]
anterior=lista[len(lista)-1]
indx=0
while(len(lista)>indx):
    tmp=lista[indx]
    if tmp==anterior:
        lista.remove(tmp)
    else:
        indx+=1
    anterior=tmp
print(lista)
