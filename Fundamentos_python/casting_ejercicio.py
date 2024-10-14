# Gracida Tapia Bryan
# 13 de octubre del 2024
# Descripción:
# En el siguiente archivo pondremos en practica lo visto en conversión de tipos de datos(casting).

# //////////////////////////////////////////////////////////////////////////////////////////
# a)
# *****   Conversión de número a cadena     *****
primer_numero = 3.14159265
segundo_numero = 12
tercer_numero = 0

# *****   Impresión de las converciones mediante letreros     *****
print()
print("Conversión de número a cadena.")
print()
print(f"El número {primer_numero} se convierte a cadena  str(primer_numero): {str(primer_numero)}")
print(f"El número {segundo_numero} se convierte a cadena  str(segundo_numero): {str(segundo_numero)}")
print(f"El número {tercer_numero} se convierte a cadena  str(tercer_numero): {str(tercer_numero)}")

# //////////////////////////////////////////////////////////////////////////////////////////
# b)
# *****   Representación de los valores anteriores indicando su valor booleano     *****
print()
print("Conversión a booleanos.")
print()

valor_booleano = bool(primer_numero)
print(f"¿El valor de {primer_numero} es verdadero? {valor_booleano}.")

valor_booleano = bool(segundo_numero)
print(f"¿El valor de {segundo_numero} es verdadero? {valor_booleano}.")

valor_booleano = bool(tercer_numero)
print(f"¿El valor de {tercer_numero} es verdadero? {valor_booleano}.")

# //////////////////////////////////////////////////////////////////////////////////////////
# c)
# *****   Conversión de cadena a entero     *****
primer_numero = "100.02"
primer_numero_float = float(primer_numero)

segundo_numero = "10002"
segundo_numero_int = int(segundo_numero)

tercer_numero = "0"
tercer_numero_int = int(tercer_numero)

# *****   Impresión de las converciones mediante letreros     *****
print()
print("Conversión de cadena a numero.")
print()

print("Conversión de cadena a flotante.")
print(f"Número como cadena: {primer_numero_float}.")

print("Conversión de cadena a entero.")
print(f"Número como cadena: {segundo_numero_int}.")

print("Conversión de cadena a entero.")
print(f"Número como cadena: {tercer_numero_int}.")

# //////////////////////////////////////////////////////////////////////////////////////////
# d)
# *****   Representación de los valores anteriores indicando su valor booleano     *****
print()
print("Conversión a booleanos.")
print()

valor_booleano = bool(primer_numero_float)
print(f"¿El valor de {primer_numero_float} es verdadero? {valor_booleano}.")

valor_booleano = bool(segundo_numero_int)
print(f"¿El valor de {segundo_numero_int} es verdadero? {valor_booleano}.")

valor_booleano = bool(tercer_numero_int)
print(f"¿El valor de {tercer_numero_int} es verdadero? {valor_booleano}.")
print("Debido a que las únicas condiciónes para que sea False son que el valor sea 0, el contenido de nuestra variable este vacía o que el valor sea None.")