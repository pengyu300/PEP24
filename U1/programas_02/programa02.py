"""
programa02
Escribe un programa que
 Cree una variable que almacene el número entero 6.
 Muestre por pantalla el tipo del objeto que contiene el número 6, y el tipo del objeto al que apunta la variable (deben ser iguales)
 Cree otra variable a la que se asigne la primera variable.
 Muestre por pantalla el tipo del objeto que contiene el número 6 y el tipo del objeto
  al que apunta la variable (deben ser iguales)
 Utilice los operadores de identidad (is e is not) para comprobar y mostrar por
  pantalla que los dos variables apuntan al mismo objeto y por lo tanto a la misma posición de memoria.
 Asigne la cadena “Hola” a la primera variable.
 Muestre por pantalla el tipo del objeto que contiene la cadena “Hola” y el tipo del
  objeto al que apunta la variable (deben ser iguales) (y diferentes al objeto 6).
 Utilice la función isinstance() para comprobar y mostrar por pantalla que el
  objeto al que apunta la primera variable es de tipo int y el de la segunda es de tipo str.
"""

variable = 6
print("Tipo del objeto: ", type(6))
print("Tipo del objeto al que apunta la variable: ", type(variable))

variable2 = variable
print("Tipo del objeto: ", type(6))
print("Tipo del objeto al que apunta la variable: ", type(variable2))

print("Apuntan al mismo objeto?", variable is variable2)
print("No apuntan al mismo objeto?", variable is not variable2)

variable = "Hola"
print("Tipo del objeto Hola: ", type("Hola"))
print("Tipo del objeto al que apunta la variable: ", type(variable))

print("Variable 1 es int: ", isinstance(variable,int))
print("variable 2 es str: ", isinstance(variable2, str))
