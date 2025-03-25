#coding=utf-8

"""
===============================================================================
 Programa: EjemploDiccionarios
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Demostración inicial del funcionamiento y manipulación de un diccionario

 ===============================================================================
"""

def visualizar_diccionario(dato_diccionario):
    print(f'El diccionario tiene {len(dato_diccionario)} elementos')

    print('Estas son las palabras que tiene:')
    for llave in list(un_dicicionario.keys()):
        print(f'{llave}: \n\t {un_dicicionario[llave]}')


print('Programa para demostrar el funcionamiento y manipulación de un diccionario')

un_dicicionario = {
    "zapato" : "Prenda de vestir que se usa en los pies",
    "morcilla": "Comida autóctona de Colombia",
    "Computador": "Dispositivo electrónico de procesamiento de informacion",
    "Miguel": "Estudiante que llega DEMASIADO tarde"
}

print(f'El diccionario tiene un tamaño de {len(un_dicicionario)} elementos')

las_llaves = list(un_dicicionario.keys())

print('\nEstas son las palabras que contiene:')
for llave in las_llaves:
    print(llave)

print('\nEstas son las definiciones que tiene nuestro diccionario:')
visualizar_diccionario(un_dicicionario)

nueva_llave = input('\n\nIngresa una palabra para incluir en el diccionario: ')
nueva_definicion = input('Ingresa la definición de la palabra: ')

un_dicicionario[nueva_llave] = nueva_definicion

print(f'El diccionario ahora tiene un tamaño de {len(un_dicicionario)} elementos')

print('\nEstas son las definiciones que tiene nuestro diccionario:')
visualizar_diccionario(un_dicicionario)

print('Aqui cambiamos el valor de un registro existente en el diccionario')
un_dicicionario['Miguel'] = 'No fue el estudiante que llegó MAS TARDE!'

visualizar_diccionario(un_dicicionario)
