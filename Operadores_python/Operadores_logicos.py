# Gracida Tapia Bryan.
# 16 de octubre del 2024.
# Descripción:
# Ejemplificación de operadores lógicos en Python.


#/////////////////////////////////////////////////////////////////////////////////////////

primer_respuesta = input("Ingresa Si/No : ")        # Declaramos nuestras variables incluyendo input para la lectura por consola.
segunda_respuesta = input("Ingresa Si/No : ")
primer_int = primer_respuesta.lower()=="si"         # En python la palabra reservada lower convierte el contenido de una cadena en letras minúsculas.
segundo_int = segunda_respuesta.lower()=="si"       # Se denota como (variable = variable.lower()== "cadena a comparar") y lo que nos regresa en un True o False.

print(f"¿El valor de {primer_respuesta} es verdadero? {primer_int}.")
print(f"¿El valor de {primer_respuesta} es verdadero? {segundo_int}.")

print(f"Ambas son respuestas fueron si? {primer_int and segundo_int}")          # En python existen los operadores lógicos como AND, OR y NO.
print(f"Una respuesta fue si? {primer_int or segundo_int}")                     # Se denotan como (primer_variable  operador_lógico  segunda_varibale).
print(f"La primera respuesta fue si? { not segundo_int}")
print(f"La segunda respuesta fue si? { not primer_int}")