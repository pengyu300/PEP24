"""
programa14
Escribe un programa que reciba un número de bytes y muestre por pantalla cuantos
GBytes, MBytes, KBytes y Bytes son. Tanto para el sistema decimal como el binario.
"""

num = int(input("Introduce cantidad de bytes: "))

# sistema decimal
GB = num // 10**9
MB = (num % 10**9) // 10**6
KB = (num % 10**6) // 10**3
B = num % 10 **3

# sistema binario
GBytes = num // 1024**3
MBytes = (num % 1024**3) // 1024**2
KBytes = (num % 1024**2) // 1024
Bytes = num % 1024

print(f"{num} bytes en sistema decimal (SI): {GB} GB, {MB} MB, {KB} KB, {B} bytes")
print(f"{num} bytes en sistema binario (IEC): {GBytes} GiB, {MBytes} MiB, {KBytes} KiB, {Bytes} bytes")
