# Gracida Tapia Bryan.
# 28 de octubre del 2024.
# Descripción:
# Programa que imprime un ejemplo del ciclo while.


#/////////////////////////////////////////////////////////////////////////////////////////
# Primer ejercicio
print("  *** Programa que imprime un ciclo while ***")
numero = int(input("ingrese la cantidad de numeros a imprimir en consola: "))
print(f"los numeros del 1 al {numero} son: ")
contador = 1
while contador <= numero:
    print(contador)
    contador +=1
print()
print("Fin de la cuenta")
#/////////////////////////////////////////////////////////////////////////////////////////
# Segundo ejercicio
print()
print(f"los numeros del 1 al {numero} son: ")
contador = 1
while contador <= numero:
    print(contador,end=" ")
    contador +=1
print()
print("Fin de la cuenta")
#/////////////////////////////////////////////////////////////////////////////////////////
# tercer ejercicio
print()
print(f"los numeros multiplos de 2 del 1 al {numero} son: ")
contador = 1

while contador <= numero:
    if (contador % 2) == 0:
        print(contador, end=" ")
    contador += 1
print("")
print("Fin de la cuenta")