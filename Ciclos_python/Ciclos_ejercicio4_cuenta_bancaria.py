# Gracida Tapia Bryan.
# 25 de noviembre del 2024.
# Descripción:
# Banco.


# ///////////////////////////////////////////////////////////////////////////////////////// Función menú.
def menu():
    print("     *** Menu ***")
    print("1) Consultar saldo.")
    print("2) Ingresar dinero.")
    print("3) Retirar dinero.")
    print("4) Salir.")
    print("Elija una opción:")
    opcion = int(input())
    print()
    return opcion

# ///////////////////////////////////////////////////////////////////////////////////////// Código a nivel de modulo.
print("  *** BIENVENIDO AL BANCO AZTECA ***")

contador = 0
saldo = 0
while contador != 4:
    opcion = menu()

    if opcion == 1:     # \\\\\\\\\\\\\\\\\\\\\\\\\ Consultar saldo de la cuenta.
        if saldo == 0:
            print("Su cuenta esta vacia")
        else:
            print(f"El saldo actual de la cuenta es: {(saldo):.2f}")
        print()
    elif opcion == 2:       # \\\\\\\\\\\\\\\\\\\\\\\\\ Realizar un deposito a la cuenta.
        respuesta = float(input("Ingrese la cantidad del deposito: "))
        saldo += respuesta
        print(f"Se ha depositado de manera exitosa.")
        print()
    elif opcion == 3:       # \\\\\\\\\\\\\\\\\\\\\\\\\ Realizar un retiro de la cuenta.
        respuesta = float(input("Ingrese la cantidad del retiro: "))
        if respuesta <= saldo:
            saldo -= respuesta
            print(f"Retirado de manera exitosa.")
        else:
            print("saldo insuficiente, intente de nuevo")
        print()
    elif opcion == 4:       # \\\\\\\\\\\\\\\\\\\\\\\\\ Salir del programa.
        print("Vuelva pronto a su banco...")
    else:
        print("Opción no valida, intente de nuevo")

    print()
    print("-----------------------------")
    print()
