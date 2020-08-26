print('While con dados ')

print('lanza los dados tres veces y escribe el resultado de cada lanzamiento: ')
l1=int(input('primer lanzamiento:'))
l2=int(input('segundo lanzamiento:'))
l3=int(input('tercer lanzamiento:'))

lim=l1+l2+l3
count=0
print('el límite es: ', lim)
print('lanza un dado y escribe el resultado: ')
while count<lim:
    dado=int(input('número: '))
    count+=dado
    print('el número acumulado es: ', count)
print('¿Cuál fue el resultado final?')

