"""
programa 01
Escribe un programa que pida primero un número par y luego un número impar (positivos
o negativos). En caso de que uno o los dos valores no sea correcto (es decir no sea par o
impar respectivamente), se mostrará un aviso.
"""

par = int(input("Introduce un numero par: "))
impar = int(input("Introduce un numero impar: "))

if par % 2 != 0 and impar % 2 == 0:
    print("El primer número debe ser par y el segundo debe ser impar")
elif par % 2 != 0:
    print("Incorrecto. El primer numero debe ser par")
elif impar % 2 == 0:
    print("Incorrecto. El segundo numero debe ser impar")
else:
    print("Correcto")
