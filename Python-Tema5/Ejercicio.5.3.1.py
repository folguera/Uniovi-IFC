#Temperaturas en grados centigrados
Tmin=input('Introduce el valor minimo de la Temperatura: ')
Tmax=input('Introduce el valor maximo de la Temperatura: ')
TPaso=5
Cdeg=range(Tmin, Tmax+1, TPaso)


Fdeg=[9./5.*e + 32 for i,e in enumerate(Cdeg)]

print('Grados centigrados:')
print(Cdeg)
print('Grados Farenheit:')
print(Fdeg)

