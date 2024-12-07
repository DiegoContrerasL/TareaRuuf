def cantidadPaneles(a: int, b: int, x: int, y: int):

    # Sin posibilidad de ubicar paneles
    if min(a,b) > min(x,y):
        return 0
    
    # Definir base de conteo
    mayorCantidad = 0

    # Determinar cual dimensión pobla mejor el lado "x"
    if x//a > x//b:
        # Añadir los paneles posibles en multiplicación directa
        mayorCantidad += ((x//a) * (y//b))

        #Ver si el lado contrario calza en el sobrante inferior del techo
        if y%b >= a:
            #Añadir los nuevos paneles bajo esta dimensión
            mayorCantidad += (((y%b)//a) * (x//b))
    else:
        # Añadir los paneles posibles en multiplicación directa
        mayorCantidad += ((x//b) * (y//a))

        #Ver si el lado contrario calza en el sobrante inferior del techo
        if y%a >= b:
            #Añadir los nuevos paneles bajo esta dimensión
            mayorCantidad += (((y%a)//b) * (x//a))

    # Retornar la cantidad total de paneles
    return mayorCantidad

print("Ejemplo 1",cantidadPaneles(1,2,2,4))
print("Ejemplo 2",cantidadPaneles(1,2,3,5))
print("Ejemplo 3",cantidadPaneles(2,2,1,10))