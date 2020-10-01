## Día 4: Funciones

1. [Primeras funciones](PH2_dia4_facil_1.py):
   - Crea una funcion llamada funcion que haga un print
   - Crea una funcion llamada estatura que reciba el parametro altura. Haz que imprima 'Mides (altura) metros'
   - Crea una funcion llamada persona que reciba 3 parametros: nombre, altura, edad. Haz que imprima '(nombre) mide (altura) metros y tiene (edad) años'
   - Llama las tres funciones

    ```
    Output data:
    Esta es tu primera funcion
    Mides 1.72 metros
    Mariana mide 1.72 metros y tiene 20 años

    ```
2. [Cuadrado](PH2_dia4_facil_2.py):
   - Crea una funcion llamada cuadrado que reciba un numero como parametro y lo regrese elevado al cuadrado.
   - Haz un input para que un usuario ponga un numero
   - Imprime el resultado

    ```
    Input data:
    Ingresa un numero: 5

    Output data:
    u numero al cuadrado es: 25

    ```
3. [¡Atínale!](PH2_dia4_facil_3.py):
   - Crea un programa que genere un numero random del 0 al 99.
   - Haz una funcion que reciba un numero como parametro y verifique si ese numero recibido es igual. Si lo es, que imprima un mensaje de victoria. De lo contrario, tiene que imprimir si el numero recibido es mayor o menor.
  
4. [Volumen de una esfera](PH2_dia4_facil_4.py):
   - En este ejercicio deberas introducir un numero, 'r', deberas encontrar el volumen de la esfera. 
   - Define la funcion llamada calcularVolumenEsfera

    ```
    Input data:
    Escoge un numero 'r': 5

    Output data:
    El volumen de la esfera es: 523.59

    ```
5. [Obtener elemento](PH2_dia4_facil_5.py):
   - Crea una funcion que reciba una lista y un indice, y regrese el elemento de la lista en ese indice.

    ```
    lista: [1,2,3,4,5]
    indice: 3

    Output data:
    El elemento en ese indice es: 4
    ```
6. [Multiplos comunes](PH2_dia4_intermedio_1.py):
   
      
   - En este ejercicio deberas diseñar una funcion que recibe tres numeros 'num1', 'num2' y 'num3'. Los dos primeros corresponden a los números de los cuales buscarás sus múltiplos en común. El tercer número es un límite. Por ejemplo: Si ingresas 6,10 y 100, la función deberá encontrar los múltiplos comunes entre 6 y 10 y que son menores a 100, ponerlos en una lista y regresar esta lista como resultado de la función.  
  
    ```
    Input data:
    Ingresa el primer numero 'num1': 6
    Ingresa el segundo numero 'num2': 10
    Ingresa el tercer numero 'num3': 100

    Output data:
    Los multiplos comunes entre 'num1' y num2' menores que 100 son: [0,30,60,90]
    ```

7. [Promociones](PH2_dia4_intermedio_2.py): 
   
      - Un servicio de internet tiene un sistema de recompensas que funciona de la siguiente manera: 
     •Si cargas menos de 10 dólares, no obtienes nada extra. 
     • Si cargas entre 10 y 25 dólares (inclusive) obtienes un 3% extra.
     •Con una carga entre 25 y 50 (inclusive), obtienes 8% extra.
     •Con una carga mayor a 50 dólares, obtienes 20% extra. 
    Diseña una funcion que reciba el monto a cargar por el usuario y retorne el monto total (incluyendo la     bonificacion correspondiente)
    ```
    Ejemplos:

    Monto a recargar  'x': 9
    El monto total por la recarga de  '9' es: 9 

    Monto a recargar 'x': 20
    El monto total por la recarga de  '20' es: 20.6 

    Calificacion alumno 'x': 30  
    El monto total por la recarga de '30' es:32.4
    ```

8. [Barra de progreso](PH2_dia4_intermedio_3.py):
   - En este ejercicio deberas definir una función que despliega una barra de progreso en la terminal de Python. 
   Hará esto mediante la impresión de una X cada “n” cantidad de segundos hasta llegar a un límite de tiempo establecido. 
    ```
    Input data:
    Ingrese la cantidad de caracteres de la barra 'n': 10
    Ingresa la cantidad de tiempo de espera 't': 50 
    Output data: XXXXXXXXXX

    ```
9. [oditrevnI](PH2_dia4_intermedio_4.py):
   - Crea una funcion que reciba un string y lo regrese invertido
    ```
    string: 'Hello world'
    
    output: dlrow olleH

    ```
10. [Substring](PH2_dia4_intermedio_4.py):
   - Crea una funcion is_substring que reciba dos strings, y detecte si el segundo es un subtring del primero
   - Regresa true o false dependiendo el caso
   - Imprime si es un substring o no
    ```
    strings: 'Hello world', 'o wo'
    
    output: 'o wo' es un substring de 'Hello world'

    strings: 'Hello world', 'unu'
    
    output: 'unu' no es un substring de 'Hello world'

    ```
11. [Busqueda binaria](PH2_dia4_reto_1.py):
   - La búsqueda binaria es un algoritmo muy eficiente para realizar búsquedas en listas que se encuentran ordenadas. Funcionan a través de dividir el problema, descartando la mitad de los elementos de la lista en cada iteración. Los pasos para realizar una búsqueda binaria son:
    •Ver el elemento que se encuentra a la mitad de la lista, si el elemento que busco es mayor, descarto la primera mitad de la lista y busco en la segunda mitad. (Nuevamente en el elemento que se encuentre a la mitad de ese segmento). 
Si el elemento es menor, descarto la segunda mitad del segmento y busco en el elemento que se encuentra en la mitad que me interesa. Continúo de esa manera hasta encontrar el elemento o descubrir que no se encuentra en la lista. 
    •Con el algoritmo anterior, se reduce el tiempo que toma la búsqueda. Para poder implementarlo siempre debemos mantener dos índices que nos marquen la posición inicial y final del segmento de la lista en donde estamos buscando, de manera que siempre podamos encontrar el elemento central. 
    Diseña una función que implemente la búsqueda binaria. Debera retornar el indice en el que se encontro el valor indicado, en caso de no encontrarlo, retorna -1.

    ```
    Ejemplo:
    Input data:
    Lista1 = [1,2,3,4,5,6,7,8,9]
    Ingresa el numero a buscar 'bucar': 5
    Output data: 4
    ```

12. [Empieza con: ] (PH2_dia4_reto2.py)
    -Diseña una función que recibe una lista de strings y una letra. La función retorna la cantidad de palabras que comienzan con la letra indicada. 

13. [Uno de distancia](PH2_dia4_reto_3.py):
   - Crea una funcion que reciba dos strings y regrese true si ambos strings son iguales o estan a una edicion de distancia, siendo las edidiciones borrar un caracter, insertar un caracter o cambiar un caracter. Si esta a mas de una edicion de distancia regresa False
   - Imprime los resultados

    ```
    Ejemplo:
    strings: 'hola', 'ola'
    output: 'hola' y 'ola' estan a una edicion de distancia

    strings: 'hola', 'bola'
    output: 'hola' y 'bola' estan a una edicion de distancia

    strings: 'hola', 'ela'
    output: 'hola' y 'ela' estan a mas de una edicion de distancia

    ```
14. [Rotación de matriz](PH2_dia4_reto_4.py):
   - Crea una funcion que reciba una matriz (listas anidadas) de n x n y la rote a la derecha, sin crear una segunda matriz
   - Imprime los resultados

    ```
    Ejemplo:
    matriz: 
            [[0,2]
             [3,4]]
    matriz rotada:
            [[3,0]
             [4,2]]

    ```

15. [Sort](PH2_dia4_reto_5.py):
   - Crea una funcion que reciba una lista de numeros y la regrese ordenada de manera ascendente
   Nota: puedes crear otra lista u ordenar la misma lista

    ```
    Ejemplo:
    lista: [9,8,7,6,5,4,3,2,1,0]
    output: [0,1,2,3,4,5,6,7,8,9]

    ```

