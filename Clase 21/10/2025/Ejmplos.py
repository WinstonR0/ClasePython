from datetime import datetime
import math

# EJERCICIO 1

# AREA DE LA FIGURA 2.3

# Pedir datos
H = float(input("Por favor ingrese el valor de la hipotenusa: "))
R = float(input("Por favor ingrese el valor del cateto opuesto: "))

"""
Se sabe que tenemos la hipotenusa, tambien tenemos uno de los catetos, que tambien es el radio de la circunferencia
se debe hallar un cateto faltante que tambien es la altura del triangulo rectangulo

"""
# formula general a2 + b2 = c2 (a= cateto 1, b=un cateto 2, c= hipotenusa)
# como ya tenemos uno de los catetos y la hipotenusa necesitamos hallar el otro

# A = altura y cateto faltante
valorDentroRaiz = H**2 - R**2
A = math.sqrt(valorDentroRaiz)

# Se debe hallar el area del triangulo
# Para hallar el area del triangulo usaremos  cateto1 * cateto2 / 2 -> R^2 * A /2 
# Se halla el area total del triangulo multiplicando por 2 -> 2 * area = R * A ya que se cancela el 2 del denominador

Area = R * A

# Hallar el area de la circunferencia, como es la mitad del circulo dividimos por 2
areaSemiCircunferencia = math.pi * R**2 / 2

# Calcular el area total de la figura sumando todas las areas
areaTotal = Area + areaSemiCircunferencia

print(f"----- RESULTADO ----- \n el area total de la figura es: {areaTotal:.2f}. \n hipotenusa: {H} \n cateto1(R): {R} \n cateto2(A): {A} \n area del triangulo: {Area} \n area del circulo: {areaSemiCircunferencia:.2f}")

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

"""
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

"""






