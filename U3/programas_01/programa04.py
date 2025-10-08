"""
programa04
Mejora el programa anterior de forma que compruebe si el usuario está introduciendo
valores correctos (por ejemplo, el radio no puede ser un número negativo) y si no es así
que pida muestre un aviso y vuelva a pedir el valor.
"""

import math

def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_rectangulo(base, altura):
    return base * altura

def mostrar_menu():
    print("\n Menu ")
    print("1. Calcular el area de un circulo")
    print("2. Calcular el area de un triangulo")
    print("3. Calcular el area de un rectangulo")
    print("4. Salir")


def opcion1():
    radio = float(input("Introduce el radio del circulo: "))
    if radio > 0:
        area = calcular_area_circulo(radio)
        print(f"El area del circulo es {area}")
    else:
        print("El radio debe ser mayor que 0")

def opcion2():
    base = float(input("Introduce la base del triangulo: "))
    altura = float(input("Introduce la altura del triangulo: "))
    if base > 0 and altura > 0:
        area = calcular_area_triangulo(base, altura)
        print (f"El area del triangulo es {area}")
    else:
        print("La base y la altura deben ser mayor que 0")

def opcion3():
    base = float(input("Introduce la base del rectangulo: "))
    altura = float(input("Introduce la altura del rectangulo: "))
    if base > 0 and altura > 0:
        area = calcular_area_rectangulo(base, altura)
        print (f"El area del rectangulo es {area}")
    else:
        print("La base y la altura deben ser mayor que 0")


def main():
    while True:
        mostrar_menu()
        opcion = input("Introduce una opcion (1-4): ")
        if opcion == "1":
            opcion1()
        elif opcion == "2":
            opcion2()
        elif opcion == "3":
            opcion3()
        elif opcion == "4":
            break
        else:
            print("Introduce una opcion valida")

main()      
