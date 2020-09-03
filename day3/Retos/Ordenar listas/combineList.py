list1=[2,4,6,8,10,12,14,16]
list2=[1,3,5,7,9,11]
result=[]
point1=0
point2=0
for i in range(len(list1)+len(list2)):
    if point1<len(list1) and point2<len(list2):
        if(list1[point1]<list2[point2]):
            result.append(list1[point1])
            point1+=1
        else:
            result.append(list2[point2])
            point2+=1
    else:
        if point1==len(list1):
            result.append(list2[point2])
            point2+=1
        else:
            result.append(list1[point1])
            point1+=1
print(result)
