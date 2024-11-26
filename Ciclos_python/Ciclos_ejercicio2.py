# Gracida Tapia Bryan.
# 28 de octubre del 2024.
# Descripción:
# Programa que imprime un ejemplo del ciclo while, mediante una suma acumulativa.

#///////////////////////////////////////////////////////////////////////////////////////// Suma acumulativa.
def suma_acumulativa ( numero_inicial, numero_final):
    total = 0
    while numero_inicial <= numero_final:
        total += numero_inicial
        numero_inicial += 1
    return total
#///////////////////////////////////////////////////////////////////////////////////////// Código a nivel de módulo.
print("     *** Programa que realiza una suma acumulativa ***\n")
numero_inicial = int(input("Ingrese el número inicial: "))
numero_final = int(input("Ingrese el número final: "))

print(f"\nLa suma acumulativa de {numero_inicial} hasta el {numero_final} es de: ", end= "")

total = suma_acumulativa(numero_inicial,numero_final)  # Llamada a la función suma acumulativa.

print(f"{total}")
print("\nFin de la cuenta...")