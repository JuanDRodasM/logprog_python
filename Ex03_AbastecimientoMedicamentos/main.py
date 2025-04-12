#coding=utf-8
"""
===============================================================================
 Programa: Ex03_AbastecimientoMedicamentos
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Aplicación de listas y diccionarios para simular el abstecimiento de medicamentos
- Se debe identificar el modo mayor y a cual es el promedio de medicamentos por modo
- Se visualizan resultados
 ===============================================================================
"""

#Función que identifica los modos que tiene la mayor cantidad de medicamentos
def identifica_modo_mayor(un_diccionario):
    #Obtenemos una lista con las llaves del diccionario
    los_modos = list(un_diccionario.keys())

    #Asumimos que el modo mayor es el primero de las llaves
    modo_identificado = los_modos[0]

    #Asumimos que el mayor valor es el asociado a esa llave
    valor_mayor_encontrado = un_diccionario[modo_identificado]

    #Recorremos el diccionario con el resto de las llaves
    for indice in range(1,len(los_modos)):
        #Si el valor asociado a esa llave en el diccionario es mayor que el valor encontrado
        #Ese será el nuevo valor mayor y esa será el modo mayor
        if un_diccionario[los_modos[indice]] > valor_mayor_encontrado:
            valor_mayor_encontrado = un_diccionario[los_modos[indice]]
            modo_identificado = los_modos[indice]

    return modo_identificado

#Función que obtiene el promedio de medicamentos por modo en el pedido
def obtiene_promedio_medicamentos(un_diccionario):

    #Totalizamos los medicamentos del pedido
    total_productos_pedido = 0
    for modo in un_diccionario.keys():
        total_productos_pedido += un_diccionario[modo]

    #calculamos el porcentaje
    promedio = (total_productos_pedido / len(un_diccionario.keys()))
    return promedio

#Función que visualiza el contenido de un diccionario
def visualiza_diccionario(un_diccionario):
    print('\nEl contenido del pedido está asi:')
    for modo in un_diccionario.keys():
        print(f'\t- {modo}: {un_diccionario[modo]}')


#Función principal
print('Programa para simular el abastecimiento de medicamentos')

modos_empleo = [
    'Orales',
    'Oftálmicos',
    'Nasales',
    'Tópicos',
    'Inyectables']

print(f'\nLos medicamentos tienen este modo de empleo:')

for modo in modos_empleo:
    print(f'- {modo}')

#Aqui inicializamos el diccionario de pedidos usando la lista de modos de empleo
#Aqui se usa el concepto dictionary comprenhension
diccionario_pedido = {modo:0 for modo in modos_empleo}

#Aqui ingresamos los datos de cada uno de los medicamentos
for modo in diccionario_pedido.keys():
    dato_correcto = False
    while dato_correcto is False:
        try:
            diccionario_pedido[modo] = int(input(f'\nIngresa la cantidad de medicamentos para el modo {modo}: '))
            if diccionario_pedido[modo] <0:
                print('El dato de la cantidad debe ser un entero positivo. Intente nuevamente')
                continue

            dato_correcto = True;
        except ValueError:
            print('El dato ingresado está en formato inválido. Intente nuevamente.')

#Aquí visualizamos el contenido de los pedidos
visualiza_diccionario(diccionario_pedido)

#Aquí encontramos el modo mayoy el promedio de medicamentos por modo
modo_identificado = identifica_modo_mayor (diccionario_pedido)
promedio_cantidad_medicamentos = obtiene_promedio_medicamentos(diccionario_pedido)

#Visualización de resultados
print('\n*** Resultados obtenidos ***')
print(f'La categoría con más productos es {modo_identificado}')
print(f'El pedido en promedio tiene {promedio_cantidad_medicamentos} medicamentos por modo de empleo')