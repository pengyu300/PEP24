"""
programa08
Escribe un programa para jugar a adivinar un número. En primer lugar la aplicación solicita genera un número 
aleatorio entre 1 y 20. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o 
menor que el introducido. El programa termina cuando se acierta el número.
"""

import random

numAleatorio = random.randrange(1,21)
intentos = 3

while intentos > 0:
    num = int(input("Introduce un numero entre 1 y 20: "))

    if num == numAleatorio:
        print("Correcto")
        break
    elif num < numAleatorio:
        print("El numero es mayor")
    else:
        print("El numero es menor")
    intentos -= 1
    print(f"Queda {intentos} intentos")

if intentos == 0:
    print(f"Has perdido. El numero secreto es {numAleatorio}")
