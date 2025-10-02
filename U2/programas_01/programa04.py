"""
programa04
Escribe un programa que lea por teclado un número real entre 1 y 10, simulando una
nota numérica, y muestre un mensaje indicando la calificación obtenida teniendo en
cuenta los siguientes rangos:
• Insuficiente: [0, 5)
• Suficiente: [5, 6)
• Bien: [6, 7)
• Notable: [7, 9)
• Sobresaliente: [9, 10]

Si el número introducido no está en ninguno de los rangos anteriores debe mostrar un
mensaje de error indicando que la nota no es válida.
Hay que usar la estructura match.
"""

nota = float(input("Introduce un nota entre 0 y 10: "))

if 0 <= nota < 5:
    calificacion = "Insuficiente"
elif 5 <= nota < 6:
    calificacion = "Suficiente"
elif 6 <= nota < 7:
    calificacion = "Bien"
elif 7 <= nota < 9:
    calificacion = "Notable"
elif 9 <= nota <= 10:
    calificacion = "Sobresaliente"
else:
    calificacion = "Error"

match calificacion:
    case "Insuficiente":
        print(f"{nota} - Insuficiente")
    case "Suficiente":
        print(f"{nota} - Suficiente")
    case "Bien":
        print(f"{nota} - Bien")
    case "Notable":
        print(f"{nota} - Notable")
    case "Sobresaliente":
        print(f"{nota} - Sobresaliente")
    case "Error":
        print(f"La nota {nota} no es valida. Debe ser entre 0 y 10")
