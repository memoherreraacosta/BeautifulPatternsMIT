preguntas=['nombre', 'objetivo', 'edad']
respuestas=['Leonardo', 'aprender Python', '18']

def imprimirValores(preguntas,respuestas):
    for preguntas, respuestas in zip(preguntas, respuestas):
     print ("¿Cual es tu", preguntas, "?"," la respuesta es: ",respuestas)

imprimirValores(preguntas,respuestas)