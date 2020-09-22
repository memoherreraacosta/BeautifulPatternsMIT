#Promociones de servicio de internet
def ofertas(monto):
    if monto < 10:
        monto=monto
    elif monto <= 25:
        monto += monto * .03
    elif monto <= 50:
        monto += monto * .08
    else:
        monto += monto * .2
    return monto


#Impresion para probar la funcion
print("Tu monto total incluida la bonificacion correspondiente es: ",ofertas(30))