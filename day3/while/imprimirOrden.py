#dada una lista, imprime los numeros de manera ascendente
list=[4,7,9,1,5,2,34,7,8,3,2,12,111,13,21]
while list:
    menor=list[0]
    for x in list:
        if x<menor:
            menor=x
    print(menor)
    list.remove(menor)

