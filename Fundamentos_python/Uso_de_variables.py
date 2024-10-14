# Gracida Tapia Bryan
# 13 de octubre de 2024
# En el siguiente archivo se ejemplifica el uso de variables en Python.

# Notas:
# En Python todo es un objeto.
# Variable - una variable es un nombre que almacena un valor guardado en la memoria temporal

# Toda variable requiere que se le asigne un valor inicial
semestre = 3        # Es una variable que apunta a un objeto de tipo int
print(semestre)     # Imprime el valor de la variable
semestre = 4        # La variable ya no apunta al objeto anterior, sino a uno nuevo, por lo que se pierde la referencia
print(semestre)

# Se crean variables de diferente tipo para ejemplificar su uso
nombre = "Bryan"  # variable de tipo String
altura = 1.65       # variable de tipo Float
edad = 19           # variable de tipo Int

# Se imprimen las variables, añadiendo letreros adicionales para mejorar la comprencion de lo que imprime
print("Nombre:", nombre)
print("Semestre:", semestre)
print("Altura: ", altura, "cm.")
print("Edad: ", edad, "años.")

# Se modifican los valores de las variables y se mandan a imprimir
altura = 1.68
edad = 20
print()
print("Valores modificados:")
print("Nombre:", nombre)
print("Semestre:", semestre)
print("Altura: ", altura, "cm.")
print("Edad: ", edad, "años.")

# En Python, las variables son dinámicas, por lo que pueden almacenar otro tipo de dato cuando se requiera
edad = "treinta y uno"      # La variable edad antes tenía el valor de tipo int
print()
print("Edad:", edad)        # La variable edad ahora tiene una valor de tipo String

# Reglas para los nombres de las variables en Python:
# - Utilizar únicamente letras (mayúsculas o minúsculas), números y el guión bajo
# - La variable no puede iniciar con números
# - No se pueden utilizar palabras reservadas, ejemplos: if, else, True, class
# - Es sensible a mayúsculas y minúsculas. Por ejemplo, las palabras "Hola", "hola" y "HOLA" son consideradas diferentes.

# Buenas prácticas
# - Utilizar minúsculas para las palabras
# - Separar las palabras con el guion bajo
# - Utilizar nombres descriptivos de acuerdo a su uso. Por ejemplo: edad, en lugar de e.

print()     #se suele usar cuando se quiere dar un salto de línea
print("Las variables son sensibles a mayúsculas y minúsculas:")
