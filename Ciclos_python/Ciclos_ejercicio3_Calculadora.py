# Gracida Tapia Bryan.
# 29 de octubre del 2024.
# Descripción:
# Calculadora basica.


#/////////////////////////////////////////////////////////////////////////////////////////
# Primer ejercicio
print("  *** CALCULADORA BÁSICA ***")
print("Elija una opcion")
contador = 0
while contador != 4:
    print("1) Suma.")
    print("2) Resta.")
    print("3) Multiplicación.")
    print("4) División.")
    print("5) División entera.")
    print("6) Potenciación.")
    print("7) Salir.")

    opcion_elegida = int(input())

    if opcion_elegida == 1:
        primer_numero = float(input("Ingrese el primer número: "))
        segundo_numero = float(input("Ingrese el segundo numero: "))

        print(f"La suma del número {primer_numero} y el número {segundo_numero} es: {(primer_numero + segundo_numero):.2f}")
        print()
    elif opcion_elegida == 2:
        primer_numero = float(input("Ingrese el primer número: "))
        segundo_numero = float(input("Ingrese el segundo número: "))

        print(f"La resta del número {primer_numero} y el número {segundo_numero} es: {(primer_numero - segundo_numero):.2f}")
        print()
    elif opcion_elegida == 3:
        primer_numero = float(input("Ingrese el primer número: "))
        segundo_numero = float(input("Ingrese el segundo número: "))

        print(f"La multiplicación del número {primer_numero} y el número {segundo_numero} es: {(primer_numero * segundo_numero):.2f}")
        print()
    elif opcion_elegida == 4:
        primer_numero = float(input("Ingrese el primer número: "))
        segundo_numero = float(input("Ingrese el segundo número: "))

        print(f"La división del número {primer_numero} y el número {segundo_numero} es: {(primer_numero / segundo_numero):.2f}")
        print()
    elif opcion_elegida == 5:
        primer_numero = float(input("Ingrese el primer número: "))
        segundo_numero = float(input("Ingrese el segundo número: "))

        print(f"La división entera del número {primer_numero} y el número {segundo_numero} es: {(primer_numero // segundo_numero):.2f}")
        print()
    elif opcion_elegida == 6:
        primer_numero = float(input("Ingrese el primer numero: "))
        segundo_numero = float(input("Ingrese el segundo numero: "))

        print(f"La potenciación del número {primer_numero} elevado a la {segundo_numero:.0f} potencia es: {(primer_numero ** segundo_numero):.2f}")
        print()
    elif opcion_elegida == 7:
        contador = 4
        print("Saliendo del programa...")
    else:
        print("Opcion no valida, intente de nuevo")

