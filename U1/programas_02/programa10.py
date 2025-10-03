# programa10
# Escribe un programa que dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido.

num = int(input("Introduce un numero de dos cifras: "))
decenas = num // 10
unidades = num % 10
invertido = unidades * 10 + decenas

print("Número invertido:", invertido)
