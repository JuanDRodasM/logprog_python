#coding=utf-8

"""
===============================================================================
 Programa: EjemploListas
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Demostración inicial del funcionamiento y manipulación de elementos de una lista

 ===============================================================================
"""

print('Programa para demostrar el funcionamiento y manipulación de una lista')

una_lista = [10, 20, 15, 40, 0, -30,10]
print('Mi lista tiene los valores: ', una_lista)
print(f'Mi lista tiene {len(una_lista)} valores')

# Usando un ciclo for "simplificado"
print('\nMi lista colocando un elemento por linea usando un ciclo for simplificado es:')
for elemento in una_lista:
    print(elemento)

# Usando un ciclo for "elaborado"
print('\nMi lista colocando un elemento por linea usando un ciclo for elaborado es:')
for elemento in range(0,len(una_lista)):
    print(f'En la posición {elemento} está el valor {una_lista[elemento]}')

#Cambiar el valor de un elemento de la lista
una_lista[3] = 10
print('\nLa lista con elemento actualizado es ',una_lista)

#Agregar un nuevo elemento al final de la lista
una_lista.append(12)
print('\nLa lista con elemento adicionado al final es ',una_lista)

# Usando un ciclo While "enredado"
print('\nMi lista colocando un elemento por linea usando un ciclo while es:')
posicion = 0
while posicion <len(una_lista):
    print(f'En la posición {posicion} está el valor {una_lista[posicion]}')
    posicion+=1

#Remover un elemento de la lista
una_lista.remove(10)
print('\nLa lista con elemento removido es ',una_lista)

#Remover un elemento de una posicion específica
una_lista.pop(3)
print('\nLa lista con elemento "popeado" es ',una_lista)

# Extender una lista agregando más elementos
una_lista.extend([5,1000,-24])
print('\nLa lista extendida es ',una_lista)