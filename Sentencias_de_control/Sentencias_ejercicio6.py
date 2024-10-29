
# Gracida Tapia Bryan.
# 28 de octubre del 2024.
# Descripción:
# Programa que muestra el costo total de un tour.


#/////////////////////////////////////////////////////////////////////////////////////////
print("  *** Programa que determina el total de un Tour ***")
precio_adulto = 200     # Se declaran variables constantes
precio_niño = 100

nombre_persona_a_cargo = input("Ingrese el nombre de la persona a cargo: ")             # Declaramos nuestras variables incluyendo input para la lectura por consola a la vez que realizamos el casting necesario.
numero_adultos,numero_niños = int(input("Ingrese el total de adultos que tomaran el servicio: ")), int(input("Ingrese el total de niños que tomaran el servicio: "))
dia_semana = (input("Ingrese el día de la semana que se adquiere el servicio: "))

dia_semana = dia_semana.lower()         # Utilizamos la palabra reservada lower convertir el contenido de nuestra variable a minúsculas.

if dia_semana == "lunes" or dia_semana == "martes" or dia_semana =="jueves":        # Se compara la cadena previamente convertida con las cadenas siguientes "lunes", "martes", "jueves" para saber si se aplica descuento
    print(f"El encargado fue: {nombre_persona_a_cargo} y el día que se llevó el servicio fue: {dia_semana}")
    print(f"El costo total del tour es de :{(numero_adultos*precio_adulto)+(numero_niños*precio_niño)-((numero_adultos*precio_adulto)+(numero_niños*precio_niño))*0.1}")
else:                                   # En caso de no cumplir la condición se cobrará el monto predestinado sin descuento.
    print(f"El encargado fue: {nombre_persona_a_cargo} y el día que se llevo el servicio fue: {dia_semana}")
    print(f"El tour no aplica descuento por lo que el total es de :{(numero_adultos * precio_adulto) + (numero_niños * precio_niño)}")