#dada una lista, crea dos listas a partir de la primera e imprimelas
import random
continuar="si"
Participantes=[]
while continuar == "si":
    cadena=input("Introduce el nombre de la persona que jugará: ")
    Participantes.append(cadena)
    continuar=input("¿Deseas agregar más personas a la lista? responde si para agregar a otra persona ")
random.shuffle(Participantes)
team1=Participantes[:len(Participantes)//2]
team2=Participantes[len(Participantes)//2:]
print("Equipo 1:")
print(team1)
print("Equipo 2asd:")
print(team2)
