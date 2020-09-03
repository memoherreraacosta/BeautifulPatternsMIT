# Patrones hermosos

print("""
                         DESCUENTOS VENTA NOCTURNA""")
articulo=int(input("¿Cuántos artículos lleva?"))
cuenta=259.9*articulo
descuento=0
if articulo>=7:
    tarjeta=input("¿Cuenta con una tarjeta de crédito (si/no)? ")
    if tarjeta=="si":
        descuento=cuenta*.15
    elif tarjeta=="no":
        descuento=cuenta*.10
    else:
        print("Error - la respuesta no está dentro de las opciones")
elif articulo<7:
    hijos=int(input("¿Cuántos hijos tiene? "))
    if hijos>2:
        descuento=cuenta*.07
    elif hijos>0:
        descuento=0
    else:
        print("Por favor escriba un número positivo")

articulo*=259.
cuenta-=descuento
print("El precio sin descuento es: $", articulo)
print("El precio final es: $", cuenta, "con un descuento de", descuento)
