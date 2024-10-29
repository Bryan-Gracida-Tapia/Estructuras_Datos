# Gracida Tapia Bryan.
# 23 de octubre del 2024.
# Descripción:
# Programa para identificar si una persona es mayor de edad.


#/////////////////////////////////////////////////////////////////////////////////////////
# Primer ejercicio
numero = int(input("ingrese un numero: "))       # Declaramos nuestras variables incluyendo input para la lectura por consola a la vez que realizamos el casting necesario.

if (numero%2) == 0:         # Se la sentencia if y en la condición se utiliza la operación modulo(%) para saber si su residuo es 0 o 1

    print("El numero es par")
    print("Al dividir el numero dado entre dos multiples veces da un residuo de 0")
else:                       # En python se utiliza else para realizar instrucciones en caso de que la primera condición no se cumpla
    print("El numero es impar")
    print("Al dividir el numero dado entre dos multiples veces da un residuo de 1 por lo cual es impar")
