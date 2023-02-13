'''
Un profesor planea organizar un viaje escolar. El coste del viaje depende de la cantidad de alumnos participantes.

El coste del trayecto es de 67,30 € por alumno hasta 25 alumnos y de 61,00 € si hay más de 25 alumnos. El coste de la comida es de 3,50 € por día y por alumno. Por último, el alojamiento es de 4,75 € por día y por alumno si la cantidad de alumnos es inferior a 30; 4,00 € para una cantidad de alumnos de entre 31 y 35, y 3,50 € si son más de 35.

Establecer el algoritmo de cálculo del precio de coste por alumno y del coste global del viaje en función de la cantidad de alumnos.
'''
alumnos = 60
dias = 7
coste_trayecto = 0
coste_total = 0
coste_comida= 3,50 * dias
coste_alojamiento = 0
coste_por_alumno = 0
if alumnos <= 25:
    coste_trayecto = 67,30
    coste_alojamiento = 4,75 * dias
elif 25< alumnos <= 30:
    coste_alojamiento = 4,75 * dias
    coste_trayecto = 61,00
elif 30 < alumnos <= 35:
    coste_alojamiento = 4,00 * dias
    coste_trayecto = 61,00
else: #Mayor de 35
    coste_alojamiento = 3,50 * dias
    coste_trayecto = 61,00

coste_por_alumno = coste_trayecto + coste_comida + coste_alojamiento
coste_total = coste_por_alumno * alumnos
