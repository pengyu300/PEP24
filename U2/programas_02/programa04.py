"""
programa04
Escribe un programa que use un bucle while y le pida continuamente al usuario que introduzca un número hasta 
que ingrese 45 como la número de salida secreto, en cuyo caso el mensaje "¡Has dejado el bucle con éxito" debe 
imprimirse en la pantalla y el bucle debe terminar.
"""

# Versión 1
while True:
    num = int(input("Introduce un numero: "))
    if num == 45:
        print("¡Has dejado el bucle con éxito!")
        break

#Versión 2
num = 0
while num != 45:
    num = int(input("Introduce un numero: "))
print("¡Has dejado el bucle con éxito!")
