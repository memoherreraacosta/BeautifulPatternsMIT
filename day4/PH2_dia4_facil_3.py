import random;

numero = random.randrange(100);


print("Adivina el numero que estoy pensando");
def atinale(num):
    if(num == numero):
        print("Felicidades le has atinado al numero");
        return #funciona como un break pero mas potente porque cierra todo el programa

    elif(num > numero):
        num1 = int(input("ingresa un numero menor "));
        atinale(num1); #llama a su misma funcion

    else:
        num1 = int(input("ingresa un numero mayor "));
        atinale(num1);


num = int(input("Ingresa un numero "));
atinale(num);
