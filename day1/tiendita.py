# Patrones hermosos

"""
TIENDITA
"""
print("Bienvenido a la tiendita! :D \n")
print("Vendemos: \n -gansito \n -chokis \n -oreos \n -agua \n -chicles ")

opt = str(input('\n¿qué desea? ' ))

if(opt == "chokis"):
    print("Precio de chokis: $14.50")
elif opt == "oreos" :
    print("Precio de oreos: $15.20")
elif opt == "gansito" :
    print("Precio de oreos: $11")
elif opt == "agua" :
    print("Precio de agua: $15")
elif opt == "chicles" :
    print("Precio de agua: $7")
else:
    print("No tenemos ese producto :c ")
