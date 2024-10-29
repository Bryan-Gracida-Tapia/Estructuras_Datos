# Gracida Tapia Bryan.
# 24 de octubre del 2024.
# Descripción:
# Programa que da a conocer la estación del año en la que se encuentra dependiendo del mes.


#/////////////////////////////////////////////////////////////////////////////////////////
print("  *** Programa que muestra en que estación te encuentras ***")

numero = int(input("Ingrese un número de un mes: "))    # Declaramos nuestras variables incluyendo input para la lectura por consola a la vez que realizamos el casting necesario.

if (numero >= 3 and numero < 6):        # Se ingresa un número el cuál de buscan entre las condiciones anidadas para saber a que estación pertenece ese número

    print("Estación: Primavera")

elif (numero >= 6 and numero < 9):

    print("Estación: Verano")

elif (numero >= 9 and numero < 12):

    print("Estación: Otoño")

elif (numero == 12 or numero == 1 or numero == 2):

    print("Estación: Invierno")

else :                                  # En caso de que no se cumpla ninguna de las condiciones llegará al else imprimiendo mes incorrecto
    print("Mes Incorrecto")
