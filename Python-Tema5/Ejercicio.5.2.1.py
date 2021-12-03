#Resolucion de ecuaciones de segundo grado. 

a = eval(input('Introduce a: ')) #Pedir parámetros a,b,c
b = eval(input('Introduce b: '))
c = eval(input('Introduce c: '))

# Comprobamos que se trate de una ecuación de segundo grado
if a == 0:
    print('Error: Ecuación sin término x²')

# A partir de aquí asumimos que es una ec. de segundo grado  
else:
    # Calcular el discriminante
    d = (b**2)-(4*a*c) #Cálculo del discriminante.

    # Calculamos la primera parte de la solución
    p1 = -b/(2*a)
    
    # Mostramos las soluciones en función del signo del discriminante
    if d < 0:
        # Calculamos la segunda parte de la solución
        p2 = ((-d)**(0.5))/(2*a)
        
        # + Guardamos los valores por si fueran necesarios más adelante
        x1 = p1 + p2*1j # Número complejo
        x2 = p1 - p2*1j # Número complejo
        
        # + Imprimimos los resultados con cierto formato
        print('La ecuación tiene dos soluciones complejas')
        print('x1 = %.2f + %.2fi'%(p1, p2))
        print('x2 = %.2f - %.2fi'%(p1, p2))
    elif d > 0:
        # Calculamos la segunda parte de la solución
        p2 = (d**(0.5))/(2*a)
        
        # + Guardamos los valores por si fueran necesarios más adelante
        x1 = p1 + p2
        x2 = p1 - p2
        # + Imprimimos los resultados con cierto formato
        print('La ecuación tiene dos soluciones reales')
        print('x1 = %.2f'%x1)
        print('x2 = %.2f'%x2)
    else:
        # + Guardamos los valores por si fueran necesarios más adelante
        x1 = x2 = p1
        # + Imprimimos los resultados con cierto formato
        print('La ecuación tiene una solución real (degenerada)')
        print('x = %10.2f'%x1)
        
    # Comprobación
    print('Vamos a comprobar los resultados')
    ec1 = a*x1*x1 + b*x1 + c
    ec2 = a*x2*x2 + b*x2 + c
    print('Sustituyendo la primera solución en la ecuación se obtiene ' + str(ec1))
    print('Sustituyendo la segunda solución en la ecuación se obtiene ' + str(ec2))
