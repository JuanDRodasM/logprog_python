#coding=utf-8

"""
===============================================================================
 Programa: NumerosAmigos
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Crear una aplicación de consola que identifique si dos números enteros son amigos
- Validar si los datos ingresados son correctos
- Implementar una función que obtenga la suma de los divisores de un número

Para información sobre el concepto de números amigos:
https://es.wikipedia.org/wiki/N%C3%BAmeros_amigos

 ===============================================================================
"""

# Definición de la función obtener_suma_divisores
def obtener_suma_divisores(numero):
    suma = 0

    #Aqui se utiliza el operador residuo para validar si el divisor es exacto
    for divisor in range(1,numero):
        if(numero % divisor == 0):
            suma += divisor

    return suma

print('Programa para identificar si dos números enteros A y B son amigos')

datos_correctos = False
while not datos_correctos:
    try:
        numero_a = int(input('Ingresa un número entero para la posición A: '))
        numero_b = int(input('Ingresa un número entero para la posición B: '))

        datos_correctos = True
    except ValueError:
        print('Los datos ingresados no son válidos. Intenta nuevamente\n')

suma_divisores_a = obtener_suma_divisores(numero_a)
suma_divisores_b = obtener_suma_divisores(numero_b)

print(f'La pareja ingresada es ({numero_a},{numero_b})')
print(f'La suma de los divisores para {numero_a} es {suma_divisores_a}')
print(f'La suma de los divisores para {numero_b} es {suma_divisores_b}')

#Validamos si los números son amigos
if suma_divisores_a == numero_b and suma_divisores_b == numero_a:
    print('Ambas sumas equivalen al otro número. Son números amigos')
else:
    print('Las sumas de los divisores no corresponden al otro número. No son números amigos')

print('\n*** Fin del programa ***')