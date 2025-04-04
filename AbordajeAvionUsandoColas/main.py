from collections import deque
import random
#coding=utf-8

"""
===============================================================================
 Programa: AbordajeAvionUsandoColas
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Aplicación de una cola prioritaria para gestionar abordaje a un avión
- Se utiliza dictionary comprenhension para definir dinámicamente un diccionario

 ===============================================================================
"""

#Función para visualizar el diccionario de asignación de categorías
def visualiza_asignacion(un_diccionario):
    total_asientos = 0
    for asiento in un_diccionario.keys():
        print(f'- {asiento}: {un_diccionario[asiento]}')
        total_asientos += un_diccionario[asiento]

#Función para visualizar el orden en que los pasajeros abordarán el avión
def visualiza_abordaje(una_cola):
    for pasajero in una_cola:
        print(f'- No.: {pasajero["numero"]}, categoria: {pasajero["categoria"]}')

#Aqui empieza la función principal
print('Gestión de abordaje prioritario a un avión')

potenciales_pasajeros = 30
categorias_asientos = ['Primera Clase','Negocios','Turista','Tripulación']
#Aqui utilizamos el concepto de Dictionary Comprenhension para definir
# el diccionario dinámicamente según las categorías en la lista
diccionario_totales_asignacion = { categoria: 0 for categoria in categorias_asientos }

print(f'Se asignaron {potenciales_pasajeros} asientos en las siguientes categorias:')

#Aqui definimos la cola de abordaje
cola_abordaje = deque()

#En este ciclo le asignamos una categoría a un pasajero
for numero_asiento in range(potenciales_pasajeros):
    #seleccionamos aleatoriamente una categoria para el pasaro
    categoria_asignada = random.choice(categorias_asientos)
    #Aqui totalizamos asignaciones
    diccionario_totales_asignacion[categoria_asignada]+=1
    #Aqui lo encolamos
    pasajero = {
        "numero":       numero_asiento+1,
        "categoria":    categoria_asignada
    }
    cola_abordaje.append(pasajero)

visualiza_asignacion(diccionario_totales_asignacion)
print('\nDetalle asignación:')
visualiza_abordaje(cola_abordaje)

print('\nDe esta manera entraron al avión:')
orden_ingreso = 1
for una_categoria in categorias_asientos:
    print(f'\nPasajeros de la categoria {una_categoria}, total: {diccionario_totales_asignacion[una_categoria]}')
    for pasajero in cola_abordaje:
        if pasajero["categoria"] == una_categoria:
            print(f'Ingreso No.: {orden_ingreso}, pasajero {pasajero["numero"]} entra al avión')
            orden_ingreso+=1
