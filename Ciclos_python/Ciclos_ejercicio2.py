# Gracida Tapia Bryan.
# 28 de octubre del 2024.
# Descripción:
# Programa que imprime un ejemplo del ciclo while.

#/////////////////////////////////////////////////////////////////////////////////////////
# Primer ejercicio
print("  *** Programa que realiza una suma acumulativa ***")
numero_inicial = int(input("ingrese el numero inicial: "))
numero_final = int(input("ingrese el numero final: "))
print(f"La suma acumulativa de {numero_inicial} hasta el {numero_final} es: ")
total = 0
while numero_inicial <= numero_final:
    total += numero_inicial
    numero_inicial +=1
print(f"{total}")
print("Fin de la cuenta")