# Gracida Tapia Bryan 7
# 14 de octubre del 2024
# Descripción:
# Entrada de datos por consola para interacturar con el usuario con valores dinámicos.


# En Python utilizamos la palabra reservada input para permitir la entrada de datos por consola, asignándolo a su vez a una variable.
numero1_cadena = input("Introduce un número decimal: ")
numero2_cadena = input("Introduce otro número decimal: ")
resultado_cadena = numero1_cadena + numero2_cadena # Asumiendo que el usuario ingresó dos números sin algún caracter la función debería ser la suma de los dos números proporcionados.
print()
print(" ****  Recibir número sin un casting de varibles  ****")
print(f"El resultado de {numero1_cadena} y {numero2_cadena} es: {resultado_cadena}") # De primera instacia observamos que los valores se imprimieron de forma corrida sin realizar la operación.

# El casting se lleva a cabo para realizar un cambio de dato, ya que se pasan a números.
numero1_float = float(numero1_cadena)
numero2_float = float(numero2_cadena)
resultado_float = numero1_float + numero2_float # Al hacer el casting facilita la operación por lo cuál se realiza de manera óptima.
print()
print(" ****  Casting de varibles  ****")
print(f"El resultado de {numero1_float} y {numero2_float} es: {resultado_float}")