'''
Ejercicio 4: Otra vez una media
En un sistema de calificaciones de 0 a 20, donde 20 es la nota más alta y 0 la más baja.
Un profesor quiere escribir un programa que calcula la media de las cuatro notas obtenidas por sus alumnos en los deberes del mes. Además, el programa deberá calcular una evaluación automática según la media del alumno. Dará «Alumno con talento» si la media es superior a 15, «Con capacidad» si está comprendida entre 12 y 15, y, por último, «Debe reorientarse» si es inferior a 12.
Escribir un algoritmo que toma como entrada las cuatro notas de un alumno y que calcula la media y la evaluación correspondiente.
El problema anterior se puede resolver definiendo una estructura de datos que, para un alumno, agrupa su media y la evaluación. Un elemento de este tipo calcula el algoritmo solicitado.
'''
Entrada
nota1 float
nota2 float
nota3 float
nota4 float

Precondiciones
nota1, nota2, nota3, nota4 >= 0
nota1, nota2, nota3, nota4 <= 20

realizacion
media = (nota1 + nota2 + nota3 + nota4)/4
si media > 15
#Se mostraria el mensaje "Alumno con talento"
si no si 12 <= media <= 15
#Se mostraria el mensaje "Con capacidad"
si no media < 12
#Se mostraria el mensaje "Debe reorientarse"
fin si