# Gracida Tapia Bryan.
# 12 de septiembre del 2024.
# Descripción:
# Creaciones de listas.

# COLA_FIFO: firs input firs ouput
# PILA_QUEUE_LIFO: last input firs ouput
#/////////////////////////////////////////////////////////////////////////////////////////
# Primer ejercicio
alumnos = []
alumnos.append("Hector") # Se utliza para agregar un elemento a la lista y se utiliza de la siguiente manera: "nombre_variable".append("lo que se agrega")
alumnos.append("Addi")
alumnos.append("Jesus Alberto")
alumnos.append("Juan")
print(alumnos)
print(alumnos[2])
alumnos.insert(1,"Tania") # Insert Se utiliza para agregar un elemento a la lista en base a un valor asginado
for alumnos in alumnos:
    print(f"{alumnos}",end="")

# alumnos.remove("Hector")  Elimina un elemento en base a un valor asignado
# alumnos.pop(2) se usa para elimnar por indice un elemnto de la lista
# del alumnos[2] se utiliza para eliminar por indice un elemento de la lista
print(alumnos)
#/////////////////////////////////////////////////////////////////////////////////////////
# Segundo ejercicio
alumnos = ["Rosalinda", "Juan", "Lourdes", "Tania", "Bryan", "Rebeca", "Jennifer", "Hector", "Galilea", "Patricia", "Jesus", "Addi"]
print(alumnos)
#alumnos.len()
print(alumnos)
alumnos.sort()
print(alumnos)
alumnos.sort(reverse= True)
print(alumnos)
print(alumnos[-2]) # tiene un formato como una hoja doblada cuando es escriben en numeros negativos, se leee desde el ultimo