# Gracida Tapia Bryan.
# 6 de noviembre del 2024.
# Descripción:
# Programa que imprime una piramide segun el numero que ingrese el usuario.


# for "variable" in secuencia
#/////////////////////////////////////////////////////////////////////////////////////////
# Primer ejercicio
numero_piramide = int(input("ingrese un numero: "))
aux = numero_piramide
contador=0
print("1)")
print()
for i in range(1,numero_piramide):
    asteriscos = "*" * i
    print(f"{asteriscos}",end="")
    print()
# /////////////////////////////////////////////////////////////////////////////////////////
# segundo ejercicio
print("2)")
print()
for i in range(1,numero_piramide):
    asteriscos = "*" * numero_piramide
    print(f"{asteriscos}",end="")
    numero_piramide -= 1
    print()
numero_piramide = aux
#/////////////////////////////////////////////////////////////////////////////////////////
# tercero ejercicio
print("3)")
print()
for i in range(1,numero_piramide):
    tabulador = " " * i
    asteriscos = "*" * numero_piramide
    print(f"{tabulador}{asteriscos}",end="")
    numero_piramide -= 1
    print()
#/////////////////////////////////////////////////////////////////////////////////////////
# cuarto ejercicio
print("3)")
print()
for i in range(1,numero_piramide):
    tabulador = " " * i
    asteriscos = "*" * numero_piramide
    print(f"{tabulador}{asteriscos}",end="")
    numero_piramide -= 1
    print()
