# Gracida Tapia Bryan.
# 24 de octubre del 2024.
# Descripción:
# Programa que compara dos numeros, en busca del mayor.


#/////////////////////////////////////////////////////////////////////////////////////////
print("  *** Programa que determina si un numero es mayor o son iguales ***")

primer_numero = float(input("ingrese un numero decimal: "))         # Declaramos nuestras variables incluyendo input para la lectura por consola a la vez que realizamos el casting necesario.
segundo_numero = float(input("Ingresa otro numero decimal: "))

if primer_numero < segundo_numero:      # Se implementa a la condición un operador lógico para saber si el segundo número es menor al otro.
    print(f"El numero {primer_numero} es menor que el numero {segundo_numero}")

elif primer_numero > segundo_numero:    # Se implementa a la condición un operador lógico para saber si el primer número es mayor al otro.
    print(f"El numero {segundo_numero} es menor que el numero {primer_numero}")

else :                                  # En caso de no cumplir ninguna de las condiciones anteriores ámbos números seran iguales
    print("Los numeros son iguales")