# Gracida Tapia Bryan.
# 28 de octubre del 2024.
# Descripción:
# Programa que imprime un ejemplo del ciclo while.


#/////////////////////////////////////////////////////////////////////////////////////////
# Primer ejercicio
print("  *** Programa que imprime un ciclo while ***")
numero = int(input("ingrese la cantidad de numeros a imprimir en consola: "))
print(f"La suma de 1 hasta el {numero} : ")
contador = 1
total = 0
while contador <= numero:
    total += contador
    contador +=1
print(f"{total}")
print("Fin de la cuenta")
#
# randint (primer numero,segundo numero)