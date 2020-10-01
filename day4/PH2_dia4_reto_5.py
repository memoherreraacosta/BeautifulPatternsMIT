####### AVANZADO
# Crea una funcion que reciba una lista de numeros y la regrese ordenada de manera ascendente, 
# puedes crear otra lista u ordenar la misma lista

def bubble_sort(lst):
    for _ in range(len(lst)):
        for j in range(len(lst)-1):
            if lst[j]>lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst 

lst = [9,8,7,6,5,4,3,2,1,0]
print(lst)
bubble_sort(lst)
print(lst)