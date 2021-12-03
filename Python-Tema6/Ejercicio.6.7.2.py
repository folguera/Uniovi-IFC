# Ejercicio 6.7.2
'''
La integral de una funcion f(x) en un intervalo [a,b] puede realizarse
en primera aproximacion dibujando una linea recta que una los puntos
(a,f(a)) y (b,f(b)), y calculando el area del trapecio bajo la linea de
la forma ...

Defina una funcion integral(f, a, b) que devuelva el valor aproximado 
de la integral mediante la ecuacion anterior de las siguientes
funciones:
...
'''

from math import sin, cos, pi

def integral(f, a, b):
	return 0.5*(b-a)*(f(a)+f(b))
	
def apartado(i, f, a, b, fi):
	numerica = integral(f, a, b)
	exacta     = fi(b)-fi(a)
	print('%i) I. Numerica = %8.5f, I. Exacta = %8.5f, Diferencia = %.1g'%(i,numerica, exacta, abs(numerica-exacta)))

	
apartado(1, cos, 0, pi, sin)
apartado(2, sin, 0, pi, lambda x: -cos(x))

def cosn(x):
	return -cos(x)
apartado(3, sin, 0, pi/2, cosn)

# Otra posibilidad
cosnp = lambda x: -cos(x)
apartado(4, sin, 0, pi/2, cosnp)

# Una ultima posibilidad
def fn(f):
	return lambda x:-f(x)

#cn = fn(cos)
apartado(5, sin, 0, pi/2, fn(cos))
