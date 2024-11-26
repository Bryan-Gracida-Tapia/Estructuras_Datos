# Gracida Tapia Bryan.
# 25 de noviembre del 2024.
# Expresión de la recta mediante cordenadas especificas.



# ///////////////////////////////////////////////////////////////////////////////////////// Función menú.
def menu():
    print("     *** Menú ***")
    print("1) Triangulo rectangulo.")
    print("2) Triangulo rectangulo de cabeza.")
    print("3) Triangulo rectangulo de cabeza espejo.")
    print("4) Triangulo isoseles.")
    print("5) Salir.")
    print("Elija el triangulo que desea crear:")
    opcion = int(input())
    print()
    return opcion



# ///////////////////////////////////////////////////////////////////////////////////////// Función piramides.
def piramides (opcion):
    aux = 0
    numero_filas = int(input("Ingrese el número de filas que tenga el triangulo: "))
    aux = numero_filas
    if opcion == 1:                     # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\  Triangulo rectangulo.
        print("     *** Triangulo rectangulo.  ***\n")
        contador = 0
        print("1)")
        print()
        for i in range(1, numero_filas + 1):
            asteriscos = "*" * i
            print(f"{asteriscos}", end="")
            print()
    elif opcion == 2:                   # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Triangulo rectangulo de cabeza.
        print("     *** triangulo rectangulo de cabeza.  ***\n")
        print()
        for i in range(1, numero_filas + 1):
            asteriscos = "*" * numero_filas
            print(f"{asteriscos}", end="")
            numero_filas -= 1
            print()
        numero_filas = aux
    elif opcion == 3:                   # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Triangulo de cabeza espejo.
        print("     *** Triangulo rectangulo de cabeza espejo.  ***\n")
        print()
        for i in range(1, numero_filas + 1):
            tabulador = " " * i
            asteriscos = "*" * numero_filas
            print(f"{tabulador}{asteriscos}", end="")
            numero_filas -= 1
            print()
        numero_filas = aux
    elif opcion == 4:                   # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Triangulo isoseles.
        print("     *** Triangulo rectangulo isoseles.  ***\n")
        for i in range(1, aux + 1):
            tabulador = " " * numero_filas
            asteriscos = "*" * i
            print(f"{tabulador}{asteriscos}", end="")
            i -= 1
            asteriscos = "*" * i
            print(f"{asteriscos}")
            i += 1
            numero_filas -= 1
            print()
    elif opcion == 5:                   # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Salir del programa.
        print("Saliendo del programa...")

    else:
        print("Opción no valida, intente de nuevo")


# ///////////////////////////////////////////////////////////////////////////////////////// Código a nivel de módulo.

opcion = 0
while opcion != 5:

    opcion = menu()
    piramides(opcion)

    print()
    print("-----------------------------")
    print()