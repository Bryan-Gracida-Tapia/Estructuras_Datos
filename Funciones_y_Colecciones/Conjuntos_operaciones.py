# Gracida Tapia Bryan.
# 25 de noviembre del 2024.
# Conjuntos .



# /////////////////////////////////////////////////////////////////////////////////////////
print(" ** Ejemplos de uso de los conjuntos **")
conjunto_nombres = set() #Conjunto vacío
print(f"conjunto_vacío : {conjunto_nombres}")
# Se añaden valores al conjunto con .add
conjunto_nombres.update(["Rebeca", "Juan", "Bryan", "Yamilet", "Galilea", "Rosalinda", "Jennifer", "Tania", "Héctor", "Patricia", "Addi", "Alberto"]) #.update para añadir varios elementos, se hace con corchetes y paréntesis
print(f"Conjunto 303: {conjunto_nombres}")
print(" ")
print(" ** Ejemplos de uso de los conjuntos **")
conjunto_nombres.add("Yamilet") #.add para añadir un elemento
#El conjunto no acepta duplicados
#Ejemplo para eliminar
print(f"Conjunto 303 añadiento a Yamilet: {conjunto_nombres}")
print(" ")
conjunto_nombres.remove("Juan") #para eliminar se hace sólo por referencia porque no tiene un orden

#Para mostrar todos los elementos en el conjunto for
for nombre in conjunto_nombres:
    print(nombre, end = ",")

 #Para verificar si un elemento pertenece a un conjunto
print(f"\nEl elemento 'Rebeca' pertenece al conjunto? {'Rebeca' in conjunto_nombres}")

# /////////////////////////////////////////////////////////////////////////////////////////
print("     *** Se crean dos conjuntos ***")
conjunto_A = {11,7,10,9,5,1,15,7}
conjunto_B = {55,70,11,77,66,9,5}
print(conjunto_A,conjunto_B)
print("     *** Operación Union ***")
# unión
union = conjunto_A|conjunto_B
print(union)
print("     *** Operación Intercepción ***")
# unión
union = conjunto_A&conjunto_B
print(union)
print("     *** Operación Diferencia A-B ***")
# unión
union = conjunto_A-conjunto_B
print(union)
print("     *** Operación Diferencia B-A ***")
# unión
union = conjunto_B-conjunto_A
print(union)

# /////////////////////////////////////////////////////////////////////////////////////////
print("     *** Animales ***")
animales = ["Capibara","Leon","Hipopotamo", "Leopardo","Tigre","Capibara","Leon"]
print(animales)
conjunto_animales = set(animales)
print(conjunto_animales)
lista_modificada = list(conjunto_animales)
print(lista_modificada)