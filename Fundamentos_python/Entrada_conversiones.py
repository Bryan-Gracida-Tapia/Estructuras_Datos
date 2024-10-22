# Gracida Tapia Bryan. 9
# 21 de octubre del 2024.
# Descripción:
# Conversión de cadenas a int, float y boolean mediante la interacción con consola.

# Se leen los datos por consola al mismno tiempo que se realiza el casting al tipo de dato que corresponde, ahorrando asi líneas de código.
print("****   Datos de los alumnos    *****")
nombre = input("Ingresa el nombre: ")       # El nombre se queda solamente con el input puesto que ya se lee como una cadena
semestre = int(input("Ingresa el no. de semestre: "))       # El semestre se lee como cadena y asu vez se realiza el casting a entero
promedio = float(input("Ingresa el promedio: "))        # El promedio se lee como cadena y asu vez se realiza el casting a float
es_mujer = input("¿Es mujer (Si/No)?: ")        # El es_mujer se queda solamente con el input puesto que ya se lee como una cadena


# No es posible convertir directamente una cadena a un valor booleano.
# Por ello, utilizamos la misma variable, convertimos a  minúsculas y lo comparamos con la cadena "si".
es_mujer = es_mujer.lower() == "si" # Con el punto accedemos a las propiedades la variable y el lower es para convertir a minúsculas, posteriormente se compara con la cadema "si"

# Se imprimen los datos del alumno.
print() #Imprimir salto de línea
print(f"El alumno {nombre} cursa el {semestre} semestre, con un promedio de {promedio:.2f}. Además, es mujer: {es_mujer}.") #la función nombre_variable:.2f imprime, en este caso, los siguientes dos decimales de "promedio", por ejemplo si el usuario ingresa un 7, imprimirá 7.00; sí el usuario ingresa un 8.4, se imprimirá un 7.40, etc