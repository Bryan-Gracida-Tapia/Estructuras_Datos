# Gracida Tapia Bryan.
# 25 de noviembre del 2024.
# Descripción:
# Calculadora basica.
import random

# ///////////////////////////////////////////////////////////////////////////////////////// .
i = 0
while i != 13:
    Alumnos = ["Tania","rebeca","yamm","jesus","alberto","juan","addi","galilea","rosalinda","paty","jenni","bryan"]
    rol = ["J1","J2","J3","J4","AU","AG","AC","AI","ALU","ALEXG","CAROLINA","IRIS"]
    eleccion = str(random.choice(Alumnos))
    segunda_eleccion = str(random.choice(rol))
    print(f"alumno: {eleccion}  Rol: {segunda_eleccion}")
    Alumnos.remove(eleccion)
    rol.remove(segunda_eleccion)
    i +=1
