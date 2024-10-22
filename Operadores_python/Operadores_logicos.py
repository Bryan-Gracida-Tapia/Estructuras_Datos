# Gracida Tapia Bryan.
# 16 de octubre del 2024.
# Descripción:
# Ejemplificacion de operadores logicos en Python.


#/////////////////////////////////////////////////////////////////////////////////////////
# Primer ejercicio.
primer_respuesta = input("Ingresa Si/No : ")
segunda_respuesta = input("Ingresa Si/No : ")
primer_int = primer_respuesta.lower()=="si"
segundo_int = segunda_respuesta.lower()=="si"

print(f"¿El valor de {primer_respuesta} es verdadero? {primer_int}.")
print(f"¿El valor de {primer_respuesta} es verdadero? {segundo_int}.")

print(f"Ambas son respuestas fueron si? {primer_int and segundo_int}")
print(f"Una respuesta fue si? {primer_int or segundo_int}")
print(f"La primera respuesta fue si? { not segundo_int}")
print(f"La segunda respuesta fue si? { not primer_int}")