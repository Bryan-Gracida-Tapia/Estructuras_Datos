# Gracida Tapia Bryan.
# 16 de octubre del 2024.
# Descripción:
# Ejemplificacion de operadores logicos en Python.


#//////////////////////////////no///////////////////////////////////////////////////////////
# Primer ejercicio.
primer_respuesta = input("La compra fue mayor a $5000.00 ? : ")
segunda_respuesta = input("La compra fue a Meses sin Intereses : ")
valor_compra = int(primer_respuesta)
segundo_int = segunda_respuesta.lower()=="si"

print(f"Aplica bonificacion? {(valor_compra>= 5000) and segundo_int}")
