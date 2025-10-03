# programa12
# Sabiendo que 1 milla equivale a 1,61 Km escribe un programa que pida un número de millas y un número de Km, 
# muestre respectivamente el número de millas y kilómetros. Los resultados deben estar redondeados a 2 decimales.

millas = float(input("Introduce millas: "))
km = float(input("Introduce kilometros: "))

millasKm = millas * 1.61
kmMillas = km / 1.61

print(f"{millas} millas son {round(millasKm,2)} km")
print(f"{km} km son {round(kmMillas,2)} millas")

