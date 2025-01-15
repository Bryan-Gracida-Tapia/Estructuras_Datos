# Gracida Tapia Bryan.
# 13 de Enero del 2025.
# Descripción:
# .
from Ciclos_python import Ciclos_ejercicio3_Calculadora

# ///////////////////////////////////////////////////////////////////////////////////////// Función menu.

if __name__ == '__main__':
    print(__name__)
    opcion = 0
    while opcion != 7:
        opcion = Ciclos_ejercicio3_Calculadora.menu()
        Ciclos_ejercicio3_Calculadora.calculadora(opcion)


