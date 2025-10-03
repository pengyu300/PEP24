# programa07
# Escribe un programa que reciba una cantidad de minutos y muestre por pantalla a
# cuantas horas y minutos corresponde.

min = int(input("Introduce una cantidad de minutos: "))

horas = min // 60
minutos = min % 60

print(f"{min} minutos son {horas} horas y {minutos} minutos")

