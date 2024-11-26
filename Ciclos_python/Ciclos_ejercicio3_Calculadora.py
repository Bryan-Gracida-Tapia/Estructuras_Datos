# Gracida Tapia Bryan.
# 25 de noviembre del 2024.
# Descripción:
# Calculadora basica.



# ///////////////////////////////////////////////////////////////////////////////////////// Función menú.
def menu():
    print("     *** Menú ***")
    print("1) Suma.")
    print("2) Resta.")
    print("3) Multiplicación.")
    print("4) División.")
    print("5) División entera.")
    print("6) Potenciación.")
    print("7) Salir.")

    opcion = int(input("Elija una opción: "))
    print()
    return opcion


# ///////////////////////////////////////////////////////////////////////////////////////// Función calculadora.
def calculadora (opcion):
    primer_numero = float(input("Ingrese el primer número: "))
    segundo_numero = float(input("Ingrese el segundo numero: "))

    if opcion == 1:     # \\\\\\\\\\\\\\\\\\\\\\\\\ Suma.
        print(
            f"La suma del número {primer_numero} y el número {segundo_numero} es: {(primer_numero + segundo_numero):.2f}")
        print()
    elif opcion == 2:       # \\\\\\\\\\\\\\\\\\\\\\\\\ Resta.
        print(f"La resta del número {primer_numero} y el número {segundo_numero} es: {(primer_numero - segundo_numero):.2f}")
        print()
    elif opcion == 3:       # \\\\\\\\\\\\\\\\\\\\\\\\\ Multiplicación.
        print(f"La multiplicación del número {primer_numero} y el número {segundo_numero} es: {(primer_numero * segundo_numero):.2f}")
        print()
    elif opcion == 4:       # \\\\\\\\\\\\\\\\\\\\\\\\\ División.
        print(f"La división del número {primer_numero} y el número {segundo_numero} es: {(primer_numero / segundo_numero):.2f}")
        print()
    elif opcion == 5:       # \\\\\\\\\\\\\\\\\\\\\\\\\ División entera.
        print(f"La división entera del número {primer_numero} y el número {segundo_numero} es: {(primer_numero // segundo_numero):.2f}")
        print()
    elif opcion == 6:       # \\\\\\\\\\\\\\\\\\\\\\\\\ Potenciación.
        print(f"La potenciación del número {primer_numero} elevado a la {segundo_numero:.0f} potencia es: {(primer_numero ** segundo_numero):.2f}")
        print()
    elif opcion == 7:       # \\\\\\\\\\\\\\\\\\\\\\\\\ Salir del programa.
        print("Saliendo del programa...")
    else:
        print("Opcion no valida, intente de nuevo")


# ///////////////////////////////////////////////////////////////////////////////////////// Código a nivel de módulo.
opcion = 0
while opcion != 7:
    opcion = menu()
    calculadora(opcion)

    print()
    print("-----------------------------")
    print()


