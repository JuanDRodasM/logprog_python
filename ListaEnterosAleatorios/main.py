#coding=utf-8

"""
===============================================================================
 Programa: ListaEnterosAleatorios
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Demostración del uso de listas con funciones
- Generar numeros aleatorios y visualizarlos de manera tabulada
- Obtener la lista de numeros pares e impares
- Ordenar las listas resultantes
 ===============================================================================
"""

import random

#Visualiza la lista de manera tabulada, 10 valores por línea
def visualizar_lista(la_lista):
    for posicion in range(0, len(la_lista)):
        if (posicion+1) % 10 ==0:
            print(f'{la_lista[posicion]}')
        else:
            print(la_lista[posicion],'\t', end="")
    print()

# Obtiene una lista de numeros pares incluida en la lista parámetro
def obtener_lista_pares(la_lista):
    lista_numeros_pares = []
    for i in range(0,len(la_lista)):
        if la_lista[i] % 2 ==0:
            lista_numeros_pares.append(la_lista[i])

    return lista_numeros_pares

# Obtiene una lista de numeros impares incluida en la lista parámetro
def obtener_lista_impares(la_lista):
    lista_numeros_impares = []
    for i in range(0,len(la_lista)):
        if la_lista[i] % 2 !=0:
            lista_numeros_impares.append(la_lista[i])

    return lista_numeros_impares

# Aqui es la función principal
print('Programa para generar una lista de 100 números enteros aleatorios \n')

#Aqui generamos la lista
la_lista = []
for i in range(0,100):
    numero = random.randint(0, 99)
    la_lista.append(numero)

print(f'La lista generada es:')
visualizar_lista(la_lista)

#Aqui encontramos la sublista de los numeros pares
lista_pares = obtener_lista_pares(la_lista)
print(f'\n\nLa lista con los números pares es:')
visualizar_lista(lista_pares)

#Aquí encontramos la sublista de los numeros impares
lista_impares = obtener_lista_impares(la_lista)
print(f'\n\nLa lista con los números impares es:')
visualizar_lista(lista_impares)

print(f'\n\nLa lista con los números impares, ordenada ascendentemente es:')
#Ordenar con sort() altera el orden de los elementos de la lista
lista_impares.sort()
visualizar_lista(lista_impares)

print(f'\n\nLa lista con los números pares, ordenada descendentemente es:')
#Ordenar con sorted() genera una copia de la lista sin afectar la original
lista_pares_descendentes = sorted(lista_pares, reverse=True)
visualizar_lista(lista_pares_descendentes)

print(f'\n\nLa lista con los números pares original es:')
visualizar_lista(lista_pares)

