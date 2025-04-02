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
- Método 4: Nativo Python (sorted)

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
    print()

#Ordena una lista utilizando el método burbuja
def ordena_lista_burbuja(la_lista):
    la_lista = la_lista.copy() # Creamos una copia local de la lista

    hubo_cambios = True #Valor inicial de la variable de control
    total_recorridos = 0
    total_cambios = 0 # Variable de control

    while hubo_cambios is True: # Condición de repetición
        hubo_cambios = False #Cada ciclo modificamos variable de control, asumiendo no cambios
        for i in range(len(la_lista) -1):
            if la_lista[i] > la_lista[i+1]:
                total_cambios += 1
                print(f'Cambio No. {total_cambios}. Se cambiará de lugar el {la_lista[i]} y el {la_lista[i+1]}')
                la_lista[i],la_lista[i+1] = la_lista[i+1], la_lista[i] #Intercambio de posición
                hubo_cambios = True

        if hubo_cambios is True:
            total_recorridos +=1
            print(f'Fin del recorrido {total_recorridos} \n')

    print(f'Usando el algoritmo burbuja, se hicieron {total_cambios} cambios de posición en {total_recorridos} recorridos')
    return la_lista

#Ordena una lista utilizando el método selección
def ordena_lista_seleccion(la_lista):
    la_lista = la_lista.copy()  # Creamos una copia local de la lista

    total_cambios = 0
    for i in range(len(la_lista)):
        indice_minimo = i
        for j in range (i+1,len(la_lista)):
            if la_lista[j] < la_lista[indice_minimo]:
                indice_minimo = j

        if i != indice_minimo:
            total_cambios += 1
            print(f'Cambio No. {total_cambios}. Se cambiará de lugar el {la_lista[i]} y el {la_lista[indice_minimo]}')
            la_lista[i], la_lista[indice_minimo] = la_lista[indice_minimo],la_lista[i]  #Intercambio de posición

    print(f'\nUsando el algoritmo de selección, se hicieron {total_cambios} cambios de posición')
    return la_lista

#Ordena una lista utilizando el método inserción
def ordena_lista_insercion(la_lista):
    la_lista = la_lista.copy()  # Creamos una copia local de la lista

    total_cambios = 0
    for i in range(1, len(la_lista)):
        valor_actual = la_lista[i]
        j = i - 1
        while j >= 0 and la_lista[j] > valor_actual:
            total_cambios += 1
            print(f'Cambio No. {total_cambios}. Se cambiará de lugar el {la_lista[j]} y el {la_lista[j + 1]} ')
            la_lista[j + 1] = la_lista[j]  # Desplazamos el elemento a la derecha
            j -= 1

        # Colocamos el valor actual en su posición correcta
        la_lista[j + 1] = valor_actual

    print(f'\nUsando el algoritmo de inserción, se hicieron {total_cambios} cambios de posición')
    return la_lista

#Ordena una lista utilizando el método nativo python
def ordena_lista_nativo(la_lista):
    return sorted(la_lista)

print('programa para demostrar el funcionamiento de métodos de ordenamiento \n')
longitud_lista = 5
limite_inferior = 1
limite_superior = 99
los_numeros = []

for posicion in range(longitud_lista):
    dato = random.randint(limite_inferior, limite_superior)
    los_numeros.append(dato)

print(f'La lista actual tiene {len(los_numeros)} valores')
visualizar_lista(los_numeros)

#Ordenación usando el método burbuja
print('\nLa lista ordenada usando el algoritmo burbuja:')
lista_ordenada = ordena_lista_burbuja(los_numeros)
visualizar_lista(los_numeros)
print('Después de ordenamiento')
visualizar_lista(lista_ordenada)

#Ordenación usando el método de selección
print('\nLa lista ordenada usando el algoritmo de selección:')
lista_ordenada = ordena_lista_seleccion(los_numeros)
visualizar_lista(los_numeros)
print('Después de ordenamiento')
visualizar_lista(lista_ordenada)

#Ordenación usando el método de inserción
print('\nLa lista ordenada usando el algoritmo de inserción:')
lista_ordenada = ordena_lista_insercion(los_numeros)
visualizar_lista(los_numeros)
print('Después de ordenamiento')
visualizar_lista(lista_ordenada)

#Usando el método nativo de python
lista_ordenada = ordena_lista_nativo(los_numeros)
print('\nLa lista ordenada usando el método SORTED de la lista:')
visualizar_lista(los_numeros)
print('Después de ordenamiento')
visualizar_lista(lista_ordenada)

