# Gracida Tapia Bryan.
# 25 de noviembre del 2024.
# Descripción:
# Programa que imprime una piramide según el número que ingrese el usuario.


# for "variable" in secuencia
numero_piramide = int(input("Ingrese un número: "))
aux = numero_piramide
#/////////////////////////////////////////////////////////////////////////////////////////
# Primer ejercicio
contador=0
print("1)")
print()
for i in range(1,numero_piramide+1):
    asteriscos = "*" * i
    print(f"{asteriscos}",end="")
    print()
# /////////////////////////////////////////////////////////////////////////////////////////
# segundo ejercicio
print("2)")
print()
for i in range(1,numero_piramide+1):
    asteriscos = "*" * numero_piramide
    print(f"{asteriscos}",end="")
    numero_piramide -= 1
    print()
numero_piramide = aux
#/////////////////////////////////////////////////////////////////////////////////////////
# tercero ejercicio
print("3)")
print()
for i in range(1,numero_piramide+1):
    tabulador = " " * i
    asteriscos = "*" * numero_piramide
    print(f"{tabulador}{asteriscos}",end="")
    numero_piramide -= 1
    print()
numero_piramide = aux
#/////////////////////////////////////////////////////////////////////////////////////////
# cuarto ejercicio
print("4)")
print()
for i in range(1,aux+1):
    tabulador = " " * numero_piramide
    asteriscos = "*" * i
    print(f"{tabulador}{asteriscos}",end="")
    i -= 1
    asteriscos = "*" * i
    print(f"{asteriscos}")
    i +=1
    numero_piramide -= 1
    print()

