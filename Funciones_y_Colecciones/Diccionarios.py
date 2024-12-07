# Gracida Tapia Bryan.
# 02 de diciembre del 2024.
# Descripción:
# Creación de diccionarios.


# ///////////////////////////////////////////////////////////////////////////////////////// Ejemplos de uso.
diccionario_alumno = {}
diccionario_profesor = {'nombre': 'alberto','primer_apellido':'Martinez','segundo_apellido':'Barbosa','Edad': 31, 'Correo': 'alberto.mtba@unsij.edu.mx','cubo':12}
diccionario_alumno['nombre'] = 'Bryan'
diccionario_alumno["primer_apellido"] = 'Gracida'
diccionario_alumno["segundo_apellido"] = 'Tapia'
print(diccionario_profesor)
diccionario_alumno['nombre']= 'Lourdes'
diccionario_alumno["primer_apellido"] = 'Durán'
diccionario_alumno["segundo_apellido"] = 'Breceda'
diccionario_alumno["grupo"] = 303
diccionario_alumno['materia_favorita'] = 'Estructura de datos'

alumno = diccionario_alumno ['nombre']
apellido1 = diccionario_alumno ['primer_apellido']
apellido2 = diccionario_alumno ['segundo_apellido']
materia = diccionario_alumno['materia_favorita']
grupo = diccionario_alumno["grupo"]
print(f"Nombre: {alumno} \nApellido paterno: {apellido1} \nApellido materno: {apellido2} \nGrupo: {grupo} \nMateria preferida: {materia}")

for clave,valor in diccionario_alumno.items():
    print(f"clave:{clave} y valor {valor}")
print()
for valor in diccionario_alumno.values():
    print(f"Valor: {valor}")
print()
for clave in diccionario_alumno.keys():
    print(f"clave:{clave} ")

# ///////////////////////////////////////////////////////////////////////////////////////// Combinación con tuplas.
diccionario_egresado = {'nombre': 'Emmanuel', ('primer_apellido','segundo_apellido'):'Gracida'' Tapia','edad':29}

for clave,valor in diccionario_egresado.items():
    print(f"clave:{clave} y valor {valor}")
print()

diccionario_informatica = {'grupo 303': {'numero_alumnos':12,'numero_materias':5,'promedio grupal': 7.99}, 'grupo 503': {'numero_alumnos':7,'numero_materias':5,'promedio grupal': 8},  'grupo 703': {'numero_alumnos':7,'numero_materias':5,'promedio grupal': 6},  'grupo 903': {'numero_alumnos':2,'numero_materias':5,'promedio grupal': 9}}
print(diccionario_informatica)

for grupo in enumerate(diccionario_informatica):
    print(f"\nGrupo: {grupo}")
