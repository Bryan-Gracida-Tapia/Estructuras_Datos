# Gracida Tapia Bryan.
# 12 de septiembre del 2024.
# Descripción:
# Creaciones de listas.
from numpy.random import poisson


# COLA_FIFO: firs input firs ouput
# PILA_QUEUE_LIFO: last input firs ouput
# /////////////////////////////////////////////////////////////////////////////////////////
# Primer ejercicio
# ///////////////////////////////////////////////////////////////////////////////////////// Funcion menu
def menu():
    print(" *** Menu ***")
    print("1) Ver calificaciones de un alumno.")
    print("2) Ver promedios de los alumnos.")
    print("3) Añadir alumno.")
    print("4) Eliminar alumno.")
    print("5) Ver promedio grupal.")
    print("6) Salir.")
    opcion = int(input("Elija una opción: "))
    print()
    return opcion


# ///////////////////////////////////////////////////////////////////////////////////////// Funcion acción
def accion(opcion):
    contador = 0
    if opcion == 1: # \\\\\\\\\\\\\\\\\\\\\\\\\ Mostrar lista
        if not alumnos:
            print("No hay alumnos registrados.")
        print("Lista:")
        for i,alumno in enumerate(alumnos):
            print(f"{i+1}) {alumno['nombre']}")

        alumno_elejido = int(input("Ingrese el número del alumno a mostrar: "))

        alumno = alumnos[alumno_elejido-1]
        posicion = (alumno_elejido-1) * 5
        print(f"     ***{alumno['nombre']}***")
        print(f"Calificaciones:")
        print(f"Estructura de datos: {alumno['calificaciones'][posicion+1]}")
        print(f"Derecho y legislación: {alumno['calificaciones'][posicion+2]}")
        print(f"Contabilidad General: {alumno['calificaciones'][posicion+3]}")
        print(f"Electronica II: {alumno['calificaciones'][posicion+4]}")
        print(f"Algebra Lineal: {alumno['calificaciones'][posicion+5]}")
        print(f"Promedio: {(alumno['calificaciones'][posicion+1]+alumno['calificaciones'][posicion+2]+alumno['calificaciones'][posicion+3]+alumno['calificaciones'][posicion+4]+alumno['calificaciones'][posicion+5]) / 5}")
        print()

    elif opcion == 2: # \\\\\\\\\\\\\\\\\\\\\\\\\ Mostrar promedios
        if not alumnos:
            print("No hay alumnos registrados.")
        contador =0
        for i in alumnos:
            posicion = (contador)*5
            alumno = alumnos[contador]
            promedio = ((alumno['calificaciones'][posicion+1]+alumno['calificaciones'][posicion+2]+alumno['calificaciones'][posicion+3]+alumno['calificaciones'][posicion+4]+alumno['calificaciones'][posicion+5])/5)
            print(f"    ***{alumno['nombre']}***")
            print(f"Promedio: {promedio:.2f}")
            contador+=1

    elif opcion == 3: # \\\\\\\\\\\\\\\\\\\\\\\\\ Ingresar alumno
        nombre = input("Ingresa el nombre del nuevo alumno: ")

        print(f"Estructura de datos: ",end="")
        calificacion = int(input(""))
        calificaciones.append(calificacion)
        print(f"\nDerecho y legislación: ",end="")
        calificacion = int(input(""))
        calificaciones.append(calificacion)
        print(f"\nContabilidad General: ",end="")
        calificacion = int(input(""))
        calificaciones.append(calificacion)
        print(f"\nElectronica II: ",end="")
        calificacion = int(input(""))
        calificaciones.append(calificacion)
        print(f"\nAlgebra Lineal: ",end="")
        calificacion = int(input(""))
        calificaciones.append(calificacion)

        alumnos.append({"nombre": nombre,"calificaciones":calificaciones})
        print(f"Alumno {nombre} añadido.")

    elif opcion == 4: # \\\\\\\\\\\\\\\\\\\\\\\\\ eliminar alumno
        if not alumnos:
            print("No hay alumnos registrados.")
        for i, alumno in enumerate(alumnos):
            print(f"{i + 1}) {alumno['nombre']}")
        alumno_elejido = int(input("Ingrese el número del alumno a eliminar: "))
        eliminar = alumnos[alumno_elejido - 1]
        posicion = (alumno_elejido - 1) * 5
        alumnos.pop(eliminar['nombre'])
        alumnos.pop(eliminar['calificaciones'][posicion+1])
        alumnos.pop(eliminar['calificaciones'][posicion+2])
        alumnos.pop(eliminar['calificaciones'][posicion + 3])
        alumnos.pop(eliminar['calificaciones'][posicion + 4])


    elif opcion == 5: # \\\\\\\\\\\\\\\\\\\\\\\\\ Mostrar promedio grupal
        if not alumnos:
            print("No hay alumnos registrados.")
        for alumno in alumnos:
            suma_total = sum(sum(alumno["calificaciones"]))
        for alumno in alumnos:
            total_calificaciones = sum(len(alumno["calificaciones"]))
        promedio_grupal = suma_total / total_calificaciones
        print(f"Promedio grupal: {promedio_grupal:.2f}")

    elif opcion == 6:
        print("Saliendo del programa...")


    else:
        print("Opción no válida, intenta de nuevo.")




# # \\\\\\\\\\\\\\\\\\\\\\\\\ programa principal
opcion = 0
alumnos = []
calificaciones = [0]
while opcion <= 5:
    opcion = menu()
    accion(opcion)
