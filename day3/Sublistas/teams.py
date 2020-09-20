#dada una lista, crea dos listas a partir de la primera e imprimelas
import random
Participantes=["Ofelia","Sandra","Jessica","Alma","Ana","Patricia","Jennifer","Andrea"]
random.shuffle(Participantes)
team1=Participantes[:len(Participantes)//2]
team2=Participantes[len(Participantes)//2:]
print(team1)
print(team2)
