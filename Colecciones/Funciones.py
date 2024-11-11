# def "nombre"("variable"):
# ///////////////////////////////////////////////////////////////////////////////////////// Funcion hola
def hola(nombre):
    print(f"Hola {nombre}")
# ///////////////////////////////////////////////////////////////////////////////////////// Funcion menu
def menu():
    print(" *** Menu ***")
    print("1) Suma.")
    print("2) Resta.")
    print("3) Multiplicación.")
    print("4) División.")
    print("5) División entera.")
    print("6) Modulo.")
    print("7) Potenciación.")
    primer_numero = int(input("Elija una opción: "))
    return primer_numero
#  ///////////////////////////////////////////////////////////////////////////////////////// Funcion calculadora
def calculadora(primer_numero,segundo_numero,tercer_numero):
    if primer_numero == 1:
        resultado = segundo_numero + tercer_numero

    elif primer_numero == 2:
        resultado = segundo_numero - tercer_numero

    elif primer_numero == 3:
        resultado = segundo_numero * tercer_numero

    elif primer_numero == 4:
        resultado = segundo_numero / tercer_numero

    elif primer_numero == 5:
        resultado = segundo_numero // tercer_numero

    elif primer_numero == 6:
        resultado = segundo_numero % tercer_numero

    elif primer_numero == 7:
        resultado = segundo_numero ** tercer_numero

    return resultado

# /////////////////////////////////////////////////////////////////////////////////////////
# primer ejercicio
nombre =input("Ingresa tu nombre: ")
hola(nombre)
print("Adiós")
print()
# /////////////////////////////////////////////////////////////////////////////////////////
# segundo ejercicio
print(" *** Calculadora ***")
segundo_numero =float(input("Ingresa el primer número: "))
tercer_numero =float(input("Ingresa el segundo número: "))
print()
primer_numero = menu()
print()
print(f"El resultado es: {calculadora(primer_numero,segundo_numero,tercer_numero)}")