# Gracida Tapia Bryan.
# 6 de noviembre del 2024.
# Descripción:
# Programa que ejemplifica un ciclo for.

# for "variable" in secuencia
#/////////////////////////////////////////////////////////////////////////////////////////
# Primer ejercicio
cadena_usuario = input("ingrese una cadena: ")
contador = 0
for caracter in cadena_usuario:
    print(caracter, end="-")
    contador += 1
print()
print(contador)
print()
#/////////////////////////////////////////////////////////////////////////////////////////
# Segundo ejercicio
alumnos = ["Rosalinda", "Juan", "Lourdes", "Tania", "Bryan", "Rebeca", "Jennifer", "Hector", "Galilea", "Patricia", "Jesus", "Addi"]
contador = 0
for alumnos in alumnos:
    print(f"Hola {alumnos}", end=" ")
    print()
print()
#/////////////////////////////////////////////////////////////////////////////////////////
# tercer ejercicio
numero_ususario = int(input("Hasta que numero desea contar: "))
contador = 0
for i in range(1,numero_ususario+1):
    print(i, end=",")
print()
