# Gracida Tapia Bryan.
# 16 de octubre del 2024.
# Descripción:
# Ejemplificación de operadores racionales en Python los cuales se utilizan para comparar dos valores.


#/////////////////////////////////////////////////////////////////////////////////////////
# Primer ejercicio

primer_numero = input("Introduce un número decimal: ")          # Declaramos nuestras variables incluyendo input para la lectura por consola.
segundo_numero = input("Introduce otro número decimal: ")

primer_float = float(primer_numero)                             # Se realiza el casting debido para una mejor manipulación de las variabes.
segundo_float = float(segundo_numero)
# En pyhton tenemos distintos tipos de operadores racionales como:
print(f"El numero {primer_float:.2f} es mayor que {segundo_float:.2f}? {primer_float>segundo_float}")           #   Mayor que (>)
print(f"El numero {primer_float:.2f} es mayor o igual que {segundo_float:.2f}? {primer_float>=segundo_float}")  #   Mayor o igual que (>=)
print(f"los numeros {primer_float:.2f} y {segundo_float:.2f} son iguales? {primer_float==segundo_float}")       #   Igual que (==)
print(f"El numero {primer_float:.2f} es menor que {segundo_float:.2f}? {primer_float<segundo_float}")           #   Menor que (<=)
print(f"El numero {primer_float:.2f} es menor o igual {segundo_float:.2f}? {primer_float<=segundo_float}")      #   Menor o igual que (<=)
print(f"El numero {primer_float:.2f} es diferente de {segundo_float:.2f}? {primer_float!=segundo_float}")       #   Diferentre de (!=)