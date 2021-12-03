##############################################################################
# Este programa lee un conjunto de valores de temperatura en grados
# centigrados de un fichero, los convierte a grados Farenheit y los imprime
# en una tabla en otro fichero.
#
# Secuencia del codigo:
# 1) Obtener los datos de entrada: Leerlos del fichero de entrada y
#    convertirlos a valores numericos almacenandolo en una lista de numeros
# 2) Realizar los calculos: Convertir los grados centrigrados en grados Farh.
# 3) Mostrar la informacion: Escribir la informacion en un fichero
##############################################################################

#---------------------------------
# (0) Parametros globales de configuracion
#---------------------------------
# + Fichero de entrada
ficheroEntrada='temperaturasC.dat'
# + Fichero de salida
ficheroSalida='temperaturasFC.dat'




#---------------------------------
# (1) Obtener los datos de entrada
#---------------------------------

########## Opcion 1

# + Abrimos el fichero de entrada y leemos los datos
print('+ Abriendo el fichero \'' + ficheroEntrada + '\' para lectura...')
fr=open(ficheroEntrada, 'r')
print('+ Leyendo temperaturas en grados (a lista de str)...')
#Cdegtext = fr.readlines() #Ojo que estaran en modo texto
Cdegtext = fr.read().splitlines() #Ojo que estaran en modo texto
print('  Cdegtext = ' + str(Cdegtext))


# + Cerrando fichero de entrada
print('+ Cerrando el fichero de entrada...')
fr.close()

# + Convertimos las temperaturas en texto a numeros
print('+ Convirtiendo texto en enteros...')
Cdeg=[eval(e) for e in Cdegtext]
print('  Cdeg = ' + str(Cdeg))

########## Opcion 2
'''
# + Abrimos el fichero de entrada y leemos los datos
print('+ Abriendo el fichero \'' + ficheroEntrada + '\' para lectura...')
fr=open(ficheroEntrada, 'r')

#+ Leyendo y convirtiendo temperaturas en grados...')
print('+ Leyendo y convirtiendo temperaturas en grados...')
Cdeg = []
Cdegtext = fr.readline() #Ojo que estaran en modo texto
while Cdegtext != '':
    Cdeg.append(eval(Cdegtext))
    Cdegtext = fr.readline()
# + Cerrando fichero de entrada
print('+ Cerrando el fichero de entrada...')
fr.close()
print('  Cdeg = ' + str(Cdeg))
'''



#---------------------------------
# (2) Realizar los calculos
#---------------------------------
# + Convertimos la temperatura a Farenheit
print('+ Convirtiendo grados centigrados en Farenheit...')
Fdeg=[9./5.*e + 32 for e in Cdeg]
print('  Fdeg = ' + str(Fdeg))





#---------------------------------
# (3) Mostar la informacion
#---------------------------------
# + Abrimos el fichero de salida y escribimos los datos
print('+ Abriendo el fichero \'' + ficheroSalida + '\' para escritura...')
fw=open(ficheroSalida, 'w')

# + Guardamos la lista en el fichero
print('+ Escribiendo las temperaturas en \'' + ficheroSalida + '\'...')
fw.write('%6s\t%6s\n'%('Cdeg','Fdeg'))
for i in range(len(Cdeg)):
    fw.write('%6.1f\t%6.1f\n'%(Cdeg[i],Fdeg[i]))

# + Cerrando ficheros
print('+ Cerrando el fichero de salida...')
fw.close()

# + Mensaje final
print('+ HECHO!')
