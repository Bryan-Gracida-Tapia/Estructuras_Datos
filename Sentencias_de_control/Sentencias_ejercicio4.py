# Gracida Tapia Bryan.
# 28 de octubre del 2024.
# Descripción:
# Programa que da a conocer Si se puede ingresar al bar la negra.


#/////////////////////////////////////////////////////////////////////////////////////////

print("**Bar la Negra**")

edad=int(input("ingrese la edad: "))            # Declaramos nuestras variables incluyendo input para la lectura por consola a la vez que realizamos el casting necesario.
cantidad_a_gastar=float(input("Ingrese catidad disponible para gastar: "))

if edad>=18 and cantidad_a_gastar>=250:         # La condición es que la persona sea mayor de edad y tenga un monto predestinado para gastar, para ello se evalúa los números dados si ambas condiciones son verdaderas se le permitirá el acceso
    print("¡Bienvenido a tu mejor bar!")
else:
    print("Lo sentimos, ya estamos por cerrar!")