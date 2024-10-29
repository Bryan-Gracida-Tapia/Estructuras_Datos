# Gracida Tapia Bryan.
# 15 de octubre del 2024.
# Descripción:
# Ejemplificación de operadores aritméticos.


# Declaramos nuestras variables.
primer_numero = input("Introduce un número entero: ")      # Les agregamos un input para así generar una entrada de datos por consola.
segundo_numero = input("Introduce otro número entero: ")
# Convertimos los valores recibidos anteriormente a enteros.
primer_int = int(primer_numero)
segundo_int = int(segundo_numero)

# operaciones aritméticas básicas

resultado_int = primer_int + segundo_int # Operación suma
print()
print(" ****  Suma  ****")
print(f"El resultado de la suma de {primer_int} y {segundo_int} es: {resultado_int}")

resultado_int = primer_int - segundo_int # Operación de resta.
print()
print(" ****  Resta  ****")
print(f"El resultado de la resta de {primer_int} y {segundo_int} es: {resultado_int}")

resultado_int = primer_int * segundo_int # Operación de multiplicación.
print()
print(" ****  Multiplicación  ****")
print(f"El resultado de la multiplicación de {primer_int} y {segundo_int} es: {resultado_int}")

resultado_int = primer_int / segundo_int # Operación de división.
print()
print(" ****  División  ****")
print(f"El resultado de la división de {primer_int} y {segundo_int} es: {resultado_int:.2f}")

resultado_int = primer_int % segundo_int # Operación de módulo.
print()
print(" ****  Módulo  ****")
print(f"El resultado de la división de {primer_int} y {segundo_int} es: {resultado_int}")

resultado_int = primer_int // segundo_int # Operación de división entera.
print()
print(" ****  División entera  ****")
print(f"El resultado de la división de {primer_int} y {segundo_int} es: {resultado_int}")

resultado_int = primer_int ** segundo_int # Operación de portencia.
print()
print(" ****  Potencias  ****")
print(f"El resultado de la potencia de {primer_int} y {segundo_int} es: {resultado_int}")