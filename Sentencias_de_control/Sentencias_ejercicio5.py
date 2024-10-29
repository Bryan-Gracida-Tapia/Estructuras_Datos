# Gracida Tapia Bryan.
# 28 de octubre del 2024.
# Descripción:
# Programa que da a conocer si un usuario aprobo o no.


#/////////////////////////////////////////////////////////////////////////////////////////
print("  *** Programa que muestra la calificacion final de una materia ***")
primer_calificacion = float(input("Ingrese la primera calificación parcial: "))     # Declaramos nuestras variables incluyendo input para la lectura por consola a la vez que realizamos el casting necesario.
segunda_calificacion = float(input("Ingrese la segunda calificación parcial: "))
tercera_calificacion = float(input("Ingrese la tercera calificación parcial: "))
calificacion_ordinario = float(input("Ingrese la calificacion ordinaria: "))

promedio = ((primer_calificacion + segunda_calificacion + tercera_calificacion)/3)*0.5 + (calificacion_ordinario*0.5)       # se calcula el promedio por método de operadores aritméticos.

if (promedio >= 6 and promedio <=10):           # En esta condición se busca que el usuario tenga un promedio entre 6 y 10.
    print(f"El alumno tuvo una calificación aprobatoria de: {promedio:.2f}")
elif promedio > 10:                             # En caso de que el promedio sea mayor a 10 significa que se ingresaron calificaciones erroneas.
    print(f"Las calificaciones ingresadas no estuvieron en el rango de 1 a 10 ")
else:                                           # Si ninguna de las condiciones anteriores se cumple entonces el alumno habrá reprobado.
    print(f"El alumno tuvo una calificación reprobatoria de: {promedio:.2f}")