# Gracida Tapia Bryan.
# 02 de diciembre del 2024.
# Descripción:
# Rifa.

import random


# ///////////////////////////////////////////////////////////////////////////////////////// Función menú.
def menu():
    print(" ***  Menú  *** ")
    print("[1].- Ver correos de participantes.")
    print("[2].- Agregar correo de participante.")
    print("[3].- Eliminar correo de participante.")
    print("[4].- Seleccionar ganador.")
    print("[5].- Salir")
    opcion_elejida = int(input("Ingrese una opción: "))
    return opcion_elejida

# ///////////////////////////////////////////////////////////////////////////////////////// Función rifa.
def rifa(opcion):
    if opcion == 1:             # ................................ Ver correos de los participantes.
        if not conjunto_correos:
            print("Aún no hay elementos para mostrar ")
            return
        for correo in conjunto_correos:
            print(f"{correo}")
    elif opcion == 2:             # ................................ Agregar correo de participante.
        correo_ingresado = input("Ingrese correo del participante: ")
        conjunto_correos.add(correo_ingresado)
        print(f" Se añadió a {correo_ingresado} :) ")
    elif opcion == 3:             # ................................ Eliminar correo de un participante.
        if not conjunto_correos:
            print("Aún no hay elementos para mostrar ")
            return
        for correo in conjunto_correos: #Imprime los correos existentes
            print(f"{correo}")

        correo_elejido = input("Ingrese el correo del participante a eliminar: ")
        conjunto_correos.remove(correo_elejido)
        print(f"Se eliminó {correo_elejido}")
    elif opcion == 4:             # ................................ Selecccionar correo ganador.
        if not conjunto_correos:
            print("No hay elementos para mostrar ")
            return

        lista_correos = list(conjunto_correos)  # Se debe convertir a lista para usar la función random.choice
        print(f"El ganador es { random.choice(lista_correos)}")

    elif opcion == 5:             # ................................ Salir del programa.
        print("Saliendo del programa...")

    else:
        print("Opción no valida")


conjunto_correos = set() #Conjunto vacío
opcion = 0
print("     *** Rifa de una computadora  ***")
print()
while opcion != 5:
    opcion = menu() #Se manda a llamar a la función menú
    rifa(opcion) #Se manda a llamar la función rifa, para saber que acción debe hacer el programa

    print()
    print("-----------------------------")
    print()



