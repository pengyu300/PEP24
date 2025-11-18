"""
Programa02: Lectura con csv.DictReader()
Crea un programa que lea el archivo ciudades.csv usando csv.DictReader().
Debe:
- Mostrar los nombres de las columnas (fieldnames).
- Recorrer las filas e imprimir información como:
{Ciudad} ({País}) tiene una población aproximada de {Población (millones)} millones.
- Si el archivo no incluye cabecera, define manualmente los campos necesarios
"""

import csv
from os import strerror

try:
    with open("ciudades.csv", "rt", encoding="utf-8") as fichero:
        leer = csv.DictReader(fichero)

        # lee la primera línea del CSV (la cabecera) y la convierte en una lista de nombres de campo.
        print ("Columnas detectadas:", leer.fieldnames)

        for fila in leer:
            ciudad = fila["Ciudad"]
            pais = fila["País"]
            poblacion = fila["Población (millones)"]

            print(f"{ciudad} ({pais}) tiene una población aproximada de {poblacion} millones.")

except FileNotFoundError as exc:
    print("Error", strerror(exc.errno))

except KeyError as exc:
    print(f"Error: falta la columna '{exc.args[0]}' en el CSV")

except Exception as exc:
    print("Error inesperado:", exc)
