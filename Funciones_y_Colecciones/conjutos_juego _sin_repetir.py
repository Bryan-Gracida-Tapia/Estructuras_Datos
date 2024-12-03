# Gracida Tapia Bryan.
# 02 de diciembre del 2024.
# Descripción:
# Juego sin repetir.

# ///////////////////////////////////////////////////////////////////////////////////////// Código a nivel de módulo.
flag = 0
contador = 1
conjunto_palabras = set()
lista_conjunto = []
tematica = input("Ingrese el tema del juego: ")

while flag == 0:
    palabra = input(f"Ingrese palabra {contador} del tema de {tematica}: ")
    conjunto_palabras.add(palabra)
    lista_conjunto.append(palabra)
    if len(conjunto_palabras) != len(lista_conjunto): #Accede al número de elementos del conjunto y de la lista
        print(f"El juego ha terminado, han dicho {contador} palabras diferentes")
        print(conjunto_palabras)
        flag = 1
    else: #Si hay el mismo número de elementos en el conjunto que en la lista, incrementa el contador ya que significa que no se repitio ningún elemento en el conjunto
        contador += 1
