# Gracida Tapia Bryan.
# 14 de Enero del 2025.
# Descripción:


# ///////////////////////////////////////////////////////////////////////////////////////// Función .
def imprimir_alumno(nombre:str="", edad:int=0, matricula:int=0,*, grupo:int=0, semestre:int=0) -> None:
    """

    :param nombre: Recibe un valor char
    :param edad: Recibe un valor entero
    :param matricula: Recibe un valor entero
    :param grupo: Recibe un valor entero
    :param semestre: Recibe un valor entero
    :return: Imprime en pantalla los datos del alumno
    """
    print("\nDatos personales:")
    print(f"\nNombres: {nombre}")
    print(f"Edad:{edad}")
    print(f"Matricula: {matricula}")
    print(f"Grupo: {grupo}")
    print(f"Semestre: {semestre}")
# /////////////////////////////////////////////////////////////////////////////////////////  Función Código a nivel de módulo .
def main()-> None:
    if __name__ == '__main__':
        nombre = "Bryan"
        edad = 19
        matricula = 24514014
        grupo = 303
        semestre = 3

        #imprimir_alumno(nombre,edad,matricula,grupo, semestre)
        #imprimir_alumno(nombre="pancho", matricula=20032671, semestre=4, edad=20, grupo=303)
        imprimir_alumno(nombre,edad,matricula,grupo=303, semestre=3)


# /////////////////////////////////////////////////////////////////////////////////////////  Main.
main()