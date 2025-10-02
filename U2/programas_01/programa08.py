"""
programa08
Escribe un programa que simule un juego en el que dos jugadores tiran dos dados. El que saque mayor puntuación total, gana. 
Si la puntuación total coincide, gana quien haya sacado el dado con el valor más alto. Si el valor más alto también coincide, empatan.
Puedes pedir el valor de cada tirada de dados por teclado o usar la la función random.randrange(1, 7) para obtener un número aleatorio entre 1 y 6 (para ello
debes poner import random al inicio del programa)
"""

import random

#Tiradas de cada jugador
dado1 = random.randrange(1,7)
dado2 = random.randrange(1,7)
dado3 = random.randrange(1,7)
dado4 = random.randrange(1,7)

total1 = dado1 + dado2
total2 = dado3 + dado4

print(f"Jugador 1: {dado1} y {dado2} (total: {total1})")
print(f"Jugador 2: {dado3} y {dado4} (total: {total2})")

if total1 > total2:
    print("Gana jugador 1")
elif total2 > total1:
    print("Gana jugador 2")
else:
    jug1 = max(dado1,dado2)
    jug2 = max(dado3,dado4)
    if jug1 > jug2:
        print("Gana jugador 1")
    elif jug2 > jug1:
        print("Gana jugador 2")
    else:
        print("Empate")
