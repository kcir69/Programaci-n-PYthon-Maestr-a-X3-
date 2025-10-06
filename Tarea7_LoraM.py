#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 5 12:26:31 2025
Figuras. Tarea 6 LoraM

@author: rklora00
"""

#Figura 1 

import numpy as np
import matplotlib.pyplot as plt

# Rango con más puntos para suavizar
t = np.linspace(-6, 6, 6000)

# Ecuaciones corregidas (estructura simétrica)
x = 2.5 * (np.sin(-5 * t)**2) * (np.cos(np.cos(4.28 - 2.3 * t))**2)
y = 2.5 * (np.sin(np.sin(-5 * t))) * (np.cos(4.28 - 2.3 * t)**2)

plt.style.use('dark_background')
plt.figure(figsize=(6,6))
plt.plot(x, y, color='#ff0044', linewidth=1.2)

# Reflejos para asegurar simetría completa
plt.plot(-x, y, color='#ff0044', linewidth=1.2, alpha=0.8)
plt.plot(x, -y, color='#ff0044', linewidth=1.2, alpha=0.8)
plt.plot(-x, -y, color='#ff0044', linewidth=1.2, alpha=0.8)

plt.axis('off')
plt.show()

#Figura 2 

t = np.linspace(-3, 3, 2000)

x = 7 * np.cos(np.cos(1.28 * np.round(t)))**2 * (1 + np.cos(1.18 * t)**4)
y = 7 * np.sin(np.sin(1.28 * t))**2 * np.sin(np.sin(1.18 * t))

# Centramos la figura (muy importante)
x = x - np.mean(x)
y = y - np.mean(y)

plt.figure(figsize=(6,6), facecolor='#ffe4ec')
plt.plot(x, y, color='#8b0044', linewidth=1, alpha=0.8)

# Rotaciones más densas
for k in range(1, 24):
    ang = k * np.pi / 12
    xr = x * np.cos(ang) - y * np.sin(ang)
    yr = x * np.sin(ang) + y * np.cos(ang)
    plt.plot(xr, yr, color='#8b0044', linewidth=1, alpha=0.4)

plt.axis('off')
plt.show()



# Figura 3 
t = np.linspace(0, 2*np.pi, 2000)
a, b, c = 1, 49, 0

x = np.cos(a*t) + np.cos(b*t)/2 + np.sin(c*t)/3
y = np.sin(a*t) + np.sin(b*t)/2 + np.cos(c*t)/3

plt.style.use('dark_background')
plt.figure(figsize=(6,6))
plt.plot(x, y, color='#55ccff', linewidth=1)
plt.axis('off')
plt.show()
# Figura 4 

t = np.linspace(-3, 3, 1500)

x = 7 * np.sin(7.32 * t) / (1 + np.cos(1.42 * t)**2)
y = 7 * np.cos(1.42 * t) * np.sin(7.32 * t)**4

plt.figure(figsize=(6,6), facecolor='#808000')  # Fondo verde oliva
plt.plot(x, y, color='black', linewidth=1)

# Simetría respecto a los ejes
plt.plot(-x, y, color='black', linewidth=1)
plt.plot(x, -y, color='black', linewidth=1)
plt.plot(-x, -y, color='black', linewidth=1)

plt.axis('off')
plt.show()



# figura 5 

t = np.linspace(-3, 3, 1500)

x = 7 * np.cos(np.cos(1.28 * np.round(t)))**2 * (1 + np.cos(1.18 * t)**4)
y = 7 * np.sin(np.sin(1.28 * t))**2 * np.sin(np.sin(1.18 * t))

# Centrado para girar en torno al origen
x = x - np.mean(x)
y = y - np.mean(y)

plt.figure(figsize=(6,6), facecolor='#ffe4ec')
plt.plot(x, y, color='#ff0066', linewidth=1, alpha=0.7)

# Rotaciones suficientes para completar la simetría circular
for k in range(1, 24):  # 24 rotaciones (15° cada una)
    ang = k * np.pi / 12
    xr = x * np.cos(ang) - y * np.sin(ang)
    yr = x * np.sin(ang) + y * np.cos(ang)
    plt.plot(xr, yr, color='#ff0066', linewidth=1, alpha=0.35)

plt.axis('off')
plt.show()


# Figura 6 


# Rango más amplio
t = np.linspace(-10, 10, 6000)

# Ecuaciones corregidas y suavizadas
x = 7 * np.cos(0.56 * t) * np.sin(0.56 * t) / (1 + 2 * (np.cos(2.02 * t)**2))
y = 7 * np.sin(0.56 * t) * np.sin(0.56 * t) / (1 + (np.sin(2.02 * t)**2))

plt.figure(figsize=(6,6), facecolor='#1b0080')  # fondo azul profundo

# Trazo principal
plt.plot(x, y, color='yellow', linewidth=1.4, alpha=0.9)

# Simetrías
plt.plot(-x, y, color='yellow', linewidth=1.4, alpha=0.9)
plt.plot(x, -y, color='yellow', linewidth=1.4, alpha=0.9)
plt.plot(-x, -y, color='yellow', linewidth=1.4, alpha=0.9)

# Rotaciones decorativas (12 pétalos)
for k in range(0, 12):
    ang = k * np.pi / 6
    xr = x * np.cos(ang) - y * np.sin(ang)
    yr = x * np.sin(ang) + y * np.cos(ang)
    plt.plot(xr, yr, color='gold', linewidth=0.9, alpha=0.5)

plt.axis('off')
plt.show()








