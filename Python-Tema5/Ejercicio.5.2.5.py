# Version mas sofisticada del ejercicio 5.2.3.py
# 1.- Crear una lista (orig) con los numeros enteros entre n y m (n y m
# deben solicitarse al usuario)
# 2.- A continuacion en una copia de esa lista (otra) cambiar de signo
# aquellos elementos que son multiplos de 3
# 3.- Imprimir por pantalla ordenadamente las 2 listas con el indice de
# cada elemento separados por el simbolo | y con una anchura de campo
# de 3. Ej.
# |   1 |  22 |  22 |
# |   2 |  23 |  23 |
# |   3 |  24 | -24 |
# |   4 |  25 |  25 |
# |   5 |  26 |  26 |
# |   6 |  27 | -27 |

# Let's rock

# Pedimos los valores de n y m
n = int(input("Introduce el valor minimo, n: "))
m = int(input("Introduce el valor maximo, m: "))

# Creamos la lista original
orig=list(range(n,m+1))
# print(a)

# Creamos dos copias de la lista original (para usar dos opciones)
otra1=orig[:]
otra2=orig[:]
# print(a)

# Iteramos sobre la copia mirando a ver que elementos son multiplos de 3
#  - Opcion 1: Sin enumerate
for i in range(len(otra1)):
	if otra1[i]%3 == 0:
		otra1[i] = -otra1[i]

#  - Opcion 2: Con enumerate
for i, e in enumerate(otra2):
	if e%3 == 0:
		otra2[i] = -e
		
for i in range(len(orig)):
	print("| %4d | %4d | %4d | %4d |"%(i, orig[i], otra1[i], otra2[i]))
