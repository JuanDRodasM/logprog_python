# coding=utf-8

"""
===============================================================================
 Programa: IdentificaPalindromos
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Validar si una cadena de caracteres es un palíndromo, utilizando al menos tres métodos diferentes

- Manera 1: usar listas y ciclos for
- Manera 2: usar una lista y reversarla
- Manera 3: usar la técnica de slicing

Definición en wikipedia:
https://es.wikipedia.org/wiki/Pal%C3%ADndromo
===============

"""
# Esta función reversa una cadena de caracteres haciendo slicing
def reversar_frase_metodo3(dato_frase):
    datos_procesados = dato_frase[::-1]
    return datos_procesados

# Esta función reversa una cadena de caracteres, reversando su lista equivalente
def reversar_frase_metodo2(dato_frase):
    lista_frase = list(dato_frase)
    lista_frase.reverse()

    # Terminamos el procesamiento reconstruyendo la frase
    datos_procesados = ''.join(lista_frase)
    return datos_procesados

# Esta funcion reversa una cadena de caracteres usando listas y ciclos for
def reversar_frase_metodo1(dato_frase):
    letras_reversadas = []

    # Reversamos la lista utilizando ciclos for desde el final hasta el inicio
    # Utilizamos la longitud de la frase - len(dato_frase)
    # El límite inferior del rango -1 para llegue hasta el indice 0
    # El límite superior se le resta 1 para que no se desborde el maximo indice
    # Como es un ciclo decremental, el paso es -1
    for indice in range(len(dato_frase) - 1, -1, -1):
        letras_reversadas.append(dato_frase[indice])

    # Terminamos el procesamiento reconstruyendo la frase
    datos_procesados = ''.join(letras_reversadas)
    return datos_procesados

# Esta función procesa la frase quitando espacios, caracteres de
# puntuación, y acentos.
def procesar_frase(dato_frase):
    letras_procesadas = []

    # Recorremos la frase como una lista de caracteres
    for letra in dato_frase:
        # Si tiene espacios o signos de puntuación, los ignoramos
        if letra in [' ', ',', '.', ';', ':', '!']:
            continue

        # Si tiene acentos, los reemplazamos por su equivalente sin acentos
        if letra in ['á', 'é', 'í', 'ó', 'ú']:
            if letra == 'á':
                letras_procesadas.append('a')

            if letra == 'é':
                letras_procesadas.append('e')

            if letra == 'í':
                letras_procesadas.append('i')

            if letra == 'ó':
                letras_procesadas.append('o')

            if letra == 'ú':
                letras_procesadas.append('u')

            continue

            # Si no hace parte de esos casos especiales, lo agregamos a la lista
        letras_procesadas.append(letra)

    # Terminamos el procesamiento reconstruyendo la frase
    datos_procesados = ''.join(letras_procesadas)
    return datos_procesados


# Aquí viene la parte principal
print('Programa para validar si una cadena de caracteres es un palíndromo\n')

una_frase = input('Ingrese una frase: ').lower()
print(f'\nProcesando la frase: {una_frase} ...')

frase_procesada = procesar_frase(una_frase)
print(f'\nLa frase procesada es: {frase_procesada}')

print('\n1. Rerversando la frase procesada por el método de listas y ciclos for')
frase_reversada = reversar_frase_metodo1(frase_procesada)
print(f'\tLa frase reversada por el método 1: {frase_reversada}')

print('\n2. Rerversando la frase procesada usando método reverse de la lista')
frase_reversada = reversar_frase_metodo2(frase_procesada)
print(f'\tLa frase reversada por el método 2: {frase_reversada}')

print('\n3. Rerversando la frase procesada usando método de slice')
frase_reversada = reversar_frase_metodo3(frase_procesada)
print(f'\tLa frase reversada por el método 3: {frase_reversada}')

# Aqui comparamos si ambas frases son iguales
if frase_procesada == frase_reversada:
    print('\n *** La frase es un palíndromo *** ')
else:
    print('\n *** La frase no es un palíndromo ***')

