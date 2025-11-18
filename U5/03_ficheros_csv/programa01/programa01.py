"""
Programa01: Lectura básica con csv.reader()
Escribe un programa que:
 Lea el fichero usando csv.reader().
 Muestre en pantalla frases como:
 La ciudad de Tokio está en Japón y tiene 37.4 millones de habitantes.
 Controle las posibles excepciones
"""

import csv
from os import strerror


try:
    with open("ciudades.csv", "rt", encoding="utf-8") as fichero:
        leer = csv.reader(fichero)

        next(leer) #saltar cabecera

        for ciudad, pais, poblacion in leer:
            print(f"La ciudad de {ciudad} está en {pais} y tiene {poblacion} millones de habitantes.")

except Exception as exc:
    print("Eroooor", strerror(exc.errno))
