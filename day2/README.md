## Día 2: Estructuras y bucles de control
### Ejercicios de flujos de control `If, For, While`
---
![Ciclos](image/ciclos.png)


---

#### Condicionales `If, Elif, Else`

1. [Escoger numero Mayor](conditionals1.py):
   - En este ejercicio deberas de introducir dos numeros, 'x' y 'y', deberas de usar una estructura de control donde se imprime cual numero es el mayor. 

    ```
    Input data:
    Escoge un numero 'x': 10
    Escoge un numero 'y': 5

    Output data:
    El numero x: 10 es mayor
    ```
2. [Escoger numero Igual](conditionals2.py):
   
      
   - En este ejercicio deberas de introducir dos numeros, 'x' y 'y', deberas de usar una estructura de control donde se imprime cual numero es el mayor o si son iguales.
  
    ```
    Input data:
    Escoge un numero 'x': 5
    Escoge un numero 'y': 5

    Output data:
    Ambos numeros 'x' y 'y' son iguales: 5
    ```

1. [Calificaciones](conditionals3.py): 
   
      - En este ejercicio deberas usar una estructura de control donde asignaras una calificacion alfabetica a partir de una numerica donde los valores sean los siguientes.
    ```
    Reglas:
    Donde 'x' sea la calificacion en numero entero
    A: 100 >= x > 90
    B: 90  >= x > 80
    C: 80  >= x > 70
    O: 70  >= x > 0


    Ejemplos:

    Calificacion alumno 'x': 99
    La calificacion alfabetica de '99' es A 

    Calificacion alumno 'x': 90
    La calificacion alfabetica de '90' es B 

    Calificacion alumno 'x': 70   
    La calificacion alfabetica de '70' es O 

    Calificacion alumno 'x': -1
    La calificacion alfabetica de '-1' es Numero Negativo 

    Calificacion alumno 'x': 101     
    La calificacion alfabetica de '101' es Calificacion muy alta 
    ```

2. [Subpalabra dentro de Palabra](conditionals4.py):
   - En este ejercicio deberas usar una estructura de control donde se decidira si una palabra esta formada de otra palabra
    ```
    Input data:
    Escribe una palabra 'x': sororidad
    Escribe otra palabra 'y' donde se determinara si extiste dentro de la palabra 'x': ignorar 

    Output data:
    No existe la palabra 'ignorar' en la palabra 'sororidad'


    Input data:
    Escribe una palabra 'x': realidad
    Escribe otra palabra 'y' donde se determinara si extiste dentro de la palabra 'x': real

    Output data:
    Si existe la palabra 'real' en la palabra 'realidad'
    ```

---
#### Ciclos `For`
1. [Repetir numero N veces](for_loop1.py):
   - En este ejercicio deberas usar una estructura de control que te permita imprimir el numero '1' por 'n' veces.
    ```
    Ejemplo:
    Input data:
    Escoge la cantidad de veces que se repita el numero 1: 3

    Output data:
    1
    1
    1
    ```

2. [Repetir x numero en serie](for_loop2.py):
    - En este ejercicio deberas usar una estructura de control te permita imprimir la serie del numero 0 al 'x'.
    ```
    Ejemplo:
    Input data:
    Escoge un numero positivo 'x': 3
    La serie del 0 al numero positivo '3' es:

    Output data:
    0
    1
    2
    ```

3. [Serie de numeros a partir de una base](for_loop3.py):
    - En este ejercicio deberas usar una estructura de control te permita imprimir la serie del numero 10 al 'x'.
    ```
    Ejemplo:
    Input data:
    Escoge un numero positivo 'x': 13    
    La serie del 10 al numero positivo '13' es:
    
    Output data:
    10
    11
    12
    ```
   
4. [Serie de numeros con x saltos](for_loop4.py):
    - En este ejercicio deberas usar una estructura de control te permita imprimir la serie del numero '0' al '50' con saltos de cada 'x' numero.
    ```
    Ejemplo:
    Input data:
    Escoge un numero positivo 'x': 11
    La serie del 0 al 50 con saltos 'x' es:
    
    Output data:
    0
    11
    22
    33
    44
    ```

5. [Serie inversa con numeros negativos usando x saltos](for_loop5.py):
   - En este ejercicio deberas usar una estructura de control te permita imprimir una serie de numeros inversa (en este caso del numero '50' al '0') con 'x' saltos
    ```
    Ejemplo:
    Input data:
    Escoge un numero negativo 'x': -13
    La serie del 50 al 0 con saltos 'x' es:
    
    Output data:
    50
    37
    24
    11
    ```
6. [Serie de numeros multiplos](for_loop6.py):
   - En este ejercicio deberas usar una estructura de control te permita imprimir una serie de numeros del '0' al '50' que sean multiplos de 'x'
    ```
    Ejemplo:
    Input data:
    Escoge un numero positivo 'x': 11
    La serie del 0 al 50 con saltos '11' es:
    
    Output data:
    El numero '0' es multiplo de 11
    1
    .
    .
    .
    10
    El numero '11' es multiplo de 11
    12
    .
    .
    .
    21
    El numero '22' es multiplo de 11
    23
    .
    .
    .
    32
    El numero '33' es multiplo de 11
    34
    .
    .
    .
    43
    El numero '44' es multiplo de 11
    45
    .
    .
    .
    50
    ```
7. [Serie de numeros multiplos de n hasta llegar a x numero](for_loop7.py):
   - En este ejercicio deberas usar una estructura de control te permita imprimir una serie de numeros multiples de 'n' hasta llegar al numero x.
   ```
    Ejemplo:
    Input data:
    Escoge un numero positivo 'x': 3
    Escoge un numero positivo 'y' que sera el tope de la iteracion: 5

    Output
    La serie del 0 al '5' con saltos '3' es: 
    El numero '0' es multiplo de '3'
    1
    2
    El numero '3' es multiplo de '3'
    4
   ```

---
#### Ciclos `While`
1. [Imprimir serie de numeros sin salto de linea](while1.py):
    - En este ejercicio deberas usar una estructura de control de tipo "while" te permita imprimir la serie del numero '0' al 'x' sin salto de linea.
    ```
    Ejemplo:
    Escoge un numero positivo 'x': 10
    0 1 2 3 4 5 6 7 8 9 
    ```

2. [Imprimir serie de numeros multiplos de x](while2.py):
   - En este ejercicio deberas usar una estructura de control de tipo "while" te permita imprimir los numeros de la serie del numero '0' al '15' que sean multiplos de 'x' sin salto de linea.
    ```
    Ejemplo:
    Escoge un numero positivo 'x': 3
    0 3 6 9 12 
    ```

---
#### Retos y contenido extra
1. [Iteradores](contenido_for_iteradores.py):
   - Contenido extra de Iteradores usados con ciclos `For`. Ejercicios basicos de 'list comprehension' y operador 'next' para objetos iteradores.
2. [Formar patron A](reto1.py):
   - Reto de formar un patron impreso A
    ```
    Escribe un codigo de tal forma que te de el siguiente patron

    *
    **
    ***
    ****

    Tu programa debe de formar el patron con la siguiente informacion solicitada
    x: caracter a imprimir
    n: numero de niveles
    ```
3. [Formar patron B](reto2.py):
   - Reto de formar un patron impreso B
    ```
    Escribe un codigo de tal forma que te de el siguiente patron

    1
    22
    333
    4444

    Tu programa debe de formar el patron con la siguiente informacion solicitada
    n: numero de niveles
    ```
4. [Formar patron C](reto3.py):
   - Reto de formar un patron impreso C
    ```
    Escribe un codigo de tal forma que te de el siguiente patron

    1 
    1 2 
    1 2 3 
    1 2 3 4 
    1 2 3 4 5

    Tu programa debe de formar el patron con la siguiente informacion solicitada
    n: numero de niveles
    ```
5. [Formar patron D](reto4.py):
   - Reto de formar un patron impreso D
    ```
    Escribe un codigo de tal forma que te de el siguiente patron

    1 
    2 1 
    3 2 1 
    4 3 2 1 
    5 4 3 2 1

    Tu programa debe de formar el patron con la siguiente informacion solicitada
    n: numero de niveles
    ```
6. [Serie de Fibonacci](reto_fibonacci.py):
   - Generar una [serie fibonacci](https://es.wikipedia.org/wiki/Sucesi%C3%B3n_de_Fibonacci) usando solo condicionales


#### Mujeres en la ciencia

- [Margaret Hamilton](https://www.bbc.com/mundo/noticias-38097302)
- [Grace Hopper](https://www.infobae.com/tecno/2017/03/08/grace-hopper-la-mujer-que-revoluciono-el-mundo-de-la-computacion-para-siempre/)
- [Mujeres en la ciencia, Ada Lovelace, Marie Curie, Rosalind Franklin, entre muchas otras mujeres destacadas](https://elpais.com/especiales/2018/mujeres-de-la-ciencia/)
- [Medal of freedom ceremony](https://www.youtube.com/watch?v=X1PNp_YggAA&ab_channel=DonDeCosta)
