# programa10
# Modifica el programa anterior par que pida en primer lugar el número de jugadores que van a jugar. Cada jugador irá jugando 
# y el programa mostrará si ha ganado o no a la banca.

import random

num_jugadores = int(input("¿Cuántos jugadores van a jugar?: "))
banca = random.randint(17, 21)
print(f"\nLa banca tiene {banca} puntos.\n")

for jugador_id in range(1, num_jugadores + 1):
    print(f"--- Jugador {jugador_id} ---")
    total = 0
    while True:
        opcion = input("¿Quieres sacar una carta? (s/n): ").lower()
        if opcion != "s":
            break
        carta = random.randint(1, 5)
        total += carta
        print(f"Has sacado un {carta}. Total: {total}")
        if total > 21:
            print("Te has pasado. Pierdes.\n")
            break

    if total <= 21:
        if total > banca:
            print(f"Jugador {jugador_id} gana a la banca. Banca:{banca}\n")
        else:
            print(f"Jugador {jugador_id} pierde contra la banca. Banca:{banca}\n")

