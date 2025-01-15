# Gracida Tapia Bryan.
# 06 de Enero del 2025.
# Descripción:
# .
import random

# ///////////////////////////////////////////////////////////////////////////////////////// Función cadena entero.

def cadena_entero(cadena_ingresada):
    no_guion_es = cadena_ingresada.count("-")
    revisar_cadena = cadena_ingresada.lstrip("-")
    if revisar_cadena.isnumeric() and no_guion_es in (0,1):
        return int(cadena_ingresada)
    else:
        return None

# ///////////////////////////////////////////////////////////////////////////////////////// código a nivel de módulo.
cadena_ingresada = input("Ingresa Z: ")
numero = cadena_entero(cadena_ingresada)
while numero is None:
    print("Opción invalida")
    numero = cadena_entero(cadena_ingresada)
print(f"El número {numero} es de tipo {type(numero)}")
print()
cadena_ingresada = input("Ingrese una cadena: ").strip()
print(cadena_ingresada.isnumeric())
print(cadena_ingresada.isalpha())
print(cadena_ingresada.isalnum())
segundo_numero_ingresado = input("Ingrese un número: ")
while not segundo_numero_ingresado.isnumeric():
    print("Opción no válida")
    segundo_numero_ingresado = input("Intente nuevamente: ")
print()
segundo_numero_ingresado = int(segundo_numero_ingresado)
print(f"El número {segundo_numero_ingresado} es de tipo {type(segundo_numero_ingresado)}")