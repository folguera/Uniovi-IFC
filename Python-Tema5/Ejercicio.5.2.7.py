#Temperaturas en grados centigrados
Tmin=-20
Tmax=40
TPaso=5
Cdeg=list(range(Tmin, Tmax+1, TPaso))


Fdeg=[9./5.*e + 32 for e in Cdeg]

print('Grados centigrados:')
print(Cdeg)
print('Grados Farenheit:')
print(Fdeg)

