#coding=utf-8

"""
===============================================================================
 Programa: NumerosAmigos
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Identificar si un número entero de tres cifras es narcisista

un número narcisista es aquel que es igual a la suma de sus dígitos elevados
a la potencia de su número de cifras.
https://es.wikipedia.org/wiki/N%C3%BAmero_narcisista

Ejemplos: 153 370 371 407
===============================================================================

"""

# Función que calcula la suma del cubo de las cifras
def obtener_suma_cubo_cifras(numero):
    centenas = numero // 100
    decenas = (numero - (centenas*100)) // 10
    unidades = numero - (centenas*100) - (decenas*10)

    suma = centenas**3 + decenas**3 + unidades**3
    return suma

# Función principal
print('Programa para identificar si un numero entero de tres cifras es narcisista\n');

datos_correctos = False
while not datos_correctos:
    try:
        numero = int(input('Ingresa un numero entero positivo de 3 cifras: '))
        # Validamos que sea entero positivo hasta 3 cifras
        if 99 < numero < 1000:
            datos_correctos = True
        else:
            print('El dato ingresado no es un entero positivo de 3 cifras. Intenta nuevamente! \n\n')

    except ValueError:
        print('El dato ingresado no es válido. Intenta nuevamente\n')

#aqui validamos la suma del cubo de sus cifras
suma_cubos = obtener_suma_cubo_cifras(numero)

if numero == suma_cubos:
    print(f'{numero} es un número narcisita. ',end="")
else:
    print(f'{numero} no es número narcisista. ', end="")

print(f'La suma de los cubos de sus cifras es {suma_cubos}')