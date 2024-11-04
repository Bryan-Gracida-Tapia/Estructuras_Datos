# Gracida Tapia Bryan.
# 29 de octubre del 2024.
# Descripción:
# Banco.


#/////////////////////////////////////////////////////////////////////////////////////////
# Primer ejercicio
print("  *** BIENVENIDO AL BANCO AZTECA ***")

contador = 0
saldo = 6800
while contador != 4:
    print("1) Consultar saldo.")
    print("2) Ingresar dinero.")
    print("3) Retirar dinero.")
    print("4) Salir.")
    print("Elija una opción:")
    opcion_elegida = int(input())
    print()

    if opcion_elegida == 1:
        print(f"El saldo actual de la cuenta es: {(saldo):.2f}")
        print()
    elif opcion_elegida == 2:
        respuesta = float(input("Ingrese la cantidad del deposito: "))
        saldo += respuesta
        print(f"Se ha depositado de manera exitosa.")
        print()
    elif opcion_elegida == 3:
        respuesta = float(input("Ingrese la cantidad del retiro: "))
        if respuesta <= saldo:
            saldo -= respuesta
            print(f"Retirado de manera exitosa.")
        else:
            print("saldo insuficiente, intente de nuevo")
        print()
    elif opcion_elegida == 4:
        contador = 4
        print("Vuelva pronto a su banco...")
    else:
        print("Opción no valida, intente de nuevo")
