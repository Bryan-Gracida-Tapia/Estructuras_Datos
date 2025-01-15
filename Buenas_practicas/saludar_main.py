# Gracida Tapia Bryan.
# 13 de Enero del 2025.
# Descripción:
import Saludar_modulo

# ///////////////////////////////////////////////////////////////////////////////////////// Función .
if __name__ == '__main__':
    print(__name__)
    print(Saludar_modulo.__name__)
    nombre = input("Ingresa tu nombre: ")
    Saludar_modulo.saludar(nombre)