Día 1
==============
# Temas
1.	Output
2.	Comments
3.	Variables
3.1.	float, string, int.
3.2.	booleans
4.	Símbolos
4.1.	operaciones básicas (+, -, *, /)
4.2.	otros símbolos (%, ==, <, >, =!, <=, >= )
5.	If (condicionales)

# Actividades de Programación
### Hola Mundo
1.	Crea un archivo y nómbralo hola_mundo.py
    	Este programa será un ejercicio para probar un output
2.	Haz un comentario de una línea con tu nombre
3.	Haz un comentario de línea múltiple con el nombre de esta actividad 
4.	Imprime ```Hola mundo```

### Input Output 
1.	Crea un archivo y nómbralo input_output.py
    Este programa será un ejercicio para hacer un input y un output
2.	Haz un comentario de una línea con tu nombre
3.	Haz un print de un enunciado preguntado un nombre: ```¿Cómo te llamas?```
4.	Crea una variable nombre que reciba un input
5.	Imprime un enunciado incluyendo la variable de tal manera que el output sea: ¡Hola + nombre!
    Ejemplo: ```¡Hola Andrea!```

### Operaciones 1
1.	Crea un archivo y nómbralo operaciones_1.py
Este programa será un ejercicio para probar las operaciones básicas matemáticas en Python 
2.	Haz un comentario de una línea con tu nombre
3.	Imprime ```Ingresa un número entero: ```
4.	Crea una variable n1 que reciba un input integer 
5.	Imprime ```Ingresa otro número entero: ```
6.	Crea una variable n2 que reciba un input integer
7.	Imprime la suma, resta, multiplicación, y division de estos números en diferentes líneas
    a.	Extra: realiza la instrucción del print en una sola línea utilizando \n para salto de línea


### Paralelogramo
1.	Crea un archivo y nómbralo paralelogramo.py
	En este programa calcularás el área de un paralelogramo
2.	Haz un comentario con tu nombre
3.	Recibe 2 floats de la altura y la base de tu paralelogramo.
        	*base = float(input(“Base: ”))*
4.	Calcula el área del paralelogramo y haz un print de la siguiente manera: 
        ```El área de el paralelogramo de (n) de base y (m) de altura es de (resultado) ```

### Operaciones 2
1.	Crea un archivo y nómbralo operaciones_2.py
    	Este programa será un ejercicio para probar las más operaciones matemáticas en Python 
2.	Haz un comentario de una línea con tu nombre
3.	Imprime ```Ingresa un número con decimal: ```
4.	Crea una variable n1 que reciba un input float 
5.	Imprime ```Ahora un número entero:```
6.	Crea una variable n2 que reciba un input integer
7.	Imprime el resultado de las siguientes operaciones:
    1)  Potencia: ```n1 ** n2```
    2)	División de enteros: ```n2 // n1```
    3)	Módulo residuo: ```n2 % n1```
    4)	División y suma:```n1 / n2 + n1```
    5)	División y suma con paréntesis: ```n1 / (n2 + n1)```

### Cilindro
1.	Crea un archivo y nómbralo cilindro.py
	En este programa calcularás el volumen de un cilindro
		```V = h * π * r²```
2.	Haz un comentario con tu nombre
3.	Recibe 2 floats de la altura y el diametro de un cilindro
4.	Calcula el volumen del cilindro  y haz un print de la siguiente manera: 
	```El volumen del cilindro de (n) de diámetro y (m) de altura es de (resultado)*```

### Restaurant
1.	Crea un archivo y nómbralo restaurant.py
	En este programa simularás las opciones del restaurant dependiendo de la edad del cliente
2.	Pregunta por la edad del cliente
3.	Dependiendo de la edad haz un print de
	a.	Menor o igual a 10 años: Menú infantil
	b.	De 10 a 18: Postres gratis (utiliza el operador AND)
	c.	Mayor a 18: Promoción 2x1
	d.	Si es un numero negativo: Por favor introduzca un número válido

### Par e impar
1.	Crea un archivo par_impar.py
	Este programa será un ejercicio para entender los condicionales
2.	Haz un comentario de una línea con tu nombre
3.	Imprime ```Ingresa un número entero: ```
4.	Crea una variable num que reciba un input integer 
5.	Crea un if donde se imprima si el número es par o impar 
	•	Puedes utilizar la operación módulo residuo entre 2 y si es 0 es par:
			```8 % 2 = 0```
			
### Convertidor de unidades
1.	Crea un archivo convertidortemperatura.py
	En este programa simularás un convertidor de unidades donde:
		```(0 °C × 9/5) + 32 = 32 °F ```
2.	Haz un comentario de una línea con tu nombre
3.	Despliega dos opciones para la conversión
	1)	Convertir de Celsius a fahrenheit
	2)	Convertir de fahrenheit a Celsius
4.	Dependiendo del input (1 o 2) imprimirás:
	1)	Escribe la temperatura en Celsius
	2)	Escribe la temperatura en fahrenheit
5.	Harás un print de la temperatura convertida con el nombre de su unidad correspondiente de la siguiente manera: 
		```25 grados Celsius son 77 grados Fahrenheit```
		
### Tiendita
1.	Crea un archivo tiendita.py
	En este programa simularás una tienda que te dirá el precio de algún producto:
	•	gansito: $11
	•	chokis: $14.50
	•	oreos: $15.20
	•	agua: $15
	•	chicles: $7
2.	Haz un comentario de una línea con tu nombre
3.	Imprime un mensaje de bienvenida y despliega los productos sin mostrar el precio
4.	Imprime ```Qué desea comprar```
5.	En una variable guardarás el input de la respuesta
6.	Utiliza ifs para desplegar el precio del producto que pidieron
	Ejemplo: ```Chokis: $15.40```
7.	Si el input no coincide con ninguno de los productos entonces imprime ```Lo sentimos, no tenemos este producto```



# Retos

## Operaciones 3 
1.	Crea un archivo reto_operaciones_3.py
2.	Haz un comentario con tu nombre
3.	Imprime ```Ingresa un número con decimal: ```
4.	Crea una variable n1 que reciba un input float 
5.	Imprime ```Ahora un número entero:```
6.	Crea una variable n2 que reciba un input integer
7.	Utiliza la librería math para realizar las siguientes operaciones:
	1)	Potencia de n1 ^ n2
	2)	N1 número multiplicado por pi (π)
	3)	Raiz cuadrada de n2
	4)	Ceil de n1:  math.ceil(n1)
	5)	Floor de n1: math.floor(n1)
	6)	Qué hacen Ceil y Floor? 

## Máximo y mínimo
1.	Crea un archivo reto_max_min.py
	Este programa será un ejercicio para entender los condicionales 
2.	Haz un comentario de una línea con tu nombre
3.	Imprime ```Ingresa un número entero: ```
4.	Crea una variable n1 que reciba un input integer 
5.	Imprime ```Ingresa otro número entero: ```
6.	Crea una variable n2 que reciba un input integer
7.	Crea las variables max y min donde guardes el número máximo y el mínimo de los dos números utilizando las operaciones <, > en ifs. Si los números son iguales imprime 		```Números 	       iguales``` y termina el programa.  
8.	Imprime ```Mínimo o máximo (min / max): ```
	Esta línea buscas hacer un input de string donde pongas si quieres que el output sea el número mínimo o máximo
9.	Crea un if comparando el string corresponde a min o max.
	a.	Si es min harás un print que diga ```“El número mímino es: ” + min```
	b.	Si es max harás un print que diga ```“El número máximo es: ” + max```

## Venta nocturna
1.	Crea un archivo reto_venta_nocturna.py
	En este programa calcularás el precio con descuentos de una venta nocturna
2.	Haz un comentario con tu nombre
3.	Pregunta cuantos artículos lleva. El precio de cada artículo es $259.9
4.	Los descuentos se calcularán de la siguiente manera:
	a.	Si el cliente lleva una cantidad mayor o igual a 7 artículos entonces preguntarás si tiene tarjeta de crédito. Si tiene tarjeta de crédito entonces el cliente 			recibirá un 15% de descuento. Si no tiene tarjeta entonces recibirá un 10% de descuento
	b.	Si el cliente lleva menos de 7 artículos entonces preguntarás cuantos hijos tiene. Si el cliente tiene más de 2 hijos entonces recibirá un descuento de 7%. De no ser     		  así no recibirá ningún descuento. 
	c.	Validar que el número de artículos sea un número positivo.
5.	Al final deberás desplegar cual sería el precio de todo sin descuento, cuanta es la cantidad del descuento y como quedaría el precio al final.








