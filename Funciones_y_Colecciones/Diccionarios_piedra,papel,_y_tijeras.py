# Gracida Tapia Bryan.
# 06 de Diciembre del 2024.
# Descripción:
# Creación del juego PIEDRA,PAPEL,TIJERAS, utilizando diccionarios.
import random


# ///////////////////////////////////////////////////////////////////////////////////////// Función menú.

def menu():
    print("\n** PIEDRA, PAPEL O TIJERAS **")
    print("[1].- Piedra.")
    print("[2].- Papel.")
    print("[3].- Tijeras.")
    print("[4].- Salir.")
    opcion_elejida = int(input("Elija una opción: "))
    print()
    return opcion_elejida

# ///////////////////////////////////////////////////////////////////////////////////////// Función eleciones.

def elecciones(opcion):
    if opcion == 1:                     # ................................ La opción elejida por el usuario vale PIEDRA.
        usuario = PIEDRA
    elif opcion == 2:                     # ................................ La opción elejida por el usuario vale PAPEL.
        usuario = PAPEL
    elif opcion == 3:                     # ................................ La opción elejida por el usuario vale TIJERAS.
        usuario = TIJERAS
    elif opcion == 4:                     # ................................ Salir del programa.
        print("Saliendo...")
    else:
        print("Opción no valida, intentelo de nuevo.")

    cpu = random.choice([PIEDRA, PAPEL, TIJERAS])      # CPU toma un valor aleatorio de la lista.

    print(f"Usuario: {usuario}")
    print(f"CPU: {cpu}")

    return usuario, cpu

# ///////////////////////////////////////////////////////////////////////////////////////// Función selecionar ganador.

def seleccionar_ganador(usuario, cpu):
    global puntos_jugador, puntos_cpu, puntos_empate            # Se usa la palabra reservada global  para acceder a las variables que se encuantran fuera de la función.

    piedra_papel_tijeras = { (PIEDRA, TIJERAS): JUGADOR,(PIEDRA, PAPEL): CPU,(TIJERAS, PAPEL): JUGADOR,(TIJERAS, PIEDRA): CPU,(PAPEL, PIEDRA): JUGADOR,(PAPEL, TIJERAS): CPU}       # Se declaran las condiciones en forma de dicionario.

    resultado = piedra_papel_tijeras.get((usuario, cpu), EMPATE)      # Se declara el ganador tomando en cuenta las condicones anteriores.

    if resultado == JUGADOR:            # ................................ Se actualizan los contadores según el resultado.
        puntos_jugador += 1         # Aumenta el contador de jugador
        print(JUGADOR)
    elif resultado == CPU:
        puntos_cpu += 1             # Aumenta el contador del CPU
        print(CPU)
    else:
        puntos_empate += 1          # Aumenta el contador de los Empates
        print(EMPATE)

# ///////////////////////////////////////////////////////////////////////////////////////// Código a nivel de módulo.

PIEDRA = "Piedra"
PAPEL = "Papel"
TIJERAS = "Tijeras"
JUGADOR = "Gana el jugador"
EMPATE = "Empate"
CPU = "Gana el CPU"


puntos_jugador = 0
puntos_cpu = 0
puntos_empate = 0


opcion = 0

while opcion != 4:
    opcion = menu()
    usuario, cpu = elecciones(opcion)
    seleccionar_ganador(usuario, cpu)

    print()
    print("-----------------------------")
    print()

    print(f"** Marcador**\nJugador: {puntos_jugador}, CPU: {puntos_cpu}, Empate: {puntos_empate}")
