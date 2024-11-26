# Gracida Tapia Bryan.
# 28 de octubre del 2024.
# Descripción:
# Programa que imprime un ejemplo del ciclo while, mediante una suma acumulativa.


#///////////////////////////////////////////////////////////////////////////////////////// suma acumulativa.
def suma_acumulativa(numero):
    contador = 1
    total = 0
    while contador <= numero:
        total += contador
        contador += 1
    return total
#///////////////////////////////////////////////////////////////////////////////////////// Código a nivel de módulo.
print("  *** Programa que imprime un ciclo while ***\n")
numero = int(input("Ingrese un número: "))
print(f"\nLa suma de 1 hasta el {numero} es de: ", end= "")
total = suma_acumulativa(numero)
print(f"{total}")
print("\nFin de la cuenta")

# randint (primer numero,segundo numero)