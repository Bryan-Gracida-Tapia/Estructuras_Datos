# Gracida Tapia Bryan 10
# 21 de octubre del 2024
# Descripción:
# Entrada de datos por consola para interacturar con el usuario con valores dinámicos.

#/////////////////////////////////////////////////////////////////////////////////////////
# Declaramos nuestras variables con las lecturas por consola .
nombre_profesor = input("ingrese su nombre: ")
numero_cubo = input("ingrese su número de cubículo: ")
horas_de_clase_semanal = input("ingrese el número den horas de clases que imparte a la semana: ")
años = input("Lleva más de cinco años en la unsij? si/no>  ")

# Realizamos los castings correspondientes para tener datos mas fáciles de manipular.
nombre_profesor= str(nombre_profesor)
numero_cubo= int(numero_cubo)
horas_de_clase_semanal= float(horas_de_clase_semanal)
años= años.lower()=='si'

# Imprimimos nuestras variables con información adicional para mejor comprención de cada letrero.
print(f"Su nombre es: {nombre_profesor}")
print(f"Su número de cubículo es: {numero_cubo}")
print(f"Horas impartidas a la semanana : {horas_de_clase_semanal:.3f}")
print(f"Tiene más de cinco años en la UNSIJ?: {años}")