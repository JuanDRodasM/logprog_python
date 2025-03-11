#coding=utf-8

"""
===============================================================================
 Programa: CodigoMurcielago
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Demostrar que una cadena de caracteres se puede manipular como una lista

- Se remplaza en una frase los caracteres que estén en la palabra "murcielago"
por las cifras equivalentes "0123456789"
 ===============================================================================
"""

#Definimos una función que cifra en "murcielago" la letra suministrada
#Si la letra no está en murcielago, se devuelve el mismo valor
def cifrar_murcielago_letra(una_letra):
    letra_cifrada = ''
    if una_letra == 'm':
        letra_cifrada = '0'
    elif una_letra == 'u' or una_letra == 'ú':
        letra_cifrada = '1'
    elif una_letra == 'r':
        letra_cifrada = '2'
    elif una_letra == 'c':
        letra_cifrada = '3'
    elif una_letra == 'i' or una_letra == 'í':
        letra_cifrada = '4'
    elif una_letra == 'e' or una_letra == 'é':
        letra_cifrada = '5'
    elif una_letra == 'l':
        letra_cifrada = '6'
    elif una_letra == 'a' or una_letra == 'á':
        letra_cifrada = '7'
    elif una_letra == 'g':
        letra_cifrada = '8'
    elif una_letra == 'o' or una_letra == 'ó':
        letra_cifrada = '9'
    else:
        letra_cifrada = una_letra

    return letra_cifrada

#Definimos una función que cifra la totalidad de la frase
def cifrar_murcielago_frase(una_frase):
    lista_letras_cifradas = []
    for letra in una_frase:
        lista_letras_cifradas.append(cifrar_murcielago_letra(letra))

    return ''.join(lista_letras_cifradas)

#La función principal
print('Programa para demostrar el funcionamiento y manipulación de una lista')

una_frase = input('Ingresa una frase a codificar: ').lower()
print(f'La frase ingresada tiene {len(una_frase)} caracteres')

una_frase_cifrada = cifrar_murcielago_frase(una_frase)
print(f'\nFrase Original: {una_frase} \nFrase Cifrada: {una_frase_cifrada}')

print('\nLa frase letra por letra es:')
for posicion in range(0,len(una_frase)):
    print(f'Letra: {una_frase[posicion]} \t crifrado: {cifrar_murcielago_letra(una_frase[posicion])}')