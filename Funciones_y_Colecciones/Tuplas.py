# Gracida Tapia Bryan.
# 12 de septiembre del 2024.
# Descripción:
# Creaciones y observación de tuplas.

# /////////////////////////////////////////////////////////////////////////////////////////
# Primer ejercicio
print(  "***Ejemplo de Tupla")
print(  "\n***Fechas de cumpleaños***")
fechas_cumple = ('12-19','12-27','10-01','10-18','01-11','09-30','08-25','01-06','10-21','04-11','03-06','08-02')
print(f"las fechas de los cumpleaños son: {fechas_cumple}")
print()
for i, fecha in enumerate(fechas_cumple):
    print(f"{i + 1}) {fechas_cumple[i]}")
# /////////////////////////////////////////////////////////////////////////////////////////
# Segundo ejercicio
print(  "\n***Fechas de cumpleaños***")
pi_serie = (4,-4/3,4/5,-4/7,4/9,-4/11,4/13,-4/15,4/17,-4/19,4/21,-4/23)
print(pi_serie)
valor_pi_3_elementos = sum(pi_serie[0:2])
print(f"{valor_pi_3_elementos:.4f}")
valor_pi_5_elementos = sum(pi_serie[0:4])
print(f"{valor_pi_5_elementos:.4f}")
valor_pi_8_elementos = sum(pi_serie[0:7])
print(f"{valor_pi_8_elementos:.4f}")
valor_pi_10_elementos = sum(pi_serie[0:9])
print(f"{valor_pi_10_elementos:.4f}")
valor_pi_todos_elementos =sum(pi_serie)
print(f"{valor_pi_todos_elementos:.4f}")
# /////////////////////////////////////////////////////////////////////////////////////////
# tercer ejercicio
print(  "\n***Cordenadas Tuplas***")
punto_1 = (1,0)
punto_2 = (5,3)
print(f"Cordenadas en tuplas: {punto_1} y {punto_2}")
x1,y1 = punto_1
x2,y2 = punto_2
pendiente = (y2-y1)/(x2-x1)
b = y1 - pendiente * x1
print(f"Expresion de la recta vale: y = {pendiente} x + {b}")