# programa02
# Escribe un programa que pida primero un número par (positivo o negativo). 
# Si el valor no es correcto, muestra un aviso.
# Si el valor es correcto, pide un número impar y si no es correcto muestra un aviso.

par = int(input("Introduce un numero par: "))

if par%2 != 0:
    print("Debe ser un numero par")
else:
    impar = int(input("Introduce un numero impar: "))
    if impar %2 == 0:
        print("Debe ser un numero impar")
    else:
        print("Correcto")
