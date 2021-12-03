##############################################################################
# Ejercicio 5.3.2: Muestra una tabla con valores de temperatura en grados
# centigrados y en grados Farenheit en un intervalo determinado
##############################################################################

# + Pedimos la temperatura minima y maxima
Tmin=int(input('Introduce el valor minimo de la Temperatura: '))
Tmax=int(input('Introduce el valor maximo de la Temperatura: '))
# + Fijamos el paso
Tpaso=5

# + Generamos la lista
print('+ Generando temperaturas entre %d y %d en intervalos de %d...'%(Tmin,Tmax,Tpaso))
Cdeg=range(Tmin, Tmax+1, Tpaso)
print(Cdeg)


# + Convertimos la temperatura a Farenheit
print('+ Convirtiendo grados centigrados en Farenheit...')
Fdeg = [9./5.*ctemp + 32 for ctemp in Cdeg]
print(Fdeg)

# + Imprimimos la tabla
print('+ Mostrando la tabla...')
print('%6s\t%6s'%('Cdeg','Fdeg'))
for i in range(len(Cdeg)):
    print('%6d\t%6.1f'%(int(Cdeg[i]),Fdeg[i]))
                    
                    
