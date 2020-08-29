"""
Conditionals programming exercises
Calificaciones
If statements
if, else, elif, continue, break
"""

palabra_x = input("Escribe una palabra 'x': ")
palabra_y = input("Escribe otra palabra 'y' donde se determinara si extiste dentro de la palabra 'x': ")

existe = False
respuesta = "la palabra '{0}' en la palabra '{1}'".format(palabra_y, palabra_x)
if palabra_y in palabra_x:
    print("Si existe " + respuesta)
else:
    print("No existe " + respuesta )
