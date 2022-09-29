anio = int(input("Ingrese el año para saber si es bisiesto o no: "))

if anio % 4 == 0:
    if anio % 100 == 0:
        if anio % 400 == 0:
            print('El año es bisiesto')
        else:
            print('El año no es bisiesto')
    else:
        print('El año es bisiesto.')
else:
    print('El año no es bisiesto.')