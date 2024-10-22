# Gracida Tapia Bryan 10
# 21 de octubre del 2024
# Descripción:
# Entrada de datos por consola para interacturar con el usuario con valores dinámicos.

#/////////////////////////////////////////////////////////////////////////////////////////
# Declaramos nuestras variables con las lecturas por consola asu vez.
# A su vez realizamos las conversiones correspondientes mediante la iteracción por consola que se realiza anteriormente.
nombre_profesor = input("ingrese su nombre: ")
numero_cubo = int(input("ingrese su número de cubículo: "))
horas_de_clase_semanal = float(input("ingrese el número den horas de clases que imparte a la semana: "))
años = input("Lleva más de cinco años en la unsij? si/no>  ")

# En la variable años se utiliza la palabra reservada lower para convertir a minúsculas, y posteriormente comparar con la cadena "si".
años= años.lower()=='si'

# Imprimimos nuestras variables con información adicional para mejor comprención de cada letrero.
print(f"Su nombre es: {nombre_profesor}")
print(f"Su número de cubículo es: {numero_cubo}")
print(f"Horas impartidas a la semanana : {horas_de_clase_semanal:.1f}")
print(f"Tiene más de cinco años en la UNSIJ?: {años}")