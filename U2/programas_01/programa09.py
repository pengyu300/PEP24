"""
programa09
Escribe un programa en Python que simule el juego de piedra, papel o tijera. En primer
lugar el programa tendrá que mostrar un mensaje por pantalla al usuario para preguntarle
qué opción desea elegir. Por ejemplo:
1. Piedra
2. Papel
3. Tijera
Seleccione una opción (1, 2 o 3):
Después de leer la opción seleccionada por el usuario el programa generará un número
aleatorio para simular una jugada y mostrará un mensaje indicando si el usuario ha
ganado o ha perdido dependiendo del resultado.
Ten en cuenta que:
• La piedra gana a la tijera pero pierde contra el papel.
• El papel gana a la piedra pero pierde contra la tijera.
• La tijera gana al papel pero pierde contra la piedra.
"""

import random

print("1. Piedra")
print("2. Papel")
print("3. Tijera")

opcion = int(input("Seleccione una opcion (1, 2 o 3): "))

if opcion not in [1,2,3]:
    print("Opcion no valida")
else:
    numAleatorio = random.randint(1,3)
    # Mostrar opciones
    opciones = {1:"Piedra", 2: "Papel", 3: "Tijera"}
    print(f"Opcion usuario: {opciones[opcion]}")
    print(f"Opcion maquina: {opciones[numAleatorio]}")

    if opcion == numAleatorio:
        print("Empate")
    elif (opcion == 1 and numAleatorio == 3) or (opcion == 2 and numAleatorio == 1) or (opcion == 3 and numAleatorio == 2):
        print("Ganaste")
    else:
        print("Perdiste")
