"""
programa02
Escribe un programa en Python que haga uso de una función llamada saludar que cumpla los siguientes requisitos:
    • Entrada: Tiene 4 parámetros de entrada, que serán 4 cadenas de texto: nombre,
    primer apellido, segundo apellido y curso. El parámetro curso tendrá en la
    declaración de la función el valor por defecto “2DAW”
    • Salida: No tiene parámetros de salida.
    • Funcionalidad: Imprime por pantalla un mensaje saludando al alumno/a que se
    haya pasado como parámetro de entrada.
El programa debe invocar a la función varias veces. En algunas de ellas se tiene que usar
el paso de parámetros de forma nominal (con clave valor).
"""

def saludar(nombre, apellido1, apellido2, curso="2DAW"):
    print(f"Hola {nombre} {apellido1} {apellido2} alumno de {curso}")

# LLamadas a la función
saludar("Ana", "Perez", "Sanchez")
saludar("Juan", "Sanchez", "Gomez", "2DAW")

# Paso de parámetros nominales
saludar(nombre="Claudia", apellido1="Ruiz", apellido2="Moreno")
saludar(nombre="Maria", apellido2="Fernandez", apellido1="Navarro", curso="2DAW")
