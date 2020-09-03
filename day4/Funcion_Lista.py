####### FACIL
#Funcion que reciba una lista y un numero como parametro y regrese el elemento en el indice de esa lista

def get_elem(lst, i):
    return lst[i]

lista = [0,1,2,3,4,5]
index = 3
elem = get_elem(lista, index)
print(elem)