#Funcion que te regresa el cuadradod el numero que elegiste
def cuadrado(num):
    numero = num**2; #doble asterisco es elevar algo
    return numero;

answer = cuadrado(int(input("Ingresa un numero: ")));
print(f"Tu numero al cuadrado es: {answer} ");
