# Gracida Tapia Bryan. 9
# 21 de octubre del 2024.
# Descripción:
# Conversión de cadenas a int, float y boolean mediante la interacción con consola.

# .
print("****   Datos de los alumnos    *****")
nombre = input("Ingresa el nombre: ")
semestre = int(input("Ingresa el no. de semestre: "))
promedio = float(input("Ingresa el promedio: "))
es_mujer = input("¿Es mujer (Si/No)?: ")


# No es posible convertir directamente una cadena a un valor booleano.
# Por ello, utilizamos la misma variable, convertimos a  minúsculas y lo comparamos con la cadena "si".
es_mujer = es_mujer.lower() == "si" #con el punto accedemos a las propiedades la variable y el lower es para convertir a minúsculas, posteriormente se compara con la cadema "si"

# Se imprimen los datos del alumno.
print() #Imprimir salto de línea
print(f"El alumno {nombre} cursa el {semestre} semestre, con un promedio de {promedio:.2f}. Además, es mujer: {es_mujer}.") #la función nombre_variable:.2f imprime, en este caso, los siguientes dos decimales de "promedio", por ejemplo si el usuario ingresa un 7, imprimirá 7.00; sí el usuario ingresa un 8.4, se imprimirá un 7.40, etc