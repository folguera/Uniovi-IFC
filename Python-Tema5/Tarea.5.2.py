'''

Realice un programa que calcule los momentos de inercia de las 
siguientes distribuciones de masa: varilla, disco, cilindro y esfera. 
El programa constara de los siguientes pasos:
* Preguntara por pantalla el nombre de la figura geometrica cuyo momento
  debe calcular.
* Comprobara si el nombre introducido coincide con los casos incluidos 
  en el programa, si no coincide con ninguno debera mostrar un mensaje
  que indique que la figura elegida no coincide con ningun caso del
  programa.
* En el caso de que el nombre coincida con uno de los casos, pedira los
  datos necesarios para calcular su momento de inercia y lo imprimira 
  por pantalla.
'''

# Listado de figuras soportadas
listafiguras = ['varilla', 'disco', 'cilindro', 'esfera']

# Pedimos la figura
print('Este programa calcula el momento de inercia para distintas figuras')
print('Actualmente soporta las siguientes')
print(listafiguras)
figura = input('\nPara que figura deseas hacer el calculo? ').lower()
print('Has elegido %s'%figura)

# Inicializamos el momento de inercia a un valor no valido
I = -1

M = eval(input('* Masa? '))
if figura == 'varilla':
	# Respecto al eje que pasa por un extremo I = 1/3 ML2
	L = eval(input('* Longitud? '))
	I = 1./3.*M*L*L
elif figura == 'disco' or figura == 'cilindro':
	# 1/2 MR2
	R = eval(input('* Radio? '))
	I = 0.5*M*R*R
elif figura == 'esfera':
	# Respecto a uno de sus diametros 2/5 MR2
	R = eval(input('* Radio? '))
	I = 2./5.*M*R*R
else:
	print('ERROR: \'%s\' no es ninguna de las figuras soportadas'%figura)

if I > 0:
	print('El momento de inercia vale ' + str(I))
