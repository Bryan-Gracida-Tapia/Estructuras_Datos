# Gracida Tapia Bryan.
# 15 de octubre del 2024.
# Descripción:
# Ejemplificacion de operadores aritmeticos.


# Declaramos nuestras variables.
primer_numero = input("Introduce un número entero: ")      # Les agregamos un input para asi generar una entrada de datos por consola.
segundo_numero = input("Introduce otro número entero: ")
# Convertimos los valores recibidos anteriormente en flotantes.
primer_int = int(primer_numero)
segundo_int = int(segundo_numero)

# operaciones aritmeticas basicas

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
print(" ****  Multiplicacion  ****")
print(f"El resultado de la multiplicacion de {primer_int} y {segundo_int} es: {resultado_int}")

resultado_int = primer_int / segundo_int # Operación de divición.
print()
print(" ****  División  ****")
print(f"El resultado de la división de {primer_int} y {segundo_int} es: {resultado_int:.2f}")

resultado_int = primer_int % segundo_int # Operación de modulo.
print()
print(" ****  Modulo  ****")
print(f"El resultado de la división de {primer_int} y {segundo_int} es: {resultado_int}")

resultado_int = primer_int // segundo_int # Operación de divición entera.
print()
print(" ****  Divicion entera  ****")
print(f"El resultado de la división de {primer_int} y {segundo_int} es: {resultado_int}")

resultado_int = primer_int ** segundo_int # Operación de .
print()
print(" ****  Potencias  ****")
print(f"El resultado de la división de {primer_int} y {segundo_int} es: {resultado_int}")