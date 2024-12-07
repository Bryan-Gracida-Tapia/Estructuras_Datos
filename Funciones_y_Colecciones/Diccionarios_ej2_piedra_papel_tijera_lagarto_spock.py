import random


# ///////////////////////////////////////////////////////////////////////////////////////// Función menú.

def menu():
    print("\n** PIEDRA, PAPEL, TIJERAS, LAGARTO, SPOCK **")
    print("[1].- Piedra")
    print("[2].- Papel")
    print("[3].- Tijeras")
    print("[4].- Lagarto")
    print("[5].- Spock")
    print("[6].- Salir")
    opcion_elejida = int(input("Elija una opción: "))
    print()
    return opcion_elejida


# ///////////////////////////////////////////////////////////////////////////////////////// Función eleciones.

def elecciones(opcion):
    if opcion == 1:                     # ................................ La opción elejida por el usuario vale PIEDRA.
        eleccion_usuario = PIEDRA
    elif opcion == 2:                     # ................................ La opción elejida por el usuario vale PAPEL.
        eleccion_usuario = PAPEL
    elif opcion == 3:                     # ................................ La opción elejida por el usuario vale TIJERAS.
        eleccion_usuario = TIJERAS
    elif opcion == 4:                     # ................................ La opción elejida por el usuario vale LAGARTO.
        eleccion_usuario = LAGARTO
    elif opcion == 5:                     # ................................ La opción elejida por el usuario vale SPOCK.
        eleccion_usuario = SPOCK
    elif opcion == 6:                     # ................................ Salir del programa.
        print("Saliendo...")
    else:
        print("Opción no valida, intentelo de nuevo.")

    eleccion_cpu = random.choice([PIEDRA, PAPEL, TIJERAS, LAGARTO, SPOCK])      # Elección CPU toma un valor aleatorio de la lista.

    print(f"Usuario: {eleccion_usuario}")
    print(f"CPU: {eleccion_cpu}")

    return eleccion_usuario, eleccion_cpu

# ///////////////////////////////////////////////////////////////////////////////////////// Función selecionar ganador.

def seleccionar_ganador(eleccion_usuario, eleccion_cpu):
    global puntos_jugador, puntos_cpu, puntos_empate            # Se usa la palabra reservada global  para acceder a las variables que se encuantran fuera de la función.


    # Se declaran las condiciones en forma de dicionario.
    condiciones = {(PIEDRA, TIJERAS): JUGADOR,(PIEDRA, LAGARTO): JUGADOR,(PAPEL, SPOCK): JUGADOR,(PIEDRA, SPOCK): CPU,(TIJERAS, LAGARTO): JUGADOR,(LAGARTO, SPOCK): JUGADOR,(LAGARTO, PAPEL): JUGADOR,(SPOCK, TIJERAS): JUGADOR,(SPOCK, PIEDRA): JUGADOR,(PIEDRA, PAPEL): CPU,(TIJERAS, PAPEL): JUGADOR,(PAPEL, TIJERAS): CPU,
              (PAPEL, LAGARTO): CPU,(TIJERAS, PIEDRA): CPU,(TIJERAS, SPOCK): CPU,(LAGARTO, PIEDRA): CPU,(LAGARTO, TIJERAS): CPU,(SPOCK, PAPEL): CPU,(SPOCK, LAGARTO): CPU,(PAPEL, PIEDRA): JUGADOR}



    resultado = condiciones.get((eleccion_usuario, eleccion_cpu), EMPATE)           # Se declara el ganador tomando en cuenta las condicones anteriores.

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
LAGARTO = "Lagarto"
SPOCK = "Spock"
JUGADOR = "Gana el jugador"
EMPATE = "Empate"
CPU = "Gana el CPU"

puntos_jugador = 0
puntos_cpu = 0
puntos_empate = 0

opcion = 0

print("** REGLAS DEL JUEGO **")                 # ................................ Se imprimen las reglas del juego.
print("- Tijeras cortan papel.\n- Papel cubre piedra.\n- Piedra aplasta lagarto.\n- Lagarto envenena Spock.\n- Spock destruye tijeras.\n- Tijeras decapitan lagarto.\n- Lagarto come papel.\n- Papel desaprueba Spok.\n- Spock vaporiza piedra.\n- Piedra aplasta tijeras.")

while opcion != 6:

    opcion = menu()
    eleccion_usuario, eleccion_cpu = elecciones(opcion)
    seleccionar_ganador(eleccion_usuario, eleccion_cpu)

    print()
    print("-----------------------------")
    print()

    print(f"** Marcador**\nJugador: {puntos_jugador}, CPU: {puntos_cpu}, Empate: {puntos_empate}")