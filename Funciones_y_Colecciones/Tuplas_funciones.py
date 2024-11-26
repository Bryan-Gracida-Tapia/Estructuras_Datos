# Gracida Tapia Bryan.
# 12 de septiembre del 2024.
# Descripción:
# Creaciones de listas.


# /////////////////////////////////////////////////////////////////////////////////////////
# Primer ejercicio
print(  "***Calificaciones del parcial")
# ///////////////////////////////////////////////////////////////////////////////////////// Función para encontrar la calificación final de parciales y la calificación final
def calificacion (calificaciones):
    promedio_parcial = sum(calificaciones[0:3])/3
    promedio_final= promedio_parcial + (calificaciones[3])/2
    return promedio_parcial, promedio_final

# \\\\\\\\\\\\\\\\\\\\\\\\\ Se leen las calificaciones de los parciales y la del ordinario
primer_parcial = float(input("Calificación parcial 1: "))
segundo_parcial = float(input("Calificación parcial 2: "))
tercer_parcial = float(input("Calificación parcial 3: "))
ordinario = float(input("Calificación ordinario: "))
# \\\\\\\\\\\\\\\\\\\\\\\\\ se ingresan las calificaciones a una tupla
calificaciones = (primer_parcial,segundo_parcial,tercer_parcial,ordinario)
promedio_parciales, promedio_final =  calificacion(calificaciones) # se realiza la llamada a la función
# \\\\\\\\\\\\\\\\\\\\\\\\\ Se imprimen los valores
print(f"Calificación parcial: {promedio_parciales}")
print(f"Calificación final: {promedio_final}")
