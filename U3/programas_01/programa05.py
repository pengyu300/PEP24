"""
programa05
Escribe un programa donde crees varias funciones y pruebes el ámbito de las variables
en Python (globales, no locales y locales).
"""

# Variables locales
def ejemplo_local1():
    n = 2
    print("Dentro de la función:" ,n)

ejemplo_local1()


def ejemplo_local2():
    n = 2
    print("Dentro de la funcion:" ,n)
    return

n = 5
ejemplo_local2()
print("Fuera de la funcion:" ,n)


# Variables globales
a = 10

def ejemplo_global1():
    print("Variable global dentro de la funcion: ",a)

ejemplo_global1()
print("Variable global fuera de la funcion: ",a)


def ejmplo_global2():
    print("Dentro de la funcion:" ,b)

b = 5
ejmplo_global2()
print("Fuera de la funcion: ",b)


# Variables no locales
def ejemplo_noLocal():
    def sub_noLocal():
        print("Desde la funcion interna: ",c)
    
    c = 3
    sub_noLocal()
    print("Desde la funcion externa: ",c)

c = 4
ejemplo_noLocal()
print("Variable global: ",c)
