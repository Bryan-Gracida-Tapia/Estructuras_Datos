# Gracida Tapia Bryan.
# 12 de septiembre del 2024.
# Descripción:
# Creaciones de listas.

# COLA_FIFO: firs input firs ouput
# PILA_QUEUE_LIFO: last input firs ouput
# /////////////////////////////////////////////////////////////////////////////////////////
# Primer ejercicio
# ///////////////////////////////////////////////////////////////////////////////////////// Funcion menu
def menu():
    print(" *** Menu ***")
    print("1) Ver Lista de videos por añadidos.")
    print("2) Ver lista por orden A-Z.")
    print("3) Ver lista por orden Z-A.")
    print("4) Añadir video.")
    print("5) Añadir varios videos.")
    print("6) Eliminar videos.")
    print("7) Salir.")
    opcion = int(input("Elija una opción: "))
    print()
    return opcion
# ///////////////////////////////////////////////////////////////////////////////////////// Funcion asignacion
def asignaciones(opcion,videos):
    i = 1
    if opcion == 1:
        print("Lista:")
        print(videos)
    elif opcion == 2:
        videos.sort()
        print("Lista A-Z:")
        print(videos)
    elif opcion == 3:
        videos.sort(reverse= True)
        print("Lista Z-A:")
        print(videos)

    elif opcion == 4:
        nombre_video = input("Ingrese el nombre del video: ")
        videos.append(nombre_video)

    elif opcion == 5:
        contador = int(input("Ingrese el número de videos que desea ingresar: "))
        while i <= contador:
            nombre_video = input(f"Ingrese el nombre del video {i}: ")
            videos.append(nombre_video)
            i += 1
        i=1
    elif opcion == 6:
        for videos in videos:
            print(f"{i}) {videos}")
            i += 1
        eliminar = int(input("Ingrese el numero del video que desea eliminar: "))
        del videos[eliminar-1]
    elif opcion == 7:
        print("Saliendo del programa")
        return opcion
    print()
    return videos

opcion = 0
videos = []
while opcion != 7:
    opcion = menu()
    videos = asignaciones(opcion,videos)