nMax=eval(input("¿Hasta donde quieres llegar? "))


# Opcion 1
print("Usando la primera opcion:")

a = [] # Creamos una lista vacía
n = 1  # Contador
while n <= nMax:
    if n%11 == 0 and n%13 == 0:
        a.append(n)
    n+=1

# Se podria imprimir directamente asi
# print(a)

# O darle algo de formato asi
i = 0
while (i < len(a)):
	print("%4d es multiplo de 11 y 13"%a[i])
	i+=1
	



# Opcion 2
print('='*40)
print("Usando la segunda opcion:")

b = [] # Creamos una lista vacía
n = 1  # Reseteamos el contador

# Bucle
while (n*11*13 <= nMax):
    b.append(n*11*13)
    n+=1

# Se podria imprimir directamente asi
#print(a)

# O darle algo de formato asi
i = 0
while (i < len(a)):
	print("%4d es multiplo de 11 y 13"%b[i])
	i+=1
	
