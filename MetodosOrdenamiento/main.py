import random

# coding=utf-8

"""
================================================================
 Programa: MetodosOrdenamiento
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Conocer el funcionamiento de tres métodos de ordenamiento

- Método 1: Burbuja (Bubble Sort)
- Método 2: Selección (Selection Sort)
- Método 3: Inserción (Insertion Sort)

Definición en wikipedia:
https://es.wikipedia.org/wiki/Algoritmo_de_ordenamiento
================================================================

"""

#Visualiza la lista de manera tabulada, 10 valores por línea
def visualizar_lista(la_lista):
    for posicion in range(0, len(la_lista)):
        if (posicion+1) % 10 ==0:
            print(f'{la_lista[posicion]}')
        else:
            print(la_lista[posicion],'\t', end="")

def ordena_lista_burbuja(la_lista):
    hubo_cambios = True #Valor inicial de la variable de control
    total_cambios = 0
    total_recorridos = 0
    while hubo_cambios is True: # Condición de repetición
        hubo_cambios = False #Cada ciclo modificamos variable de control, asumiendo no cambios
        for i in range(len(la_lista) -1):
            if la_lista[i] > la_lista[i+1]:

                print(f'Cambio No. {total_cambios + 1}. Se cambiará de lugar el {la_lista[i]} y el {la_lista[i+1]}')

                la_lista[i],la_lista[i+1] = la_lista[i+1], la_lista[i] #Intercambio de posición
                hubo_cambios = True
                total_cambios += 1

        if hubo_cambios is True:
            total_recorridos +=1
            print(f'Fin del recorrido {total_recorridos}')

    print(f'\nUsando el algoritmo burbuja, se hicieron {total_cambios} cambios de posición en {total_recorridos} recorridos')
    return la_lista


def ordena_lista_insercion(la_lista):
    longitud = len(la_lista)
    total_cambios = 0

    for i in range(longitud):
        indice_minimo = i
        for j in range (i+1,longitud):
            if la_lista[j] < la_lista[indice_minimo]:
                indice_minimo = j

        print(f'Cambio No. {total_cambios+1}. Se cambiará de lugar el {la_lista[i]}')

        la_lista[i], la_lista[indice_minimo] = la_lista[indice_minimo],la_lista[i]  #Intercambio de posición
        total_cambios += 1


    print(f'\nUsando el algoritmo de inserción, se hicieron {total_cambios} cambios de posición')
    return la_lista

def ordena_lista_nativo(la_lista):
    return sorted(la_lista)

print('programa para demostrar el funcionamiento de métodos de ordenamiento \n')

longitud_lista = 10
limite_inferior = 1
limite_superior = 20
los_numeros = []

for posicion in range(longitud_lista):
    dato = random.randint(limite_inferior, limite_superior)
    los_numeros.append(dato)

print(f'La lista actual tiene {len(los_numeros)} valores y es:')
visualizar_lista(los_numeros)

#Ordenación usando el método burbuja
print('\nLa lista ordenada usando el algoritmo burbuja:')
lista_ordenada = ordena_lista_burbuja(los_numeros)
visualizar_lista(lista_ordenada)

#Ordenación usando el método de inserción
print('\nLa lista ordenada usando el algoritmo de inserción:')
lista_ordenada = ordena_lista_insercion(los_numeros)
visualizar_lista(lista_ordenada)

#Usando el método nativo de python
lista_ordenada = ordena_lista_nativo(los_numeros)
print('\nLa lista ordenada usando el método SORTED de la lista:')
visualizar_lista(lista_ordenada)
