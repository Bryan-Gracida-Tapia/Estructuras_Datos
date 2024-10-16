# Gracida Tapia Bryan.
# 16 de octubre del 2024.
# Descripción:
# Ejemplificacion de operadores de asignacion compuesta.

#/////////////////////////////////////////////////////////////////////////////////////////
# Primer ejercicio
# Declaramos nuestras variables.
primer_numero = input("Introduce un número: ")
segundo_numero = input("Introduce otro número: ")

primer_int = int(primer_numero)
segundo_int = int(segundo_numero)

print(f"los numeros ingresados son {primer_int} y {segundo_int}")
# En python exixtentipos de operadores basicos compuestos tales como suma, resta, multiplicacion, divicion, etc.
primer_int += 3
segundo_int -= 5

print(f"los numeros con nuevo valor son {primer_int} y {segundo_int}")

primer_int *= 5
segundo_int /= 4

print(f"los numeros con nuevo valor son {primer_int} y {segundo_int}")
#////////////////////////////////////////////////////////////////////////////////////////////
# Segundo ejercicio
primer_numero = input("Introduce un número: ")      # Volvemos a ingresar .
segundo_numero = input("Introduce otro número: ")

primer_int = int(primer_numero)
segundo_int = int(segundo_numero)
primer_int += segundo_int
primer_int *= primer_int
primer_int -= segundo_int
primer_int += 3
primer_int /= 2

print(primer_int, segundo_int)