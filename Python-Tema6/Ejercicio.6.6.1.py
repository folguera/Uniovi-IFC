'''
Ejercicio 6.6.1. Con la función finite diff definida en el ejemplo 6.5.11
cree una nueva función que calcule la velocidad y la aceleración de un 
móvil con movimiento rectilíneo a partir de la función que define la
posición con respecto al tiempo de dicho móvil. Considere para la
posición una función polinómica del tiempo. Para realizar el ejercicio 
cree un módulo llamado cinematica_rectilineo que contenga todas las
funciones necesarias.
'''

from cinematica_rectilineo import *

t = eval(input('Instante de tiempo: '))

s = posicion(1,2,3)
v,a = aceleracion_y_velocidad(s, t)

print('La velocidad vale %f'%v)
print('La aceleracion vale %f'%a)
