# programa06
# Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta

dia = int(input("Dia: "))
mes = int(input("Mes: "))
anio = int(input("Anio: "))

correcta = True

if mes <1 or mes> 12:
    correcta = False
elif dia < 1:
    correcta = False
else:
    #validar dia segun el mes
    if mes in [1,3,5,7,8,10,12]:
        if dia <1 or dia> 31:
            correcta = False
    elif mes in [4,6,9,11]:
        if dia <1 or dia> 30:
            correcta = False
    elif mes == 2:
        bisiesto = (anio % 4 == 0 and anio % 100 !=0) or (anio % 400 == 0)
        if bisiesto and dia > 29:
            correcta = False
        elif not bisiesto and dia > 28:
            correcta = False

if correcta:
    print("La fecha es correcta")
else:
    print("La fecha es incorrecta")
