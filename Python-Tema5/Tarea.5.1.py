'''
Realice un programa que cree una matriz a de n x n (a partir de un valor
generico n) con los elementos igual a 1, 2, 3, ..., n^2.
Una vez construida la matriz el programa debera realizar las
siguientes operaciones:
* Imprimira los elementos pares de a.
* Realizara una copia de a en b sustituyendo en b los elementos impares por 0.
'''

# Empezamos pidiendo el valor de n
n=eval(input('Introduce la dimension de la matriz: '))


# Creamos la matriz que tendra la forma
# [[       1,        2,        3, ...,  n]
#  [     n+1,      n+2,      n+3, ..., 2n]
#  [    2n+1,     2n+2,     2n+3, ..., 3n]
#   ...
#  [(n-1)n+1, (n-1)n+2, (n-1)n+3, ..., n^2]]
#
# Luego la fila i-esima tendra la forma:
#  [i*n + 1, i*n+2, i*n+3, ---, (i+1)*n]
# O lo que es lo mismo range(i*n+1, (i+1)*n+1)
# Asi que vamos a ir anyadiendo filas a una matriz vacia
print('>> Creando la matriz:')
a=[]
for i in range(n):
	a.append(list(range(i*n+1, (i+1)*n+1)))
print(a)


# (1) Iteramos a los elementos de la matriz mirando cuales de ellos son
# pares. Si no necesitamos los indices de los elementos pares:
print('>> Imprimiendo elementos pares (sin indices): ')
for fila in a:
	for elemento in fila:
		if elemento%2 == 0:
			print("Encontrado un elemento par: %d"%elemento)

# Si necesitamos los indices tenemos que recorrer los valores
print('>> Imprimiendo elementos pares (con indices): ')
for i in range(len(a)):
	for j in range(len(a[i])):
		if a[i][j]%2 == 0:
			print("El elemento (%d,%d) es par con valor %d"%(i,j,a[i][j]))



# Hacemos la copia de a en b y de paso sustituimos los elementos impares
# por 0. Al ser una lista de lista, tenemos que copiar cada fila y
# anyadirselo a una matriz nueva
print('>> Sustituyendo: ')
b=[]
for i in range(len(a)):
	b.append(a[i][:])
	for j in range(len(b[i])):
		if b[i][j]%2 != 0:
			b[i][j]=0


# Imprimimos ambas matrices para comprobar que la copia funciona		
print('Matriz original:')	
print(a)
print('Matriz copia:')	
print(b)

