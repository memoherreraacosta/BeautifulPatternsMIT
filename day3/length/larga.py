#cuál lista tiene más elementos?
list1=[1,5,6,8,9,2,3,4]
list2=[6,8,9,3,2,5,234,4,5]
if(len(list1)>len(list2)):
    print("la lista 1 es más larga")
elif(len(list1)<len(list2)):
    print("la lista 2 es más larga")
else:
    print("las listas tienen el mismo tamaño")