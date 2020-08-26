"""

Conditionals programming exercises

Calificaciones

If statements

if, else, elif, continue, break
"""

x = int(input("Calificacion alumno 'x': "))
calificacion = "Calificacion muy alta"

if 100 >= x:
    calificacion = "A"
    if 90 >= x:
        calificacion = "B"
        if 80 >= x:
            calificacion = "C"
            if 70 > x:
                calificacion = "Numero Negativo" if x < 0 else "F"

print("La calificacion alfabetica de '{0}' es {1} ".format(x, calificacion))
