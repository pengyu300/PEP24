# programa09
# Escribe un programa que calcule la calificación de estudiante en un módulo. La calificación se obtiene de la calificación parcial en cada RA 
# (RA1 20%, RA2, 60% y RA3 20%).

RA1 = float(input("Introduce la calificacon de RA1: "))
RA2 = float(input("Introduce la calificacon de RA2: "))
RA3 = float(input("Introduce la calificacon de RA3: "))

calificacion = RA1 * 0.2 + RA2 * 0.6 + RA3 * 0.2

print(f"Nota final: {calificacion}")
