
# Gracida Tapia Bryan.
# 12 de septiembre del 2024.
# Descripción:
# Creacion de compras.


# COLA_FIFO: firs input firs ouput
# PILA_QUEUE_LIFO: last input firs ouput
# /////////////////////////////////////////////////////////////////////////////////////////
# Primer ejercicio
# ///////////////////////////////////////////////////////////////////////////////////////// Funcion menu
def menu():
    print(" *** Menu ***")
    print("1) Ver lista.")
    print("2) Añadir producto a la lista.")
    print("3) Añadir varios productos a la lista.")
    print("4) Eliminar producto de la lista.")
    print("5) Salir.")
    opcion = int(input("Elija una opción: "))
    print()
    return opcion
# ///////////////////////////////////////////////////////////////////////////////////////// Funcion asignacion
def acciones(opcion):
    i = 0
# /////////////////////////////////////////////// Imprimir la matriz
    if opcion == 1: #
        print("Lista:")
        for j in nombre_producto:
            print(f"{cantidad_producto[i]} | {nombre_producto}")
            i += 1
        i=0
# /////////////////////////////////////////////// Ingresar datos a la matriz
    elif opcion == 2:
        producto = input("Ingrese el nombre del producto: ")
        nombre_producto.append(producto)
        producto = input("Ingrese la cantidad del producto: ")
        cantidad_producto.append(producto)

    elif opcion == 3:
        contador = int(input("Ingrese el número de producto se agregarán: "))
        while i <= contador:
            producto = input("Ingrese el nombre del producto: ")
            nombre_producto.append(producto)
            producto = input("Ingrese la cantidad del producto: ")
            cantidad_producto.append(producto)
            i += 1
        i=1
# /////////////////////////////////////////////// Eliminar datos de la matriz
    elif opcion == 4:
        for nombre in nombre_producto:
            print(f"{i}) producto: {nombre_producto[i]}")
            i += 1
        eliminar = int(input("Ingrese el número del producto que desea eliminar: "))
        nombre_producto.pop(eliminar-1)
        cantidad_producto.pop(eliminar-1)
    elif opcion == 5:
        print("Saliendo del programa")

    print()
# /////////////////////////////////////////////// Codigo principal
opcion = 0
nombre_producto=[]
cantidad_producto = []
while opcion != 7:
    opcion = menu()
    acciones(opcion)