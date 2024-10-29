# Gracida Tapia Bryan.
# 17 de octubre del 2024.
# Descripción:
# Ejemplificación de operadores lógicos en Python.

#/////////////////////////////////////////////////////////////////////////////////////////
print("  *** Programa que determina si una persona pertenece a la UNSIJ ***")

primer_respuesta = input("Pertenece a la UNSIJ ? : ")        # Declaramos nuestras variables incluyendo input para la lectura por consola.
segunda_respuesta = input("Es estudiante de la UNSIJ ? : ")
tercer_respuesta = input("Es intendente de la UNSIJ ? : ")
cuarta_respuesta = input("Es profesor de la UNSIJ ? : ")

primer_respuesta = primer_respuesta.lower()== "si"           # Utilizamos la palabra reservada lower para comparar una cadena y saber si se cumple la condición.
segundo_respuesta = segunda_respuesta.lower()=="si"
tercer_respuesta = tercer_respuesta.lower()=="si"
cuarta_respuesta = cuarta_respuesta.lower()=="si"


print(f"Forma parte de la comunidad UNSIJ? {(primer_respuesta and segundo_respuesta) or (primer_respuesta and tercer_respuesta) or (primer_respuesta and cuarta_respuesta)}")
# Se debe cumplir con dos de las condiciones para que sea True por ellos se denota como ( (primer variable and otra variable) or (...)... )