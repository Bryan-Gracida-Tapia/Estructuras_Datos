# Gracida Tapia Bryan.
# 16 de octubre del 2024.
# Descripción:
# Ejemplificación de operadores de asignación compuesta.

#/////////////////////////////////////////////////////////////////////////////////////////
# Primer ejercicio

primer_numero = input("Introduce un número: ")      # Declaramos nuestras variables incluyendo input para la lectura por consola.
segundo_numero = input("Introduce otro número: ")

primer_int = int(primer_numero)     # Se realiza el casting debido para una mejor manipulación de las variabes.
segundo_int = int(segundo_numero)

print(f"los numeros ingresados son {primer_int} y {segundo_int}")
# En python exixten tipos de operadores básicos compuestos tales como suma, resta, multiplicación, división, etc.
primer_int += 3     # Se denotan de la siguiente forma (variable operador_básico= número_o_variable)
segundo_int -= 5

print(f"los números con nuevo valor son {primer_int} y {segundo_int}")

primer_int *= 5
segundo_int /= 4

print(f"los números con nuevo valor son {primer_int} y {segundo_int}")
#////////////////////////////////////////////////////////////////////////////////////////////
# Segundo ejercicio
primer_numero = input("Introduce un número: ")      # Volvemos a ingresar dos números diferentes.
segundo_numero = input("Introduce otro número: ")

primer_int = int(primer_numero)
segundo_int = int(segundo_numero)
# Operaciones compuestas, esta vez realizadas con variables en lugar de números.
primer_int += segundo_int
primer_int *= primer_int
primer_int -= segundo_int
primer_int += 3
primer_int /= 2

print(primer_int, segundo_int)