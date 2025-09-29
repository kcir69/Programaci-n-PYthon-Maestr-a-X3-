#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 29 13:07:28 2025

Tarea 6. Archiv HTML 
"""

# creaHTML_mejorado.py

# Encabezado del HTML con un poco de estilo
d1 = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Mis Sitios Web para visitar</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #f4f4f9; margin: 20px; }
        h1 { color: #2c3e50; }
        ol { font-size: 18px; }
        li { margin: 10px 0; }
        a { text-decoration: none; color: #2980b9; }
        a:hover { color: #e74c3c; font-weight: bold; }
    </style>
</head>
<body>
<h1>🌐 Lista de Sitios comunes para visitar en python HTML </h1>
<ol>
'''

# Parte final del HTML
d2 = '''
</ol>
<p style="margin-top:30px;">Generado automáticamente con Python 🐍</p>
</body>
</html>
'''

# Lista de sitios (nombre, url)
li = [
    ("Google", "https://www.google.com"),
    ("YouTube", "https://www.youtube.com"),
    ("Wikipedia", "https://www.wikipedia.org"),
    ("Facebook", "https://www.facebook.com"),
    ("Twitter (X)", "https://www.twitter.com"),
    ("Instagram", "https://www.instagram.com"),
    ("UNAM", "https://www.unam.mx"),
    ("BBC News", "https://www.bbc.com"),
    ("CNN", "https://edition.cnn.com"),
    ("GitHub", "https://github.com")
]

# Crear archivo HTML
with open("sitios_mejorados.html", "w", encoding="utf-8") as filo:
    filo.write(d1)

    for nombre, url in li:
        v1 = f'<li><a href="{url}" target="_blank">Visitar {nombre}</a></li>\n'
        filo.write(v1)

    filo.write(d2)