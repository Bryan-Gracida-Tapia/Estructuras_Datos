# Gracida Tapia Bryan. 8
# 14 de octubre del 2024.
# Descripción:
# Practica de entrada por consolas y operaciones básicas.


# Declaramos nuestras variables.
primer_numero = input("Introduce un número decimal: ")      # Les agregamos un input para asi generar una entrada de datos por consola.
segundo_numero = input("Introduce otro número decimal: ")
# Convertimos los valores recibidos anteriormente en flotantes.
primer_float = float(primer_numero)
segundo_float = float(segundo_numero)

# Operaciones básicas.

resultado_float = primer_float + segundo_float # Operación de suma.
print()
print(" ****  Suma  ****")
print(f"El resultado de la suma de {primer_float} y {segundo_float} es: {resultado_float}")

resultado_float = primer_float - segundo_float # Operación de resta.
print()
print(" ****  Resta  ****")
print(f"El resultado de la resta de {primer_float} y {segundo_float} es: {resultado_float}")

resultado_float = primer_float * segundo_float # Operación de multiplicación.
print()
print(" ****  Multiplicacion  ****")
print(f"El resultado de la multiplicación de {primer_float} y {segundo_float} es: {resultado_float}")

resultado_float = primer_float / segundo_float # Operación de divición.
print()
print(" ****  División  ****")
print(f"El resultado de la división de {primer_float} y {segundo_float} es: {resultado_float:.2f}")     # En python untilizamos : :.(numero)f dependiendo, el número de decimales que queremos que nos muestre la variable

# En Python se pueden generar las operaciones básicas, ya sea asignando el valor de la operación a una variable
# También se puede haciendolo directo a la hora de impresión de la siguiente forma : {(n1+n2)}
