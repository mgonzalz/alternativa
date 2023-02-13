"""Ejercicio 3: Descuento
Un comerciante hace un descuento del 5 % en todas las compras con un importe comprendido entre 100 y 500 €, y del 8 % en los importes superiores.
Escribir el algoritmo de cálculo del importe del descuento en una compra dada."""

#Si el importe es menor a 100 no hay descuento
#si el importe esta entre 100 y 500 hay un descuento del 5%
#si el importe es mayor a 500 hay un descuento del 8%


Entrada:
importe = float
descuento = float
importe_final = float

Precondicion:
importe > 0

Realizacion:

si #el importe es menor a 100
    importe < 100:
entonces #no hay descuento
    descuento = 0
    importe_final = importe
si no si #el importe esta entre 100 y 500
    importe < 500
entonces #hay un descuento del 5%
    descuento = importe * 0.05
    importe_final = importe - descuento
si no #el importe es mayor a 500, hay un descuento del 8%
    descuento = importe * 0.08
    importe_final = importe - descuento
    
fin si

Postcondicion:
importe_final <= importe

Resultado:
importe_final = float
