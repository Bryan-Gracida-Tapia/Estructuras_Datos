# Gracida Tapia Bryan.
# 25 de noviembre del 2024.
# Descripción:
# Lista de videos de youtube agregados.


# COLA_FIFO: firs input firs ouput
# PILA_QUEUE_LIFO: last input firs ouput

# ///////////////////////////////////////////////////////////////////////////////////////// Funcion menu
def menu():
    print(" *** Menú ***")
    print("1) Ver Lista de videos por añadidos.")
    print("2) Ver lista por orden A-Z.")
    print("3) Ver lista por orden Z-A.")
    print("4) Añadir video.")
    print("5) Añadir varios videos.")
    print("6) Eliminar videos.")
    print("7) Salir.")

    opcion = int(input("Elija una opción: "))

    return opcion


# ///////////////////////////////////////////////////////////////////////////////////////// Funcion acción
def accion (opcion):
    contador = 1
    if opcion == 1:  # \\\\\\\\\\\\\\\\\\\\\\\\\ Mostrar lista.
        if not videos:
            print("No hay videos agregados.")
            return
        print("Lista:")
        for video in videos:
            print(f"{contador}) {video}")
            contador += 1


    elif opcion == 2:   # \\\\\\\\\\\\\\\\\\\\\\\\\ Mostrar lista en orden alfabético.
        if not videos:
            print("No hay videos agregados.")
            return
        videos.sort()
        print("Lista A-Z:")
        for video in videos:
            print(f"{contador}) {video}")
            contador += 1


    elif opcion == 3:       # \\\\\\\\\\\\\\\\\\\\\\\\\ Mostrar lista en orden Z - A.
        if not videos:
            print("No hay videos agregados.")
            return
        videos.sort(reverse=True)
        print("Lista Z-A:")
        for video in videos:
            print(f"{contador}) {video}")
            contador += 1

    elif opcion == 4:       # \\\\\\\\\\\\\\\\\\\\\\\\\ Añadir un video.
        nombre_video = input("Ingrese el nombre del video: ")
        videos.append(nombre_video)

    elif opcion == 5:       # \\\\\\\\\\\\\\\\\\\\\\\\\ Añadir varios videos.
        cantidad_videos = int(input("Ingrese el número de videos que desea ingresar: "))
        while contador <= cantidad_videos:
            nombre_video = input(f"Ingrese el nombre del video {contador}: ")
            videos.append(nombre_video)
            contador += 1
        contador = 1

    elif opcion == 6:       # \\\\\\\\\\\\\\\\\\\\\\\\\ Eliminar un video.
        if not videos:
            print("\nNo hay videos agregados.")
            return
        for video in videos:
            print(f"{contador}) {video}")
            contador += 1
        eliminar = int(input("Ingrese el número del video que desea eliminar: "))
        videos.pop(eliminar - 1)

    elif opcion == 7:       # \\\\\\\\\\\\\\\\\\\\\\\\\ Salir del programa.
        print("Saliendo del programa")

    print()


# /////////////////////////////////////////////// Código a nivel de modulo
opcion = 0
i=0
videos = []
while opcion != 7:
    opcion = menu()
    accion(opcion)
    print()
    print("-----------------------------")
    print()
