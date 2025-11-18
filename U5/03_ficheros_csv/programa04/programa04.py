"""
Programa 04: Escritura desde diccionarios con csv.DictWriter()
Crea un programa que escriba un archivo patrimonios.csv con información sobre
ciudades con lugares Patrimonio de la Humanidad:
patrimonios = [
 {"Ciudad": "Roma", "País": "Italia", "Lugar emblemático": "Coliseo"},
 {"Ciudad": "El Cairo", "País": "Egipto", "Lugar emblemático": "Pirámides de Guiza"},
 {"Ciudad": "Kioto", "País": "Japón", "Lugar emblemático": "Templos históricos"}
]
El programa debe:
- Usar DictWriter con fieldnames=["Ciudad", "País", "Lugar emblemático"].
- Escribir la cabecera con writeheader() y las filas con writerows().
- Cambiar el delimitador a ;.
- Mostrar un mensaje final: "Archivo 'patrimonios.csv' generado correctamente."

"""

import csv
from os import strerror

patrimonios = [
 {"Ciudad": "Roma", "País": "Italia", "Lugar emblemático": "Coliseo"},
 {"Ciudad": "El Cairo", "País": "Egipto", "Lugar emblemático": "Pirámides de Guiza"},
 {"Ciudad": "Kioto", "País": "Japón", "Lugar emblemático": "Templos históricos"}
]

fieldnames = ["Ciudad", "País", "Lugar emblemático"]

try:
    with open("patrimonios.csv", "wt", encoding="utf-8", newline="") as fichero:
        writer = csv.DictWriter(fichero, fieldnames=fieldnames, delimiter=";")

        writer.writeheader()
        writer.writerows(patrimonios)

    print("Archivo 'patrimonios.csv' generado correctamente.")

except OSError as exc:
    print("Error:", strerror(exc.errno))
except Exception as exc:
    print("Error inesperado:", exc)
            

