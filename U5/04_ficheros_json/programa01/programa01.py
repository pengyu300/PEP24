"""
Programa01: Lectura de un fichero JSON
Crea un fichero llamado paises.json con el siguiente contenido:
[
 {"nombre": "Japón", "continente": "Asia", "poblacion": 125.7},
 {"nombre": "Canadá", "continente": "América", "poblacion": 38.2},
 {"nombre": "España", "continente": "Europa", "poblacion": 48.0}
]
Escribe un programa que:
- Abra el archivo y lo lea con json.load().
- Muestre por pantalla cada país con un formato como:
Japón está en Asia y tiene 125.7 millones de habitantes.
- Controle posibles errores con try/except.
"""

import json

try:
    with open("paises.json", "r", encoding="utf-8") as fichero:
        datos = json.load(fichero)

        for pais in datos:
            print(f"{pais['nombre']} está en {pais['continente']} y tiene {pais['poblacion']} millones de habitantes.")

except FileNotFoundError:
    print("ERROR: No se encontró el archivo 'paises.json'.")
except json.JSONDecodeError:
    print("ERROR: El archivo JSON tiene un formato incorrecto.")
except Exception as e:
    print("ERROR inesperado:", e)
