# Gracida Tapia Bryan.
# 25 de noviembre del 2024.
# Descripción:
# Programa que identifica cual es el número maximo y minimo de los números ingresados por el usuario.


# ///////////////////////////////////////////////////////////////////////////////////////// función menu

def menu():
    print(" *** Menú ***")
    print("1) Ver lista de números.")
    print("2) Añadir números a la lista.")
    print("3) Determinar el valor máximo y mínimo de la lista de números.")
    print("4) Salir.")
    opcion = int(input("Elija una opción: "))
    print()
    return opcion

# ///////////////////////////////////////////////////////////////////////////////////////// Función para encontrar los números máximo y mínimo
def determinar ():

    # ................................ Número Mínimo y Máximo
    numero_minimo = lista[0]
    numero_maximo = lista[0]
    if not lista:
        print("No hay números en la lista.")
    for det in lista:
        if numero_minimo >= det:
            numero_minimo = det
        if numero_maximo <= det:
            numero_maximo = det
    return numero_maximo,numero_minimo

# ///////////////////////////////////////////////////////////////////////////////////////// Código a nivel de módulo.
opcion = 0
lista = []
while opcion <= 6:
    opcion = menu()

    if opcion == 1:     # ................................ Mostrar lista
        if not lista:
            print("No hay números en la lista.")
        print("Lista:")
        for i,numero in enumerate(lista):
            print(f"{i+1}) {numero}")
        print()

    elif opcion == 2:   # ................................ Ingresar número
        numero = int(input("Ingresa un número: "))
        lista.append(numero)
        print(f"Número: {numero} añadido correctamente.")

    elif opcion == 3:   # ................................ Número Mínimo y Máximo
        maximo,minimo = determinar() # |-------------------------------| llamada a la función determinar
        print(f"El número máximo de la lista es: {maximo} \nEl número mínimo de la lista es: {minimo}")

    elif opcion == 6:   # ................................ Salir del programa
        print("Saliendo del programa...")

    else:
        print("Opción no válida, intenta de nuevo.")

    print()
    print("-----------------------------")
    print()