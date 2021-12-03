# Ejercicio 6.7.3
'''
Se puede mejorar facilmente la aproximacion de la integral utilizada
en el ejercicio anterior aproximando la funcion f(x) mediante una 
primera linea que una (a,f(a)) con el punto medio (c,f(c)) entre
a y b y otra segunda linea que una el punto medio (c,f(c)) con (b,f(b)).
El punto medio c es igual a 1/2(a+b). El area bajo estas dos lineas es
el area de dos trapecios que nos proporcionaran una nueva expresion
aproximada de la intergral de f(x). Obtenga la nueva expresion 
aproximada de la integral e implemente una nueva funcion en Python que
calcule de nuevo las integrales aproximadas de las funciones del
ejemplo anterior
'''

from math import sin, cos, pi
from calculo import integral1, integral2, integraln
from sys import exit

def apartado(i, f, a, b, fi):
	numerica1 = integral1(f, a, b)
	numerica2 = integral2(f, a, b)
	numerican = integraln(f, a, b, 10)
	exacta     = fi(b)-fi(a)
	print('| %2d | %10.5f | %10.5f | %10.5f | %10.5f |'%(i, exacta, numerica1, numerica2, numerican))	
	print('|    |   Error-->   %10.5g | %10.5g | %10.5g |'%(abs(numerica1-exacta), abs(numerica2-exacta), abs(numerican-exacta)))
	print('+----+------------+------------+------------+------------+')	

print('| Ap |   Exacta   | Numerica 1 | Numerica 2 | Numerica N |')	
print('+----+------------+------------+------------+------------+')	
apartado(1, cos, 0, pi, sin)
apartado(2, sin, 0, pi, lambda x: -cos(x))
apartado(3, sin, 0, pi/2, lambda x: -cos(x))

















# Exits function
exit()
print('-'*20)
def apartado(i, f, a, b, fi):
	n=10
	numerica1 = integral1(f, a, b)
	numerica2 = integral2(f, a, b)
	numerican = integraln(f, a, b, n)
	exacta     = fi(b)-fi(a)
	print('%i) I. Numerica 1 | 2| n | Exacta = %8.5f | %8.5f | %8.5f | %8.5f'%(i,numerica1, numerica2, numerican, exacta))
	print('   Dif. 1 | 2 | n = %.1g | %.1g | %.1g'%(abs(numerica1-exacta), abs(numerica2-exacta), abs(numerican-exacta)))

apartado(1, cos, 0, pi, sin)
apartado(2, sin, 0, pi, lambda x: -cos(x))
apartado(3, sin, 0, pi/2, lambda x: -cos(x))
