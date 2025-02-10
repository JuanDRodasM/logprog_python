#coding=utf-8

# ============================
# Programa:       EjemploCicloWhile
# Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

# Propósito:
# ----------
#- Demostrar el funcionamiento del ciclo de control While, generando una tabla de multiplicar.
#- Demostrar como funciona la sentencia break para interrumpir la ejecución de un ciclo

# ============================


# Programa para imprimir los numeros del 1 al 10

print('Programa para imprimir los numeros del 1 al 10')

# Partes de un ciclo de control
# 1. Variable de control
# 2. Condicion de repetición
# 3. sentencia de salida


# Imprimir los primeros n multiplos de 7

print('Programa que visualiza una cantidad de multiplos de 7\n')
total_multiplos = int(input('Ingrese la cantidad de multiplos a visualizar: '))

if total_multiplos > 0:
    contador = 1
    while contador <= total_multiplos:
        print(f'7 x {contador} = {contador * 7}')
        contador += 1
else:
    print('El numero ingresado no es valido. Debe ser positivo')


print('\nPrograma para imprimir los números enteros')
print('hasta llegar la primer multiplo de 5')

numero = 1
while numero <= 10:
    # El ciclo se detiene si se encuentra el primer
    # multiplo de 5
    if (numero % 5 == 0):
        print(numero)
        break

    print(numero)
    numero += 1  # Es lo mismo que numero = numero + 1

print(f'\nLa variable numero terminó con el valor {numero}')