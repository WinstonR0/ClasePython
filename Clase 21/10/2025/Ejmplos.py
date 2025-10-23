from datetime import datetime

# EJERCICIO 1
"""

"""

#EJERCICIO 2

# 1 Galon = 3.785 Litros
# 3.785 Litros = 1 Galon

"""

galon = 3.785

cantidadLitros = int(input("Ingrese la cantidad de leche producida en un dia (Litros): "))

total = cantidadLitros/galon

print(f"Usted recibira: {total:.2f}")

"""


# EJERCICIO 3
"""
valorTraje = float(input("Ingrese el valor de su compra: "))
nombre = input("Ingrese su nombre por favor: ")
documento = int(input("Ingrese su documento por favor:"))
fecha = datetime.now()



if valorTraje > 2500.00:
    descuento = valorTraje * 0.15
    total = valorTraje - descuento
    print(f"----- FACTURA ----- \n El cliente: {nombre} \n identificado con documento: {documento} \n en la fecha de: {fecha} \n pago un total de: {total} \n con un descueto de: {descuento}")

"""

#EJERCICIO 4 

plato = 95.00

anfitrion = input("¿como te llamas?: ")
cantidadPersonas = int(input("¿Cuantas personas asistiran al evento?"))
fecha = datetime.now()
operacion = plato * cantidadPersonas

if cantidadPersonas > 200 or cantidadPersonas <= 300:
    plato = 85.00
    operacion
    print(f"----- FACTURA ----- \n en la fecha: {fecha} \n se registra el evento a nombre de: {anfitrion} \n con una cantidad de personas de: {cantidadPersonas} \n un valor por unidad del plato de: {plato} \n y un valor a pagar de: {operacion}")
elif cantidadPersonas > 300:
    plato = 75.00
    operacion
    print(f"----- FACTURA ----- \n en la fecha: {fecha} \n se registra el evento a nombre de: {anfitrion} \n con una cantidad de personas de: {cantidadPersonas} \n un valor por unidad del plato de: {plato} \n y un valor a pagar de: {operacion}")
else:
    print("cantidad de personas invalido")



