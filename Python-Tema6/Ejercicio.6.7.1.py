'''
Ejercicio 6.7.1
Modifique el ejemplo 6.5.11 para que calcule la primera derivada de
las siguientes funciones
'''

# Importamos finite_diff del modulo que habiamos creado en el ejercicio
# anterior
# Ademas importamos funciones que necesitamos de math
from cinematica_rectilineo import finite_diff
from math import exp, sin, cos, pi, log

h=1E-6

# Apartado 1
d1,dd1 = finite_diff(exp,0,h)
e1 = exp(0)
print('1) D. numerica = %8.5f, D. exacta = %8.5f, Diferencia = %.1e'%(d1, e1,abs(d1-e1)))

# Apartado 2
def exp2(x):
	return exp(-2*x)
	
d2,dd2 = finite_diff(exp2,0,h)
e2 = -2*exp2(0)
print('2) D. numerica = %8.5f, D. exacta = %8.5f, Diferencia = %.1e'%(d2, e2,abs(d2-e2)))


# Apartado 3
d3,dd3 = finite_diff(cos, 2*pi,h)
e3 = -sin(2*pi)
print('3) D. numerica = %8.5f, D. exacta = %8.5f, Diferencia = %.1e'%(d3, e3,abs(d3-e3)))


# Apartado 4
d4,dd4 = finite_diff(log, 1,h)
e4 = 1.
print('4) D. numerica = %8.5f, D. exacta = %8.5f, Diferencia = %.1e'%(d4, e4,abs(d4-e4)))
