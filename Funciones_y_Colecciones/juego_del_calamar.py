# Gracida Tapia Bryan.
# 06 de Enero del 2025.
# Descripción:
# Creación del juego PIEDRA,PAPEL,TIJERAS, de la serie: El juego del calamar. Utilizando diccionarios.
import random


# ///////////////////////////////////////////////////////////////////////////////////////// Función menú.

def menu():
    print("\n** PIEDRA, PAPEL O TIJERAS **")
    print("[1].- Piedra.")
    print("[2].- Papel.")
    print("[3].- Tijeras.")
    print("[4].- Salir.")
    opcion_elejida_uno,opcion_elejida_dos = int(input("Elija una opción: ")),int(input("Elija una opción: "))
    print()
    if opcion_elejida_uno == 4 or opcion_elejida_dos == 4:                     # ................................ Salir del programa.
        print("Saliendo...")
        flag = 1
    return flag,opcion_elejida_uno,opcion_elejida_dos

# ///////////////////////////////////////////////////////////////////////////////////////// Función eleciones.

def elecciones(opcion_uno,opcion_dos):

    if opcion_uno == 1:                     # ................................ La opción elejida por el usuario vale PIEDRA.
        usuario_uno = PIEDRA
    elif opcion_uno == 2:                     # ................................ La opción elejida por el usuario vale PAPEL.
        usuario_uno = PAPEL
    elif opcion_uno == 3:                     # ................................ La opción elejida por el usuario vale TIJERAS.
        usuario_uno = TIJERAS
    else:
        print("Opción no valida, intentelo de nuevo.")

    if opcion_dos == 1:                     # ................................ La opción elejida por el cpu vale PIEDRA.
        usuario_dos = PIEDRA
    elif opcion_dos == 2:                     # ................................ La opción elejida por el cpu vale PAPEL.
        usuario_dos = PAPEL
    elif opcion_dos == 3:                     # ................................ La opción elejida por el cpu vale TIJERAS.
        usuario_dos = TIJERAS
    else:
        print("Opción no valida, intentelo de nuevo.")

    cpu = random.choice([PIEDRA, PAPEL, TIJERAS])      # CPU toma un valor aleatorio de la lista.
    cpu_dos = random.choice([PIEDRA, PAPEL, TIJERAS])

    print(f"Usuario: {usuario_uno} y {usuario_dos}")
    print(f"CPU: {cpu} y {cpu_dos}")

    return usuario_uno,usuario_dos, cpu, cpu_dos

# ///////////////////////////////////////////////////////////////////////////////////////// Función decisión.
def decision(usuario,usuario_dos, cpu, cpu_dos):
    decision_usuario = int(input(f"Cual de las dos opciones elijes:\n 1){usuario} ó 2) {usuario_dos}\n"))
    if decision_usuario == 1:                     # ................................ La opción elejida por el usuario vale PIEDRA.
        decision_elejida = usuario
    elif decision_usuario == 2:                     # ................................ La opción elejida por el usuario vale PAPEL.
        decision_elejida = usuario_dos
    else:
        print("Opción no valida, intentelo de nuevo.")

    decision_cpu = random.randint(0,2)      # CPU toma un valor aleatorio de la lista.
    if decision_cpu == 1:  # ................................ La opción elejida por el usuario vale PIEDRA.
        decision_elejida_cpu = cpu
    elif decision_cpu == 2:  # ................................ La opción elejida por el usuario vale PAPEL.
        decision_elejida_cpu = cpu_dos
    else:
        print("Opción no valida, intentelo de nuevo.")

    print(f"\n    *** Decisiones finales***")
    print(f"Usuario: {decision_elejida}")
    print(f"CPU: {decision_elejida_cpu}")
    return decision_elejida,decision_elejida_cpu
# ///////////////////////////////////////////////////////////////////////////////////////// Función selecionar ganador.

def seleccionar_ganador(decision_usuario,decision_cpu):
    global puntos_jugador, puntos_cpu, puntos_empate            # Se usa la palabra reservada global  para acceder a las variables que se encuantran fuera de la función.

    piedra_papel_tijeras = { (PIEDRA, TIJERAS): JUGADOR,(PIEDRA, PAPEL): CPU,(TIJERAS, PAPEL): JUGADOR,(TIJERAS, PIEDRA): CPU,(PAPEL, PIEDRA): JUGADOR,(PAPEL, TIJERAS): CPU}       # Se declaran las condiciones en forma de dicionario.

    resultado = piedra_papel_tijeras.get((decision_usuario, decision_cpu), EMPATE)      # Se declara el ganador tomando en cuenta las condicones anteriores.

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


flag = 0

while flag !=1:
    flag,opcion_uno,opcion_dos = menu()
    if flag ==  0:
        primera_eleccion_usuario, segunda_eleccion_usuario, primera_eleccion_cpu, segunda_eleccion_cpu = elecciones(opcion_uno, opcion_dos)
        decision_usuario, decision_cpu = decision(primera_eleccion_usuario, segunda_eleccion_usuario, primera_eleccion_cpu, segunda_eleccion_cpu)
        seleccionar_ganador(decision_usuario, decision_cpu)

    print()
    print("-----------------------------")
    print()

    print(f"** Marcador**\nJugador: {puntos_jugador}, CPU: {puntos_cpu}, Empate: {puntos_empate}")
