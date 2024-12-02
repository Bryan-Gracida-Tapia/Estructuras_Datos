# Gracida Tapia Bryan.
# 25 de noviembre del 2024.
# Descripción:
# Creación de listas de alumnos y manipulación mediante el uso de bibliotecas.



# ///////////////////////////////////////////////////////////////////////////////////////// Función menú.
def menu():
    print("     *** Menú ***")
    print("1) Ver calificaciones de un alumno.")
    print("2) Ver promedios de los alumnos.")
    print("3) Añadir alumno.")
    print("4) Eliminar alumno.")
    print("5) Ver promedio grupal.")
    print("6) Salir.")
    opcion = int(input("Elija una opción: "))
    print()
    return opcion


# ///////////////////////////////////////////////////////////////////////////////////////// Función acción.
def accion(opcion):
    contador = 0
    if opcion == 1:                     # ................................ Ver todas las calificaciones de un alumno.
        if not alumnos:
            print("No hay alumnos registrados.")
            return
        print("Lista:")
        for alumno in alumnos: # Se imprimen todoss los alumnos existentes en forma de lista.
            print(f"{contador}) {alumno['nombre']}")
            contador += 1
        alumno_elejido = int(input("Ingrese el número del alumno a mostrar: "))
        alumno = alumnos[alumno_elejido-1]

        print(f"     ***{alumno['nombre']}***")
        print(f"Calificaciones:")
        print(f"Estructura de datos: {alumno['calificaciones']['Estructura de datos']}")
        print(f"Derecho y legislación: {alumno['calificaciones']['Derecho y legislación']}")
        print(f"Contabilidad General: {alumno['calificaciones']['Contabilidad General']}")
        print(f"Electrónica II: {alumno['calificaciones']['Electrónica II']}")
        print(f"Álgebra Lineal: {alumno['calificaciones']['Álgebra Lineal']}")
        print(f"Promedio: {sum(alumno['calificaciones'].values())/5}") # Se utiliza la palabra reservada .values() para extraer todas las calificaciones, y se utiliza la palabra reservada sum(), para realizar la suma de las calificaciones que extrae .values(), para despues dividirlo entre 5.
        print()
    elif opcion == 2:                   # ................................ Ver el promedio de cada alumno.
        contador = 0
        if not alumnos:
            print("No hay alumnos registrados.")
        for i in alumnos:
            alumno = alumnos[contador]
            promedio = sum(alumno['calificaciones'].values())/5 # Se utiliza la palabra reservada .values() para extraer todas las calificaciones, y se utiliza la palabra reservada sum(), para realizar la suma de las calificaciones que extrae .values(), para despues dividirlo entre 5.
            print(f"    ***{alumno['nombre']}***")
            print(f"Promedio: {promedio:.2f}")
            contador += 1

    elif opcion == 3:                   # ................................ Agregar a un alumno.
        nombre = input("Ingrese el nombre del nuevo alumno: ")
        materias = ["Estructura de datos", "Derecho y legislación", "Contabilidad General","Electrónica II", "Álgebra Lineal"]
        for materia in materias: # Se lee cada calificación en el orden de la lista  materias y se van guardando dentro de otra lista.
                calificacion = float(input(f"{materia}: "))
                calificaciones[materia] = calificacion

        alumnos.append({"nombre": nombre, "calificaciones": calificaciones})
        print(f"Alumno agregado correctamente.")

    elif opcion == 4:                    # ................................ Eliminar alumno.
        contador = 0
        if not alumnos:
            print("No hay alumnos registrados.")
        print("Lista de alumnos:")

        for alumno in alumnos: # Se imprimen todos los alumnos existentes en forma de lista.
            print(f"{contador}) {alumno['nombre']}")
            contador += 1

        alumno_elegido = int(input("Ingrese el número del alumno a eliminar: "))
        eliminado = alumnos.pop(alumno_elegido - 1)
        print(f"Alumno {eliminado['nombre']} eliminado correctamente.")



    elif opcion == 5:                   # ................................ Mostrar promedio grupal.
        total_calificaciones = 0
        contador = 0
        if not alumnos:
            print("No hay alumnos registrados.")
        for alumno in alumnos:
            total_calificaciones += sum(alumno['calificaciones'].values())/5 # Se utiliza la palabra reservada .values() para extraer todas las calificaciones, y se utiliza la palabra reservada sum(), para realizar la suma de las calificaciones que extrae .values(), para luego dividirlo entre las materias existentes
            contador +=1
        promedio_grupal = total_calificaciones / contador # El promedio grupal es el resultado de la suma del promedio final de cada alumno, entre los alumnos existentes.
        print(f"Promedio grupal: {promedio_grupal:.2f}")

    elif opcion == 6:
        print("Saliendo del programa...")


    else:
        print("Opción no válida...")


# ///////////////////////////////////////////////////////////////////////////////////////// Código a nivel de módulo.

alumnos = []
calificaciones = {}
opcion = 0
while opcion != 6:
    opcion = menu()
    accion(opcion)

    print()
    print("-----------------------------")
    print()


