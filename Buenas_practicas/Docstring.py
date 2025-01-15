# Gracida Tapia Bryan.
# 09 de Enero del 2025.
# Descripción:
# .
import random
# ///////////////////////////////////////////////////////////////////////////////////////// Función menu.
def menu() -> int:
    """

    :return: retorna un valor entero según haya elegido el usuario
    """
    print("[1].- Convertir a entero")
    print("[2].- Convertir a flotante")
    print("[3].- Salir")
    opcion = int(input("Ingrese una opción: "))
    return opcion


# ///////////////////////////////////////////////////////////////////////////////////////// Función cadena entero.
def cadena_a_entero(cadena: str) -> int | None:
    """

    :param cadena: Es la cadena que se convertirá a un entero
    :return: El enetero o en caso de no tratarse de un número retorna un None
    """
    numero_guiones = cadena.count("-")
    revisar_cadena = cadena.lstrip("-")
    if revisar_cadena.isnumeric() and numero_guiones in (0, 1):
        return int(cadena)
    else:
        return None

# ///////////////////////////////////////////////////////////////////////////////////////// Función cadena decimal.
def cadena_a_flotante(cadena: str) -> float | None:
    numero_puntos = cadena.count(".")
    revisar_cadena = cadena.replace(".", "").lstrip("-")
    if revisar_cadena.isnumeric() and numero_puntos in (0, 1):
        return float(cadena)
    else:
        return None


# ///////////////////////////////////////////////////////////////////////////////////////// código a nivel de módulo.
print()
opcion = menu()
while opcion != 3:
    if int(opcion) == 1:
        num_cadena = input("Ingresa número a convertir: ")
        numero = cadena_a_entero(num_cadena)
    elif int(opcion) == 2:
        num_cadena = input("Ingresa el número a convertir: ")
        numero = cadena_a_flotante(num_cadena)
    else:
        print("Opción no válida. Intente de nuevo")
        opcion = menu()
        continue

    while numero is None:
        num_cadena = input("Opción no válida. Intente nuevamente: ")
        numero = cadena_a_entero(num_cadena) if int(opcion) == 1 else cadena_a_flotante(num_cadena)

    print(f"El número {numero} es de tipo {type(numero)}")

    print()
    print("-----------------------------")
    print()
