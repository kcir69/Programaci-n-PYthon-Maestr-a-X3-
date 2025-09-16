# -*- coding: utf-8 -*-
"""
Tarea:Obed Lora Marin


Elaborar un l-system de la curva koch. Se encontró este programita que 
modula y genera un L-system. 

https://piratefsh.github.io/p5js-art/public/lsystems/ 
"""



# Definir el sistema 
ax = "F"                 # punto de inicio
reglas = {"F": "F+F--F+F"}   # Movimiento
angulo = 90                 # giro
ciclo = 2

#  L-system
cadena = ax
for _ in range(ciclo):
    nueva_cadena = ""
    for simbolo in cadena:
        if simbolo in reglas:
            nueva_cadena += reglas[simbolo]
        else:
            nueva_cadena += simbolo
    cadena = nueva_cadena


#Haciendo una busqueda en internet me decía que turle sirve para hacer 
#una gráfica. 

import turtle

t = turtle.Turtle()
t.speed(0)   # 0 = lo más rápido
turtle.bgcolor("white")
t.color("red")

for simbolo in cadena:
    if simbolo == "F":
        t.forward(5)     # paso hacia adelante
    elif simbolo == "+":
        t.left(angulo)   # girar a la izquierda
    elif simbolo == "-":
        t.right(angulo)  # girar a la derecha

turtle.done()