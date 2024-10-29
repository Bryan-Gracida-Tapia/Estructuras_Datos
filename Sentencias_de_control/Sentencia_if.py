# Gracida Tapia Bryan.
# 23 de octubre del 2024.
# Descripción:
# Programa para identificar si una persona es mayor de edad.


#/////////////////////////////////////////////////////////////////////////////////////////
# Primer ejercicio
edad = int(input("ingrese su edad: "))      # Declaramos nuestras variables incluyendo input para la lectura por consola a la vez que realizamos el casting necesario.
if edad >= 18:      # la sentencia if en python se denota como ( if condicion:)
    # Codigo a ejecutar dentro del if
    # En python en lugar de llaves se utilizan tabulaciones para identificar que codigo se ejecutara dentro del if.
    print("Eres mayor de edad..")
    print("codigo que se ejecuta despues de que la condicion se cumple")
print("No cumple la condicion")     # En este punto donde ya no se encuentra la tabulacion antes de la instruccion significa que ya no pertenece a la sentencia if.