"""
programa07
Escribe un programa que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los 
números introducidos. Realiza dos versiones: una que utiliza la instrucción break y otra no.
"""

#  Versión 1 con break
suma = 0
contador = 0

while True:
    num = int(input("Introduce un numero (0 para salir): "))
    if num == 0:
        break
    suma += num
    contador += 1

if contador > 0:
    print(f"Suma:{suma} Media:{suma/contador} ") 
else:
    print("No se ha introducido ningun numero (0 para salir: )")


# Versión 2 sin break
suma = 0
contador = 0
num = -1

while num != 0:
    num = int(input("Introduce un numero: "))
    suma += num
    contador += 1

if contador > 0:
    print(f"Suma{suma} Media:{suma/contador}")
else:
    print("No se ha introducido ningun numero ")
