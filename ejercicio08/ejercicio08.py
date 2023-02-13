"""Ejercicio 8: Prima anual
A final de año, la empresa LA CAMPANA paga una prima anual a sus empleados camioneros.
En principio, el conductor recibirá la prima anual completa si no ha tenido accidentes con una responsabilidad superior o igual al 20 % durante el año que termina. Si la responsabilidad es superior al 20 %, la empresa considera al conductor responsable del accidente. Si el conductor ha sido responsable de un accidente, solo recibe la mitad de la prima. Con dos accidentes, solo recibe un tercio. Con tres accidentes, la prima se reduce a un cuarto. Si supera los tres accidentes, la prima se anula.
Esta prima es la suma de una prima de distancia y de una prima de antigüedad.
La prima de distancia aumenta un céntimo por kilómetro recorrido durante el año, con un máximo de 400 €.
La prima de antigüedad solo se paga una vez transcurridos cuatro años de antigüedad y es de 200 €. Luego aumenta 20,00 € por año adicional.
Escribir el algoritmo de cálculo de la prima anual que se concederá a cada conductor."""
#No ha tenido accidentes con una responsabilidad superior o igual al 20 % recibe la prima anual completa
#Ha tenido un accidente con una responsabilidad superior o igual al 20 % recibe la mitad de la prima
#Ha tenido dos accidentes con una responsabilidad superior o igual al 20 % recibe un tercio de la prima
# Ha renido tres accidentes con una responsabilidad superior o igual al 20 % recibe un cuarto de la prima
#Ha tenido más de tres accidentes con una responsabilidad superior o igual al 20 % no recibe la prima
#Prima = prima de distancia + prima de antigüedad
#Prima de distancia = 0.01 * km recorridos durante el año (máximo 400€)
#Prima de antigüedad = 200€ + 20€ por año adicional (a partir del 4º año)


