# Ejercicio 6.3.1.
# Utilice las funciones de conversion de tipos para convertir los
# grados Celsius en Fahrenheit mediante la expresion
# F = 9/5C + 32

# C es la temperatura en grados centigrados
C = input("Introduce la temperatura en grados centigrados: ")


# Fmal es la temperatura en grados Farenheit MAL CALCULADA
Fmal = 9/5*C + 32

# F es la temperatura en grados Farenheit BIEN CALCULADA
F = float(9)/5*C + 32

print("%.2f gados Centigrados corresponde a %.2f grados Farenheit"%(C,F))
print("Si lo hubieramos hecho mal saldria %.2f grados Farenheit"%Fmal)
