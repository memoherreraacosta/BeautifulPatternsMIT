# ¿Alguna vez pensaste que los números pueden ser venenosos?
>if x in list

Escribe un programa que contenga dos listas: una con números ganadores y otra con números venenosos. La persona que está jugando, tiene que ingresar un número del 1 al 10 (No es necesario validarlo, el número es solo para restringir la cantidad de casos posibles y hacer sencilla la jugabilidad). Si el número que ingresó se encuentra en la lista de números ganadores, **ganará el juego**, pero si el número está en la lista de los números venenosos, **pierde instantáneamente**. En caso de que el número ingresado no se encuentre en ninguna lista, vuelves a intentarlo hasta que exista alguna coincidencia.

### Instrucciones:
- Declara dos listas, una con los números ganadores y otra con los números venenosos.
- Ahora dentro de un ciclo infinito (`while true:`) haremos funcionar el juego.
- Pide que el usuario ingrese su número. 
- Si el numero está en la lista de ganadores, imprime un mensaje de victoria y termina el ciclo con `break`
- Si el numero está en la lista de perdedores, imprime un mensaje de derrota y termina el ciclo con `break`
- Si no se encuentra en ninguna lista, indica al usuario que vuelva a intentarlo.

