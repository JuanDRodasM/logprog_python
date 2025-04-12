#coding=utf-8
"""
===============================================================================
 Programa: Ex03_PedidosPasteleria
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Aplicación de listas y diccionarios para simular la gestión de pedidos de pastelería
- Se debe identificar la categoría mayor y a cual porcentaje corresponde
- Se visualizan resultados
 ===============================================================================
"""

#Función que identifica la categoría que tiene la mayor cantidad de productos
def identifica_categoria_mayor(un_diccionario):
    #Obtenemos una lista con las llaves del diccionario
    las_categorias = list(un_diccionario.keys())

    #Asumimos que la categoría mayor es la primera de las llaves
    categoria_identificada = las_categorias[0]

    #Asumimos que el mayor valor es el asociado a esa llave
    valor_mayor_encontrado = un_diccionario[categoria_identificada]

    #Recorremos el diccionario con el resto de las llaves
    for indice in range(1,len(las_categorias)):
        #Si el valor asociado a esa llave en el diccionario es mayor que el valor encontrado
        #Ese será el nuevo valor mayor y esa será la categoría mayor
        if un_diccionario[las_categorias[indice]] > valor_mayor_encontrado:
            valor_mayor_encontrado = un_diccionario[las_categorias[indice]]
            categoria_identificada = las_categorias[indice]

    return categoria_identificada

#Función que identifica el porcentaje del total de productos asociados a una categoria
def obtiene_porcentaje_categoria(un_diccionario, una_categoria):

    #Totalizamos los productos de la orden
    total_productos_orden = 0
    for categoria in un_diccionario.keys():
        total_productos_orden += un_diccionario[categoria]

    #calculamos el porcentaje
    porcentaje = (un_diccionario[una_categoria] / total_productos_orden) * 100
    return porcentaje


#Función que visualiza el contenido de un diccionario
def visualiza_diccionario(un_diccionario):
    print('\nEl registro de pedidos está asi:')
    for categoria in un_diccionario.keys():
        print(f'\t- {categoria}: {un_diccionario[categoria]}')

#Función Principal
print('Gestión de Pedidos para pastelería - Éclairs del Alma')

#variables a utilizar
diccionario_pedidos = {
    'Tortas' : 0,
    'Postres' : 0,
    'Panadería' : 0,
    'Bebidas': 0,
    'Decoraciones' : 0
}

#Aqui ingresamos los datos de cada uno de los productos
for categoria in diccionario_pedidos.keys():
    dato_correcto = False
    while dato_correcto is False:
        try:
            diccionario_pedidos[categoria] = int(input(f'\nIngresa la cantidad de productos para la categoría {categoria}: '))
            if diccionario_pedidos[categoria] <0:
                print('El dato de la cantidad debe ser un entero positivo. Intente nuevamente')
                continue

            dato_correcto = True;
        except ValueError:
            print('El dato ingresado está en formato inválido. Intente nuevamente.')

visualiza_diccionario(diccionario_pedidos)

#Aquí invocamos las funciones
categoria_identificada = identifica_categoria_mayor(diccionario_pedidos)
porcentaje_categoria_mayor = obtiene_porcentaje_categoria(diccionario_pedidos,categoria_identificada)

#Visualización de resultados
print('\n*** Resultados obtenidos ***')
print(f'La categoría con más productos es {categoria_identificada}')
print(f'Representa el {porcentaje_categoria_mayor:.2f} % de los productos de la orden')