# Gracida Tapia Bryan.
# 15 de octubre del 2024.
# Descripción:
# Ejemplificación de los diferentes tipos de asignación.

primer_numero, segundo_numero = 10,5    # En python al momento de declarar se ponen primero las variables separadas por coma para después darles valor de igual manera
tercer_numero, cuarto_numero = 9.14, "chuy"     # Asignación múltiple
quinto_numero, sexto_numero = primer_numero + segundo_numero, primer_numero - segundo_numero
septimo_numero = octavo_numero = noveno_numero = 10     # Asignación encadenada
decimo_numero, onceavo_numero = "Alberto", "Geto"       # Intercambio de variable
onceavo_numero, decimo_numero = decimo_numero, onceavo_numero

print(primer_numero, tercer_numero, cuarto_numero, segundo_numero)

print(quinto_numero, sexto_numero)

print(septimo_numero, octavo_numero, noveno_numero)

print(decimo_numero, onceavo_numero)

nombre, apellido = input("Ingresa nombre: "), input("ingresa apellido: ")   # De igual manera ne python podemos pedir dos varibles y leerlas en consola solo separadas por coma.

print(nombre, apellido)