#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Examen 1 
Tarea:Obed Lora Marin
Revisando la prubea de lateralidad de Harris 
(https://es.scribd.com/document/722648434/TEST-LATERALIDAD-HARRIS)
Se realiza un algoritmo para que cualquier usuario pueda usarlo  
"""

import sys

def preg(pregunta):
    # Pide respuesta al usuario (0 = Izquierda, 1 = Derecha, 2 = SALIR)
    while True:
        r = input(pregunta + " [0=Izq / 1=Der / 2=SALIR]: ")
        if r in ("0", "1"):
            return int(r)
        elif r == "2":
            print("Programa terminado por el usuario.")
            sys.exit()   # <--- más confiable que exit()
  
print("\n Prueba de lateralidad de Harris \n")

# Secciones de cada preguntas
secciones = {
    "MANO": [
        "Tirar una pelota",
        "Sacar punta a un lapicero",
        "Clavar un clavo",
        "Cepillarse los dientes",
        "Girar el pomo de la puerta",
        "Sonarse la nariz",
        "Utilizar las tijeras",
        "Cortar con un cuchillo",
        "Peinarse",
        "Escribir",
    ],
    "PIE": [
        "Dar una patada a un balón",
        "Escribir una letra con el pie",
        "Saltar a la pata coja",
        "Mantener el equilibrio sobre un pie",
        "Subir un escalón",
        "Girar sobre un pie",
        "Sacar un balón de un rincón",
        "Conducir un balón unos 10 mts.",
        "Elevar una pierna sobre una mesa",
        "Pierna que adelantas al desequilibrarte",
    ],
    "OJO": [
        "Mirar por un agujero (cartón)",
        "Mirar por un tubo como si fuera un telescopio",
        "Usar un visor o cámara de fotos",
    ],
    "OÍDO": [
        "Escuchar en la pared",
        "Tomar el teléfono",
        "Escuchar en el suelo",
    ]
}

# Guardar resultados
for nombre, preguntas in secciones.items():
    print(f"\n Dominancia DEL {nombre}")
    der = 0
    izq = 0
    for p in preguntas:
        r = preg(p)
        if r == 1:
            der += 1
        else:
            izq += 1
    if der > izq:
        print(f"Dominancia del {nombre}: Derecha")
    elif izq > der:
        print(f"Dominancia del {nombre}: Izquierda")
    else:
        print(f"Dominancia del {nombre}: Mixta")