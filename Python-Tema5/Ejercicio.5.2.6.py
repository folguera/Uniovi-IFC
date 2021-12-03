#Temperaturas en grados centigrados
Tmin=-20
Tmax=40
TPaso=5
Cdeg=list(range(Tmin, Tmax+1, TPaso))


Fdeg=[]
i=0
while i < len(Cdeg):
    Fdeg.append(9./5.*Cdeg[i] + 32)
    i+=1;

print('Grados centigrados:')
print(Cdeg)
print('Grados Farenheit:')
print(Fdeg)

