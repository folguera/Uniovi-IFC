'''
Tarea 5.5
Una empresa fabrica piezas esfericas, cilindricas y parelepipedicas de
ciertos materiales. Los datos de las piezas se guardan en ficheros con
la siguiente estructura:

# esfera: densidad, di´ametro
# cilindro: densidad, radio_base, altura
# paralelep´ıpedo: densidad, a, b, c
7.49075959024,3.59571454067
5.11118004268,9.63476493877,8.48747375353
1.98675149697,8.82195404513,1.7374815326,4.96095699634
...


En el ejemplo (dentro del fichero de nombre cuerpos.txt que se adjunta)
las tres primeras lineas son siempre comentarios, y luego vienen los 
datos separados por comas, una pieza por linea: dos numeros para la
esfera, tres numeros para el cilindro y cuatro numeros para el
paralelepipedo. El primer numero de cada linea es la densidad de la
pieza y el resto son sus dimensiones (de acuerdo a como se expresa en
las tres primeras lineas del fichero).

Prepare un programa en python que determine el volumen total, la masa
total y la densidad media de todas las piezas que aparecen en el fichero
cuerpos.txt (que puede tener cualquier numero de lineas).
'''

# Importamos el numero pi (tema 6)
from math import pi

# Variables globales, constantes, etc...
fichero = 'cuerpos.txt' # El nombre del fichero de entrada

# Abrimos el fichero (lectura)
print('Abriendo %s...'%fichero)
f = open(fichero)

# Leemos el fichero
print('Leyendo...')
line = ' '

# Lista de densidades para cada cuerpo
d = []
# Lista de volumenes para cada cuerpo
v = []

while line != '':
	# Leemos una nueva linea
	line = f.readline()

	# Si la linea no contiene nada seguimos
	if line == '': continue
	
	# Saltamos las lineas vacias y los comentarios
	if line[0] == '#' or line[0] == ' ' or line == '\n': continue

	# Dividimos la linea en partes separadas por comas
	camposl = line.split(',')
	
	# Actuemos en funcion del numero de elementos
	if (len(camposl) == 2):
		# Se trata de una esfera
		# + guardamos la densidad
		d.append(float(camposl[0]))
		# + averiguamos el radio
		r = float(camposl[1])
		# + calculamos el volumen
		vesf = 4./3.* pi * r**3
		# + guardamos el volumen
		v.append(vesf)
	elif (len(camposl)) == 3:
		# Se trata de un cilindro
		# + guardamos la densidad
		d.append(float(camposl[0]))
		# + averiguamos el radio_base
		rb = float(camposl[1])
		# + averiguamos la altura
		h = float(camposl[2])
		# + calculamos el volumen
		vcil = h* pi * rb**2
		# + guardamos el volumen
		v.append(vcil)
	elif (len(camposl)) == 4:
		# Se trata de un cilindro
		# + guardamos la densidad
		d.append(float(camposl[0]))
		# + averiguamos a, b y c
		a = float(camposl[1])
		b = float(camposl[2])
		c = float(camposl[3])
		# + calculamos el volumen
		vpar = a*b*c
		# + guardamos el volumen
		v.append(vpar)
	else:
		print('ERROR: Hubo un problema leyendo el fichero')
		
# Ahora a partir de los datos contenidos en d y v podemos calcular las
# masas
m = [d[i]*v[i] for i in range(len(d))]		

# Calculemos la masa total y el volumen total que no es mas que la suma
M = sum(m) # Tambien con math.fsum
V = sum(v) # Tambien con math.fsum

# La densidad media se puede calcular a partir de esos valores
D = M/V


print("%10s %10s %8s"%('masa', 'volumen', 'densidad'))
for i in range(len(d)):
	print("%10.4f %10.4f %8.4f"%(m[i],v[i],d[i]))
	
print("%10s %10s %8s"%('-'*10, '-'*10, '-'*8))
print("%10.0f %10.0f %8.4f"%(M,V,D))

