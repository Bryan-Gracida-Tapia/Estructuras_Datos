# Gracida Tapia Bryan.
# 24 de octubre del 2024.
# Descripción:
# Programa que da a conocer si al usuario se le aplicará un descuento.


#/////////////////////////////////////////////////////////////////////////////////////////
print("  *** Programa que determina si aplica descuento ***")

cantidad = int(input("Ingrese la cantidad de su compra: "))     # Declaramos nuestras variables incluyendo input para la lectura por consola a la vez que realizamos el casting necesario.
menbresia = input("Cuenta con la menbresía?: ")

menbresia = menbresia.lower() == "si"                           # Utilizamos la palabra reservada lower para comparar una cadena y saber si se cumple la condición.


if (menbresia == True and cantidad < 1000):     # En esta condición se requiere que cuente con una menbrecia y su compra sea mayor a 1000 para así obtener un descuento del 8%
    print("Tu descuento es del 8%")
    print(f"El total a pagar es: {cantidad - (cantidad * 0.08)}")

elif cantidad >= 1000:                          # En esta condición solo se requiere que el monto sea mayor a 1000 para así obtener un descuento

    print("Tu descuento es del 5%")
    print(f"El total a pagar es: {cantidad - (cantidad * 0.05)}")

else :                                          # En caso de no cumplir ninguna de las condiciones no se aplicará ningún descuento
    print("No obtiene ningún descuento")
    print(f"El total a pagar es: {cantidad}")
