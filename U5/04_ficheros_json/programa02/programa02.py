"""
Programa02: Escritura de un fichero JSON
Crea un programa que genere un archivo capitales.json con la siguiente información:
capitales = [
 {"país": "Francia", "capital": "París"},
 {"país": "Australia", "capital": "Canberra"},
 {"país": "Kenia", "capital": "Nairobi"},
 {"país": "Brasil", "capital": "Brasilia"}
 ]

 Debe:
• Escribir los datos en formato JSON con json.dump().
• Usar los parámetros ensure_ascii=False y indent=4 para mejorar la legibilidad.
• Mostrar el mensaje: "Archivo 'capitales.json' creado
correctamente."
 """

import json

capitales = [
 {"país": "Francia", "capital": "París"},
 {"país": "Australia", "capital": "Canberra"},
 {"país": "Kenia", "capital": "Nairobi"},
 {"país": "Brasil", "capital": "Brasilia"}
 ]

with open("capitales.json", "w", encoding="utf-8") as fichero:
    json.dump(capitales, fichero, ensure_ascii=False, indent=4)

print("archivo 'capitales.json' creado correctamente")
