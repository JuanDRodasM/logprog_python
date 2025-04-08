import random

from Rec01_EmpanadasGourmet.main import porcentaje

#coding=utf-8
"""
===============================================================================
 Programa: MaterialesConstruccion
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Aplicación de listas y diccionarios para simular la generación de ordenes de materiales de construcción
- Se deben identificar ordenes nulas (sin productos) y prioritarias (todos los productos)
- Se visualizan resultados
 ===============================================================================
"""

#Aqui definimos la función que calcula el total de ordenes según el criterio
def calcula_total_ordenes(un_diccionario, un_criterio):
    total_ordenes = 0

    #Aqui definimos el valor buscado según el criterio
    if un_criterio == 'nula':
        valor_buscado = 0
    elif un_criterio == 'prioritaria':
        valor_buscado = 10

    #Aqui identificamos cuantas categorías se revisarán, que pueden ser las de la primera orden
    primera_llave = '1'
    total_categorias = len(un_diccionario[primera_llave].keys())

    #Aqui buscamos cuantas ordenes tienen en TODAS sus categorías el valor buscado
    for orden in un_diccionario.keys():
        valores_encontrados = 0

        #Aqui revisamos para cada categoria, si tiene el valor buscado
        for categoria in un_diccionario[orden].keys():
            if un_diccionario[orden][categoria] == valor_buscado:
                valores_encontrados +=1

        #Si la cantidad de valores encontrados coicide con la cantidad de categorias
        #Esa orden cumple con el criterio de contabilizacion
        if valores_encontrados == total_categorias:
            total_ordenes += 1

    return total_ordenes

#Función Principal
categorias = ['Cimentación','Estructura','Techos','Acabados','Tuberías']
total_ordenes = 1000
cantidad_minima = 0
cantidad_maxima = 10

print('Programa para simular la generación de ordenes de materiales de construcción')
print(f'Se simularán {total_ordenes} en las siguientes categorias:')

for categoria in categorias:
    print(f'- {categoria}')

#Aqui definimos el diccionario de las ordenes
diccionario_ordenes = {}

#Aqui generamos 1000 ordenes
print('\nDetalle de las ordenes simuladas:')
for orden in range(total_ordenes):
    pedido = {}
    for una_categoria in categorias:
        cantidad = random.randint(cantidad_minima, cantidad_maxima)
        pedido[una_categoria] = cantidad

    #Colocamos el número de orden como una cadena de caracteres
    # para que funcione como llave del diccionario
    diccionario_ordenes[str(orden+1)] = pedido

print(f'El diccionario de ordenes tiene {len(diccionario_ordenes)} ordenes')

#Visualizamos el contenido del diccionario
for llave in diccionario_ordenes.keys():
    print(f'Orden No. {llave}:')
    for categoria_producto in diccionario_ordenes[llave]:
        print(f'\t- {categoria_producto}: {diccionario_ordenes[llave][categoria_producto]}')

total_ordenes_nulas = calcula_total_ordenes(diccionario_ordenes, 'nula')
total_ordenes_prioritarias = calcula_total_ordenes(diccionario_ordenes, 'prioritaria')

porcentaje_ordenes_nulas = (total_ordenes_nulas / total_ordenes) * 100
porcentaje_ordenes_prioritarias = (total_ordenes_prioritarias / total_ordenes) * 100

print('\n*** Resultados ***')
print(f'Total ordenes nulas: {total_ordenes_nulas}, que equivalen al {porcentaje_ordenes_nulas:.2f} %')
print(f'Total ordenes proritarias: {total_ordenes_prioritarias}, que equivalen al {porcentaje_ordenes_prioritarias:.2f} %')
