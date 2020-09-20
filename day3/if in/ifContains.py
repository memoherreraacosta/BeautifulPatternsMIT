numerosBuenos=[1,2,3]
numerosVenenosos=[4,5,6]

while True:
    var=int(input("\033[95mIntroduce el número\033[0m\n"))
    if var in numerosBuenos:
        print("\033[92m¡Felicidades, has ganado!\033[0m")
        break
    elif var in numerosVenenosos:
        print("\033[91mIntrodujiste un número venenoso. Suerte para la próxima\033[0m")
        break
    else:
        print("\033[93mEl número elegido no te puede dar la victoria, vuelve a intentarlo\033[0m")




