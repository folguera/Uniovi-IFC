'''
La sucesion de Fibonacci es una sucesion infinita de numeros naturales
n la que cada numero se calcula sumando los dos anteriores a el, por lo 
que los numeros de esta sucesion son:
	0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
A los elementos de esta sucesion se les llama numeros de Fibonacci.
Realice un programa (utilizando un bucle) que calcule y muestre por 
pantalla el numero Fibonacci cuyo orden n sera un dato de entrada.
'''

# Usado para calcular tiempos
import time


# Empezamos preguntando por n y asegurandonos que es un valor razonable
n=eval(input('Introduce el orden del numero: '))
assert type(n) == int, 'El numero tiene que ser entero'
assert n>0, 'El orden tiene que ser mayor que 0'


#######################################################################
# Primera version.
# No almacenamos los valores en ninguna lista por lo que tenemos que
# tener dos variables que guarden los dos ultimos numeros.
print('>> Primera version')
tic1 = time.clock()
f1 = 0  # El primero numero
f2 = 1  # El segundo numero
f  = -1 # El numero nuevo


if n==1:
	f = f1
elif n==2:
	f = f2
else:
	print('Orden %3d: %7d'%(1,f1))
	print('Orden %3d: %7d'%(2,f2))
	for i in range(3,n+1):
		f=f1+f2
		f1=f2
		f2=f
		#print('Orden %3d: %7d'%(i,f))
tac1 = time.clock()

print('El numero de Fibonacci de orden %d es %d'%(n,f))
print('Calculado en %f s'%(tac1-tic1))
#######################################################################
# Segunda version
# En esta version almacenamos los numeros en una lista.
print('>> Segunda version')
tic2 = time.clock()
F = [0, 1] # Dos primeros numeros
for i in range(2, n):
	F.append(F[i-2]+F[i-1])
tac2 = time.clock()

#print('Los primeros %d numeros de Fibonacci son: '%(n) + str(F))
print('El numero de Fibonacci de orden %d es %d'%(n,F[-1]))
print('Calculado en %f s'%(tac2-tic2))
