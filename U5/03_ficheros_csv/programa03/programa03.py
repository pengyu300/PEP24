"""
Programa03: Escritura de un CSV con csv.writer()
Crea un programa que genere un fichero nuevo llamado capitales.csv con los
siguientes datos:
Ciudad      País        Continente
París       Francia     Europa
Canberra    Australia   Oceanía
Nairobi     Kenia       África
Ottawa      Canadá      América
El programa debe:
- Escribir la cabecera y los datos con writerow() y writerows().
- Usar un bloque try/except con os.strerror() para capturar errores de E/S.
- Confirmar con un mensaje final: "Archivo 'capitales.csv' creado correctamente."
"""

import csv
from os import strerror


capitales = [
    ["París", "Francia", "Europa"],
    ["Canberra", "Australia", "Oceanía"],
    ["Nairobi", "Kenia", "África"],
    ["Ottawa", "Canadá", "América"]
]

try:
    with open("capitales.csv", "wt", encoding="utf-8", newline="") as fichero:
        writer = csv.writer(fichero)

        writer.writerow(["Ciudad", "País", "Continente"]) #escribir una fila en el csv
        writer.writerows(capitales)

    print("Archivo 'capitales.csv' creado correctamente. ")

except OSError as exc:  # 只捕获带 errno 的异常
    print("Error:", strerror(exc.errno))
except Exception as exc:  # 捕获其他所有异常
    print("Error inesperado:", exc)
