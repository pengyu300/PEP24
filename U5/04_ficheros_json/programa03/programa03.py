"""
Programa03: Cargar un objeto desde una cadena JSON
Define en tu programa la siguiente cadena:
import json
cadena_json = '''
[
 {"nombre": "Chile", "moneda": "Peso chileno"},
 {"nombre": "Egipto", "moneda": "Libra egipcia"}
]
'''
• Convierte la cadena en un objeto Python con json.loads().
• Muestra el tipo de dato que se obtiene.
• Imprime cada país con su moneda.
"""

import json

cadena_json = '''
[
 {"nombre": "Chile", "moneda": "Peso chileno"},
 {"nombre": "Egipto", "moneda": "Libra egipcia"}
]
'''

# Convertir la cadena a objeto Python
paises = json.loads(cadena_json)

print("Tipos de dato obtenido: ", type(paises))

for p in paises:
    print (f"{p['nombre']} usa como moneda el {p['moneda']}.")
