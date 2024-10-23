# Gracida Tapia Bryan.
# 16 de octubre del 2024.
# Descripción:
# Ejemplificacion de operadores logicos en Python.


#//////////////////////////////no///////////////////////////////////////////////////////////
# Primer ejercicio.
primer_respuesta = int(input("La compra fue mayor a $5000.00 ? : "))
segunda_respuesta = input("La compra fue a Meses sin Intereses : ")
segundo_int = segunda_respuesta.lower()=="si"

print(f"Aplica bonificacion? {(primer_respuesta>= 5000) and segundo_int}")
