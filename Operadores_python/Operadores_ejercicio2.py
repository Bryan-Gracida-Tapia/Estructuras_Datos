# Gracida Tapia Bryan.
# 17 de octubre del 2024.
# Descripción:
# Ejemplificación de operadores logicos en Python.


#/////////////////////////////////////////////////////////////////////////////////////////
print("  *** Programa que determina si un usuario es profesor o estudiante ***")

primer_respuesta = input("Es profesor de la UNSIJ ? : ")        # Declaramos nuestras variables incluyendo input para la lectura por consola.
segunda_respuesta = input("Es estudiante de la UNSIJ ? : ")
primer_int = primer_respuesta.lower()== "si"                    # Utilizamos la palabra reservada lower para comparar una cadena y saber si se cumple la condición.
segundo_int = segunda_respuesta.lower()=="si"

print(f"Forma parte de la comunidad UNSIJ? {primer_int or segundo_int}")    # En caso  de que las una de las condiciones sea verdadera sera True para ello se utiliza el operador lógico OR.