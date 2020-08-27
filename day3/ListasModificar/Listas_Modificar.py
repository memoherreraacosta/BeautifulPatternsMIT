usuarios=['nicole', 'luis', 'roberto']
contraseñas=['hola123', 'tec21', 'soylomax']

print(usuarios)
print(contraseñas)

user=input("introduce el usuario al que quieres modificar la contraseña: ")
for x in range(len(usuarios)):
    if usuarios[x] == user:
        contra=input("introduce la antigua contraseña: ")
        if contraseñas[x]==contra:
            contraM=input("introduce la nueva contraseña: ")
            contraseñas[x]=contraM
            break
        else:
            print("Contraseña incorrecta")
            break 
    else:
        print("No existe ese usuario")
        break

print(usuarios)
print(contraseñas)