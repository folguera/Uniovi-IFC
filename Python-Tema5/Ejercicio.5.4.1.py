#Temperaturas en grados centigrados
# + Pedimos la temperatura minima y maxima
Tmin=eval(input('Introduce el valor minimo de la Temperatura: '))
Tmax=eval(input('Introduce el valor maximo de la Temperatura: '))
# + Fijamos el paso
Tpaso=5
# + Fichero de salida
nombrefichero='temperaturasC.dat'

# + Generamos la lista
print('+ Generando temperaturas entre %d y %d en intervalos de %d...'%(Tmin,Tmax,Tpaso))
Cdeg=range(Tmin, Tmax+1, Tpaso)
print(Cdeg)


# + Abrimos el fichero
print('+ Abriendo el fichero \'' + nombrefichero + '\' para escritura...')
f=open(nombrefichero, 'w')

# + Guardamos la lista en el fichero
#   f.write(str(Cdeg)) no sirve porque lo imprime en formato lista
print('+ Escribiendo las temperaturas...')
for i in range(len(Cdeg)):
    f.write(str(Cdeg[i]) + '\n')


# + Cerrando ficheros
print('+ Cerrando los ficheros abiertos...')
f.close()

# + Mensaje final
print('+ HECHO!')
