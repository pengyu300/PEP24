"""
programa01
Escribe un programa que muestre una lista de números del 1 al 10. Resuelve el ejercicio
de dos formas distintas, utilizando los bucles for y while. Cuando utilices el bucle for
puedes hacer uso de la función range.
"""

print("Con bucle for: ")
for i in range(1,11):
    print(i, end= " ")

print("\nCon bucle while: ")
i = 1
while i <= 10:
    print(i, end=" ")
    i += 1
