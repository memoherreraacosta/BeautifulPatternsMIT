preguntas=['nombre', 'objetivo', 'edad']
respuestas=['Leonardo', 'aprender Python', '18']


for preguntas, respuestas in zip(preguntas, respuestas):
    print ("¿Cual es tu", preguntas, "?"," la respuesta es: ",respuestas)
