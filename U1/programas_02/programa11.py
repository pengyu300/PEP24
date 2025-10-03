# programa11
# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a 
# otra ciudad B es de N segundos. Escribie un programa que determine la hora de llegada a la ciudad B.

hh = int(input("Hora de salida (HH): "))
mm = int(input("Minuto de salida (MM): "))
ss = int(input("Segundo de salida (SS): "))
n = int(input("Duración del viaje en segundos: "))

segundos = hh * 3600 + mm * 60 + ss + n
hora_llegada = segundos // 3600 % 24
minuto_llegada = segundos % 3600 // 60
segundo_llegada = segundos % 60

print(f"Hora de llegada: {hora_llegada}:{minuto_llegada}:{segundo_llegada}")
