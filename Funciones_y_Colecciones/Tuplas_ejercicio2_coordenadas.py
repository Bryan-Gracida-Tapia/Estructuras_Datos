# Gracida Tapia Bryan.
# 25 de noviembre del 2024.
# Calculadora básica.



# ///////////////////////////////////////////////////////////////////////////////////////// Función menú.
def menu():
    print("     *** Menú ***")
    print("1) Ver coordenadas almacenadas.")
    print("2) Agregar coordenada (x,y).")
    print("3) Calcular la pendiente y la ecuación de la recta entre dos coordenadas.")
    print("4) Eliminar coordenada (x,y).")
    print("5) Salir.")
    print("Elija una opción:")
    opcion = int(input())
    print()
    return opcion



# ///////////////////////////////////////////////////////////////////////////////////////// Función acción.
def operacion (opcion):
    if opcion == 1:                     # ................................  Mostrar cordenadas existentes.
        contador = 1
        if not cordenadas:
            print("No hay cordenadas registradas.")
            return
        print("Lista:")
        for cordenada in cordenadas:  # Se imprimen todas las cordenadas existentes en forma de lista.
            print(f"{contador}) Eje X: {cordenada['cordenadas']['Eje X']}",end="")
            print(f"  Eje Y: {cordenada['cordenadas']['Eje Y']}")

            contador += 1
    elif opcion == 2:                   # ................................ Agregar cordenadas.
        x = float(input("Eje X: "))
        y = float(input("Eje Y: "))

        punto = {"cordenadas": {"Eje X": x, "Eje Y": y}}
        cordenadas.append(punto)

        print("Coordenada agregada correctamente.")

    elif opcion == 3:                   # ................................ Calcular la pendiente y la expresión de la recta.
        # |-------------------------------| Selección de las cordenadas.
        contador = 1
        if not cordenadas:
            print("No hay cordenadas registradas.")
            return
        print("Lista:")

        for punto in cordenadas:  # Se imprimen todas las cordenadas existentes en forma de lista.
            print(f"{contador}) {punto['cordenadas']}")
            contador += 1
        primera_cordenada = int(input("Ingrese el indice de la cordenada 1: "))
        segunda_cordenada = int(input("Ingrese el indice de la cordenada 2: "))
        cordenada_1 = cordenadas[primera_cordenada - 1]['cordenadas']
        cordenada_2 = cordenadas[segunda_cordenada - 1]['cordenadas']

        # |-------------------------------| Asignación de ejes correspondientes a las cordenadas.
        x1, y1 = cordenada_1['Eje X'], cordenada_1['Eje Y']
        x2, y2 = cordenada_2['Eje X'], cordenada_2['Eje Y']
        pendiente = ((y2 - y1) / (x2 - x1))
        b = y1 - pendiente * x1
        print(f"Expresión de la recta vale: y = {pendiente:.2f} x + {b}")

    elif opcion == 4:                   # ................................ Eliminar cordenada.
        contador = 1
        if not cordenadas:
            print("No hay cordenadas registradas.")
            return
        print("Lista:")

        for punto in cordenadas:  # Se imprimen todas las cordenadas existentes en forma de lista.
            print(f"{contador}) {punto['cordenadas']}")
            contador += 1
        cordenada_elegida = int(input("Ingrese el número del alumno a eliminar: "))
        cordenadas.pop(cordenada_elegida - 1)
        print(f"Cordenada eliminada correctamente.")
    elif opcion == 5:                   # ................................ Salir del programa.
        print("Saliendo del programa...")

    else:
        print("Opción no valida, intente de nuevo")


# ///////////////////////////////////////////////////////////////////////////////////////// Código a nivel de módulo.

print("     *** Rectas a partir de puntos (coordenadas) en el plano cartesiano  ***")
opcion = 0
cordenadas = []
puntos = {}
while opcion != 5:

    opcion = menu()
    operacion(opcion)

    print()
    print("-----------------------------")
    print()

