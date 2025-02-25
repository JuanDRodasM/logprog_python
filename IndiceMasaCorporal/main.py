# ======================================================================
# Programa:       AnalisisTemperatur
# Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

# Propósito:
# ----------
# Programa para calcular el indice de masa corporal a partir del
# peso en Kg y la estatura en m

print('Programa para calcular el indice de masa corporal\n')

# Variable de control, con valor que permite iniciar el ciclo
ocurrio_error = True

# Variables del problema
while ocurrio_error is True:
    try:
        peso = float(input('\nIngrese su peso en kg: '))
    except ValueError:
        print('El peso ingresado no es un numero. Intenta nuevamente')
        ocurrio_error = True
        continue

    try:
        estatura = float(input('Ingrese su estatura en metros: '))
    except ValueError:
        print('El estatura ingresada no es un numero. Intenta nuevamente')
        ocurrio_error = True
        continue

    indice = peso / (estatura ** 2)

    print(f'\nSu indice de masa corporal es: {indice:.2f}')

    if indice < 18.5:
        print('Usted tiene bajo peso')
    elif (indice >= 18.5 and indice < 25):
        print('Usted tiene un peso normal')
    elif (indice >= 25 and indice < 30):
        print('Usted tiene sobrepeso')
    else:
        print('Usted tiene obesidad')

    # Cuando la operación se completa exitosamente
    # Esta es la clausula de salida que rompe el ciclo while
    ocurrio_error = False
