#regresa los elementos en comun de una lista
list1=[1,5,7,9,3,2,456,7,4,5,6,2,8,56,3,7,8]
list2=[6,9,13,15,7,5,13,35,21]
result=[]
for x in list1:
    if x in list2:
        result.append(x)
print(result)