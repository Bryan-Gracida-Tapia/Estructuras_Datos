
# Gracida Tapia Bryan.
# 12 de septiembre del 2024.
# Descripción:
# Creacion de compras.


# COLA_FIFO: firs input firs ouput
# PILA_QUEUE_LIFO: last input firs ouput

# ///////////////////////////////////////////////////////////////////////////////////////// Funcion menú.
def menu():
    print(" *** Menú ***")
    print("1) Ver lista.")
    print("2) Añadir producto a la lista.")
    print("3) Añadir varios productos a la lista.")
    print("4) Eliminar producto de la lista.")
    print("5) Salir.")
    opcion = int(input("Elija una opción: "))
    print()
    return opcion
# ///////////////////////////////////////////////////////////////////////////////////////// Funcion asignacion.
def acciones(opcion):
    i = 0
    if opcion == 1:         # ................................ Imprimir la matriz.
        print("Lista:")
        for j in nombre_producto:
            print(f"{cantidad_producto[i]} | {nombre_producto}")
            i += 1
        i=0

    elif opcion == 2:       # ................................ Ingresar datos a la matriz.
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

    elif opcion == 4:       # ................................ Eliminar un producto de la lista.
        for nombre in nombre_producto:
            print(f"{i}) producto: {nombre_producto[i]}")
            i += 1
        eliminar = int(input("Ingrese el número del producto que desea eliminar: "))
        nombre_producto.pop(eliminar-1)
        cantidad_producto.pop(eliminar-1)
    elif opcion == 5:       # ................................ Salir del programa.
        print("Saliendo del programa")

    print()
# /////////////////////////////////////////////// Código a nivel de módulo
opcion = 0
nombre_producto=[]
cantidad_producto = []
while opcion != 7:
    opcion = menu()
    acciones(opcion)