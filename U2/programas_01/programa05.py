# programa05
# Escribe un programa que pida dos números y diga cuál es el menor, cuál el mayor o si son iguales.

num1 = float(input("Introduce el primer numero: "))
num2 = float(input("Introduce el segundo numero: "))

if num1 > num2:
    print(f"Mayor: {num1} Menor: {num2}")
elif num2 > num1:
    print(f"Mayor: {num2} Menor: {num1}")
else:
    print("Son iguales")
