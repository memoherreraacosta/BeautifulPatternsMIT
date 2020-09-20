#Barra de progreso
import time
def barra_progreso(segundos,n):
    impresiones = segundos // n
    for i in range(0, impresiones):
        time.sleep(n)
        print("X", end="")

#Llamada para probar la funcion
barra_progreso(20,1)