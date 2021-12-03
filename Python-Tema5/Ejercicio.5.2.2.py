#nMax=1000

nMax = input("Hasta que numero quieres buscar multiplos de 11 y 13? ")


# Opcion 1
print("Usando la primera opcion:")
n=1
while n<nMax:
    if n%11 == 0 and n%13 == 0:
        print(str(n) + ' es divisible por 11 y por 13')
    n+=1

# Opcion 2
print("Usando la segunda opcion:")
n=1
while (n*11*13 < nMax):
    print('%d es divisible por 11 y por 13'%(n*11*13))
    n+=1
