# Gracida Tapia Bryan.
# 15 de octubre del 2024.
# Descripción:
# Ejemplificacion de los diferentes tipos de asignacion.

primer_numero, segundo_numero = 10,5 # En python al momento de declarar se ponen primero las variables separadas por coma para despues darles valor de igual manera
tercer_numero, cuarto_numero = 9.14, "chuy"     # Asignacion múltiple
quinto_numero, sexto_numero = primer_numero + segundo_numero, primer_numero - segundo_numero
septimo_numero = octavo_numero = noveno_numero = 10     # Asignacion encadenada
decimo_numero, onceavo_numero = "Alberto", "Geto"       # Intercambio de variable
onceavo_numero, decimo_numero = decimo_numero, onceavo_numero

print(primer_numero, tercer_numero, cuarto_numero, segundo_numero)

print(quinto_numero, sexto_numero)

print(septimo_numero, octavo_numero, noveno_numero)

print(decimo_numero, onceavo_numero)

nombre, apellido = input("Ingresa nombre: "), input("ingresa apellido: ")

print(nombre, apellido)