# Gracida Tapia Bryan.
# 25 de noviembre del 2024.
# Creación de piramides mediante el triángulo elejido .



# ///////////////////////////////////////////////////////////////////////////////////////// Función menú.
def menu():
    print("     *** Menú ***")
    print("1) Triángulo rectángulo.")
    print("2) Triángulo rectángulo de cabeza.")
    print("3) Triángulo rectángulo de cabeza espejo.")
    print("4) Triángulo isoseles.")
    print("5) Salir.")
    print("Elija el triángulo que desea crear:")
    opcion = int(input())
    print()
    return opcion



# ///////////////////////////////////////////////////////////////////////////////////////// Función piramides.
def piramides (opcion):
    aux = 0
    numero_filas = int(input("Ingrese el número de filas que tenga el Triángulo: "))
    aux = numero_filas
    if opcion == 1:                     # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\  Triángulo rectangulo.
        print("     *** Triángulo rectángulo.  ***\n")
        contador = 0
        print("1)")
        print()
        for i in range(1, numero_filas + 1):
            asteriscos = "*" * i
            print(f"{asteriscos}", end="")
            print()
    elif opcion == 2:                   # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Triángulo rectangulo de cabeza.
        print("     *** Triángulo rectángulo de cabeza.  ***\n")
        print()
        for i in range(1, numero_filas + 1):
            asteriscos = "*" * numero_filas
            print(f"{asteriscos}", end="")
            numero_filas -= 1
            print()
        numero_filas = aux
    elif opcion == 3:                   # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Triángulo de cabeza espejo.
        print("     *** Triángulo rectángulo de cabeza espejo.  ***\n")
        print()
        for i in range(1, numero_filas + 1):
            tabulador = " " * i
            asteriscos = "*" * numero_filas
            print(f"{tabulador}{asteriscos}", end="")
            numero_filas -= 1
            print()
        numero_filas = aux
    elif opcion == 4:                   # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ Triángulo isoseles.
        print("     *** Triángulo  isoseles.  ***\n")
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
        print("Opción no valida")


# ///////////////////////////////////////////////////////////////////////////////////////// Código a nivel de módulo.

opcion = 0
while opcion != 5:

    opcion = menu()
    piramides(opcion)

    print()
    print("-----------------------------")
    print()