'''
Tarea 5.4
Se lanza una pelota hacia arriba con una velocidad inicial v0. La 
posicion vertical de la misma vendra dada por la ecuacion
	y = y0 + v0*t - (1/2)*g*t^2
Realice un programa en python que solicite al usuario:

* La altura inicial, y0, desde la que se lanza la pelota.

* La velocidad inicial, v0, a la que se lanza la pelota.

y a partir de esos parametros:

1) Calcule y muestre por pantalla en intervalos de un segundo la
   posicion de la pelota hasta que vuelve a caer a la altura inicial 
   (t = 2v0/g).

2) Calcule y guarde esa informacion en un fichero llamado posiciones.dat
   una tabla en la que la primera columna contenga el valor de t y la
   segunda el valor de y.

3) Repetir los apartados anteriores pero extender el intervalo de tiempos
   hasta que la pelota cae al nivel del suelo (y = 0)
'''

# Variables globales, constantes, etc...
g = 9.8 #m/s2 (aceleracion de la gravedad)



# Solicitamos la altura y velocidad inicales y0, v0
y0 = eval(input('Introduce la altura inicial (m): '))
v0 = eval(input('Introduce la velocidad inicial (m/s): '))



################################3
# Apartado 1
print('>> Apartado 1')

# Calculamos cuanto tarda en caer al suelo
tf = 2*v0/g
print('La pelota volvera a la posicion inicial en %f s'%tf)




################################3
# Apartado 2
print('>> Apartado 2')

# Lista con los posibles tiempos
t = range(int(tf)+1)

# Calculamos las alturas
y = [y0 + v0*ti - 0.5*g*ti*ti for ti in t]

# Vamos a guardarlo todo
f = open('posiciones.dat','w')
for i in range(len(t)):
	f.write('%3d %f\n'%(t[i], y[i]))
	print('%3d %f'%(t[i], y[i]))
f.close()





################################3
# Apartado 3
print('>> Apartado 3')

# Para el tercer apartado hay que resolver la ecuacion de segundo grado
# y0 + v0*t -1/2*g*t^2 = 0
t2f = (v0 + (v0**2 + 2*g*y0)**0.5)/g
print('La pelota volvera al suelo en %f s'%t2f)

# Lista con los posibles tiempos
t2 = range(int(t2f)+1)

# Calculamos las alturas
y2 = [y0 + v0*ti - 0.5*g*ti*ti for ti in t2]

# Vamos a guardarlo todo
f = open('posiciones2.dat','w')
for i in range(len(t2)):
	f.write('%3d %f\n'%(t2[i], y2[i]))
	print('%3d %f'%(t2[i], y2[i]))
f.close()
