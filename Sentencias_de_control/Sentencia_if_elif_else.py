# Gracida Tapia Bryan.
# 23 de octubre del 2024.
# Descripción:
# Programa para identificar el grupo de edad al que pertenece una persona.


#/////////////////////////////////////////////////////////////////////////////////////////
# Primer ejercicio
edad = int(input("ingrese una edad: "))     # Declaramos nuestras variables incluyendo input para la lectura por consola a la vez que realizamos el casting necesario.

if edad <= 14:                              # Se toma la edad ingresada y se busca el rango al que pertenece entre las condiciones.
    print("Niños y adolecentes")
elif (edad > 14 and edad <= 25):            # En python se utiliza ( elif ) para utilizar if anidados.
    print("Jovenes")
elif (edad > 25 and edad <= 45):
    print("Adultos jovenes")
elif (edad > 45 and edad <= 60):
    print("Adultos maduros")
else :                                      # Los if anidados se terminan con un else dando este fin a las condiciones.
    print("Adultos mayores")
