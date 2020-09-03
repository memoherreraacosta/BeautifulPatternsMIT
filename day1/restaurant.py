# Patrones hermosos

"""
RESTAURANT
"""

edad = int(input('¿Qué edad tiene? '   ))

if(edad <= 10 && edad > 0){
    print("Menú infantil")
}else if( edad > 10 && edad <=18){
    print("Postre gratis")
}else if(edad > 18){
    print("Promoción 2x1")
}else{
    print("Por favor introduzca un número válido")
}
