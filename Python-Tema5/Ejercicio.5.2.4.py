# Ejercicio de los multiplos y listas comprimidas
nmax = int(input('Hasta que valor quieres buscar multiplos de 11 y de 13: '))

# El numero de multiplos de 11 y de 13 entre 1 y nmax
nmultiplos = nmax // 143

# A por los multiplos
multiplos = [ i*143 for i in range(1, nmultiplos+1) ]

print(multiplos)
