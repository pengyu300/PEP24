# programa03
# Escribe un programa que pida dos números y muestre su división.
# No se puede dividir por 0 (mostrar aviso en ese caso).

numero1 = float(input("Introduce el dividendo: "))
numero2 = float(input("Introduce otro divisor: "))

if numero2 == 0:
    print("No se puede dividir por 0")
else:
    resultado = numero1 / numero2
    print(f"Resultado:  {numero1} / {numero2} = {resultado}")
