def sucesor(dia):
    if dia == "Lunes":
        return "Martes"
    elif dia == "Martes":
        return "Miercoles"
    elif dia == "Miercoles":
        return "Jueves"
    elif dia == "Jueves":
        return "Viernes"
    elif dia == "Viernes":
        return "Sabado"
    elif dia == "Sabado":
        return "Domingo"
    elif dia == "Domingo":
        return "Lunes"

dia = int(input("Ingrese un dia de la semana: "))
dias_Semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
if dia >= 7 or dia <= 1:
    dia = dias_Semana[dia-1]
    print("El dia siguiente es: ", sucesor(dia))
else:
    print("El dia ingresado no es valido")

