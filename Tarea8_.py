# -*- coding: utf-8 -*-
"""
Created on Mon Oct 20 13:26:40 2025

@author: 52561
"""
"""
Entregar antes de la próxima clase.

Dada la función 
 definida en el intervalo [-1, 4].

Hacer lo siguiente:

Trazar la función.

Trazar una recta tangente en el punto (1,1) de la gráfica.
"""


import numpy as np
import matplotlib.pyplot as plt

# Definir la función f(x) = x^2
def f(x):
    return x**2

# Crear valores de x entre -1 y 4
x = np.linspace(-1, 4, 100)
y = f(x)


m = 2  
x0 = 1
y0 = f(x0)

# Ecuación de la recta tangente: y = m*(x - x0) + y0
tangente = m * (x - x0) + y0

# Graficar
plt.plot(x, y, label='f(x) = x²', color='blue')
plt.plot(x, tangente, '--', label='Tangente en (1,1)', color='red')
plt.scatter(x0, y0, color='black')  # punto (1,1)
plt.title("Gráfica  f(x)=x² y su recta tangente en (1,1)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()


"""
Ejercicio 2

 Hacer un programa que muestre en pantalla una lista de 5 nombres de estructuras cerebrales y el usuario al seleccionar un nombre despliegue en pantalla información importante de la estructura (puede ser figuras también).
"""

# Lista de estructuras cerebrales
StrCerebrales = {
    "Corteza cerebral": "Responsable de funciones cognitivas superiores, como pensamiento y lenguaje.",
    "Cerebelo": "Coordina movimientos y mantiene el equilibrio.",
    "Zona subventricular: producción de líquido cefaloraquideo"
    "Tálamo": "Centro de relevo sensorial hacia la corteza cerebral.",
    "Hipotálamo": "Regula temperatura corporal, hambre y emociones.",
    "Tronco encefálico": "Controla funciones vitales como respiración y ritmo cardíaco.",
    "Ganglios de la base": "Principalmente motores."}

print("Estructuras cerebrales disponibles:\n")

# Mostrar la lista de estructuras
for i, nombre in enumerate(StrCerebrales.keys(), start=1):
    print(f"{i}. {nombre}")

# Pedir al usuario una opción
op = int(input("\nSelecciona una estructura (1-7): "))

# Mostrar información
clave = list(StrCerebrales.keys())[op - 1]
print(f"\n{clave}: {StrCerebrales[clave]}")



"""
Ejercicio 3 
Construya una imagen de tamaño 256x256 pixeles y 
trace 20 lineas rectas de manera aleatoria y despliegue la imagen.

"""

# Crear una imagen vacía (negra) de 256x256 píxeles
imagen = np.zeros((256, 256, 3))  

# Dibujar 20 líneas aleatorias
for i in range(20):
    x1, y1 = np.random.randint(0, 256, 2)
    x2, y2 = np.random.randint(0, 256, 2)
    color = np.random.rand(3)
    plt.plot([x1, x2], [y1, y2], color=color)

plt.title("20 líneas aleatorias en una imagen 256x256")
plt.xlim(0, 256)
plt.ylim(0, 256)
plt.gca().invert_yaxis()  
plt.show()












