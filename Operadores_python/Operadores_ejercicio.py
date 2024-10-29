# Gracida Tapia Bryan.
# 16 de octubre del 2024.
# Descripción:
# Práctica de operadores lógicos y racionales en Python.


#/////////////////////////////////////////////////////////////////////////////////////////
print("  *** Programa que determina si se aplica una bonificación ***")

primer_respuesta = int(input("La compra fue mayor a $5000.00 ? : "))    # Declaramos nuestras variables incluyendo input para la lectura por consola a la vez que realizamos el casting necesario.
segunda_respuesta = input("La compra fue a Meses sin Intereses : ")
segundo_int = segunda_respuesta.lower()=="si"                           # Utilizamos la palabra reservada lower para comparar una cadena y saber si se cumple la condición.

print(f"Aplica bonificación? {(primer_respuesta>= 5000) and segundo_int}")  # En caso de que las las dos condiciones sean verdaderas la respuesta sera un True para ello utilizamos el operador lógico AND.
