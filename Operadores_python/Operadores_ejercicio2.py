# Gracida Tapia Bryan.
# 17 de octubre del 2024.
# Descripción:
# Ejemplificacion de operadores logicos en Python.


#//////////////////////////////no///////////////////////////////////////////////////////////
# Primer ejercicio.
primer_respuesta = input("Es profesor de la UNSIJ ? : ")
segunda_respuesta = input("Es estudiante de la UNSIJ ? : ")
primer_int = primer_respuesta.lower()== "si"
segundo_int = segunda_respuesta.lower()=="si"

print(f"Forma parte de la comunidad UNSIJ? {primer_int or segundo_int}")