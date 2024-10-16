# Gracida Tapia Bryan.
# 16 de octubre del 2024.
# Descripción:
# Ejemplificacion de operadores racionales en Python los cuales se utilizan para comparar dos valores.


#/////////////////////////////////////////////////////////////////////////////////////////
# Primer ejercicio
# Declaramos nuestras variables.
primer_numero = input("Introduce un número decimal: ")
segundo_numero = input("Introduce otro número decimal: ")

primer_float = float(primer_numero)
segundo_float = float(segundo_numero)

print(f"El numero {primer_float:.2f} es mayor que {segundo_float:.2f}? {primer_float>segundo_float}")
print(f"El numero {primer_float:.2f} es mayor o igual que {segundo_float:.2f}? {primer_float>=segundo_float}")
print(f"los numeros {primer_float:.2f} y {segundo_float:.2f} son iguales? {primer_float==segundo_float}")
print(f"El numero {primer_float:.2f} es menor que {segundo_float:.2f}? {primer_float<segundo_float}")
print(f"El numero {primer_float:.2f} es menor o igual {segundo_float:.2f}? {primer_float<=segundo_float}")
print(f"El numero {primer_float:.2f} es diferente de {segundo_float:.2f}? {primer_float!=segundo_float}")