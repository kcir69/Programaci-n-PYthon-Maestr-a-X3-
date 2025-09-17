#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 16:16:07 2025

@author: rklora00
Ejericicos Clase de Programación
Posible examen 

"""

#Ejercicio 1. 



import turtle
import random

# Crear pantalla
screen = turtle.Screen()
screen.setup(800, 600)

# Crear tortuga
t = turtle.Turtle()
t.speed(0)  # que sea rápido

# Colores posibles
colores = ['red', 'blue', 'green', 'black']

# Dibujar 50 círculos
for i in range(50):
    # Elegir coordenadas
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)

    # Elegir radio
    radio = random.randint(10, 20)

    # Elegir color
    color = random.choice(colores)

    # Mover la tortuga al lugar
    t.penup()
    t.goto(x, y)  # moverse sin dibujar
    t.pendown()

    # Dibujar círculo
    t.color(color)
    t.circle(radio)

turtle.done()

################

#Ejercicio 2

# Regresión lineal simple usando fórmulas
def regresion_lineal(x, y):
    n = len(x)
    
    # Calcular medias
    x_mean = sum(x) / n
    y_mean = sum(y) / n
    
    # Calcular beta1 (pendiente)
    num = sum(x[i] * y[i] for i in range(n)) - n * x_mean * y_mean
    den = sum(x[i]**2 for i in range(n)) - (1/n) * (sum(x))**2
    M = num / den
    
    # Calcular beta0 (intercepto)
    beta0 = y_mean - M * x_mean
    
    return beta0, M


#Ejemplo
# Datos
x = [1.00, 2.00, 3.00, 4.00, 5.00, 6.00, 7.00, 8.00, 9.00, 10.00, 11.00, 12.00]
y = [1.23, 2.13, 1.42, -0.69, 4.29, 3.64, 9.30, 10.62, 7.42, 8.40, 12.30, 10.30]


b0, b1 = regresion_lineal(x, y)

print("Ecuación de la recta:")

print("y= " + str(round(b1, 2)) + "x" + " " + str(round(b0, 2)))

print(f" Interseccion (β): {b0}")
print(f" Pendiente (M): {b1}")



####### Ejercicio 3. Calcular la integral.
# Evaluar la función f(x) = 4 - (x - 1)^2 en 3 puntos: -1, 1, 3

x0 = -1
x1 = 1
x2 = 3

# Evaluamos manualmente
f0 = 4 - (x0 - 1)**2
f1 = 4 - (x1 - 1)**2
f2 = 4 - (x2 - 1)**2

# Paso h
h = (x2 - x0) / 2

# Regla de Simpson 1/3 para 3 puntos
area = (h / 3) * (f0 + 4*f1 + f2)

print("Aproximación de la integral:", area)


#si queremos usar el método de rectuangulos y hacerlo función

def Integral_Definida_por_rectangulos(lim_inf, lim_sup, num_trangulos):
    # Definimos los límites de integración
    lim_inf = -1
    lim_sup = 3
    num_trangulos = 100  
    h = (lim_sup - lim_inf) / num_trangulos
    
    area = 0
    
    for i in range(num_trangulos):
        xi = lim_inf + i * h
        fx = 4 - (xi - 1)**2
        area += fx * h
    
    print("Aproximación de la integral por el método de rectángulos:", area)
    return area 

#Ejercicio 4. Conversión a números binarios y decimal.


# Convertir decimal a binario manualmente
def Convertir_Decimal_a_binario(numero):
    resultado = ""
    # Mientras el número sea mayor a 0
    while numero > 0:
        residuo = numero % 2
        resultado = str(residuo) + resultado   
        # Lo agregamos al inicio del string
        numero = numero // 2           
        # División entera entre 2
    
    print("Número decimal 1024 en binario es:", resultado)
    return resultado 

def Convertir_binario_a_decimal(binario):

    decimal = 0
    potencia = 0
    
    # Mientras queden dígitos
    while binario > 0:
        digito = binario % 10         # Extraer último dígito (0 o 1)
        decimal += digito * (2 ** potencia)  # Sumar al total
        binario = binario // 10       # Eliminar último dígito
        potencia += 1                 # Aumentar la potencia
    
    print("Número decimal:", decimal)
    return decimal

#### Ejericicios de Estadistica descriptica. 
# También se podría hace rusando numpy  pero decidimos crearlas mejor gg 

# Media aritmética
def Media(datos):
    n = len(datos)
    media = sum(datos) / n
    print(f"La media es: {media}")
    return media
    

# Mediana (ordenar y tomar el valor central)
def Mediana(datos):
    n = len(datos)
    datos_ordenados = sorted(datos)

    if n % 2 == 0:
        mediana = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
        
    else:
        mediana = datos_ordenados[n//2]
        
    print(f"La mediana es: {mediana}")
    
    return mediana

# Varianza (muestral, con n-1)
def Varianza(datos):
    n= len(datos)
    media=Media(datos)
    suma_cuadrados = 0
    for x in datos:
        suma_cuadrados += (x - media) ** 2
    
    var = suma_cuadrados / (n - 1)
    
    print(f"La varianza es: {var}")

    return var

# Varianza (muestral, con n-1)
def STD(datos):
    n = len(datos)
    var=Varianza(datos)
    desviacion_std = var ** 0.5
    
    print(f"Desviacion estandar es: {desviacion_std}")
    
    return desviacion_std

def Asimetría(datos):
    suma_cubo = 0
    n = len(datos)
    media=Media(datos)
    std=STD(datos)
    for x in datos:
        suma_cubo += (x - media) ** 3
    
    asimetria = (suma_cubo / n) / (std ** 3)
    print(f"La asimetría es:: {asimetria}")
    return asimetria 


def Kurtosis(datos):
    suma_cuarta = 0
    n = len(datos)
    med=Media(datos)
    std=STD(datos)
    for x in datos:
        suma_cuarta += (x - med) ** 4
    
    Kurtosis = (suma_cuarta / n) / (std ** 4) - 3
    print(f"La Kurtosis es: {Kurtosis}")
    return Kurtosis



# Ejemplos del uso de las funciones de estadistica descriptica. 

# Datos piloto
datos = [1, 2, 3, 4, 5, 6, 7, 8, 9] #Lista 

med=Media(datos)
mediana=Mediana(datos)
varia=Varianza(datos)
desviacion=STD(datos)
asi=Asimetría(datos)
Kurtos=Kurtosis(datos)

