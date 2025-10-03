"""
programa03
Escribe un programa que muestre los números pares que hay entre 0 y 10. Resuelve el ejercicio de 4 formas 
diferentes. Usando los bucles for y while sin y con la sentencia continue.
"""

print("Bucle for sin continue: ")
for i in range (0, 11, 2):
    print(i, end=" ")

print("\nBucle while sin continue: ")
i = 0
while i <= 10:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1

print("\nBucle for con continue: ")
for i in range(11):
    if i % 2 != 0:
        continue
    print(i, end=" ")

print("\nBucle while con continue:")
i = 0
while i <= 10:
    if i % 2 != 0:
        i += 1
        continue
    print(i, end=" ")
    i += 1
