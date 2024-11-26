# Gracida Tapia Bryan.
# 25 de noviembre del 2024.
# Descripción:
# Programa que imprime una piramide según el número que ingrese el usuario.

# ///////////////////////////////////////////////////////////////////////////////////////// Función menú.
def menu():
    print("     *** Menú ***")
    print("1) Triangulo rectangulo.")
    print("2) triangulo rectangulo de cabeza.")
    print("3) Triangulo rectangulo de cabeza espejo.")
    print("4) Triangulo isoseles.")
    print("5) Salir.")
    print("Elija una opción:")
    opcion = int(input())
    print()
    return opcion


def piramides(opcion):
    aux = 0
    numero_filas = int(input("Ingrese el número de filas que tenga el triangulo: "))
    aux = numero_piramide
# for "variable" in secuencia
numero_filas = int(input("Ingrese un número: "))
piramides(opcion)
aux = numero_piramide
#/////////////////////////////////////////////////////////////////////////////////////////
# Triangulo rectangulo
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
# Tirangulo equilatero
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