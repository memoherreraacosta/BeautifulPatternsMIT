
def funcion(): #No tiene parametros
    print("Esta es tu primera funcion");

def estatura(altura): #Funcion con parametros
    print(f"Mides {altura} metros");

def persona(nombre, altura, edad): #funcion con mas de un parametro
    print(f"{nombre} mide {altura} metros y tiene {edad} años");

funcion(); #Tienes que mandar llamar la funcion
estatura(1.72); #tienes que mandar llamar a la funcion y pasar los parametros
persona("Mariana", 1.72, 20); #Tienes que pasar todos los parametros
