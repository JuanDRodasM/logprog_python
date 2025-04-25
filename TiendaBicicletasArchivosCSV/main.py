import random
import csv

#coding=utf-8
"""
===============================================================================
 Programa: TiendaBicicletasArchivosCSV
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Aplicación que almacena un diccionario de inventario de bicicletas en un
- archivo de texto plano en formato CSV (Comma Separated Values)
- La creación del diccionario se hace usando dictionary comprenhension a partir
  de listas que tienen valores para los atributos
 ===============================================================================
"""
#Función para visualizar el contenido del diccionario
def visualiza_diccionario_biciletas(un_diccionario):
    print(f'\n Total entradas: {len(un_diccionario)}. Contenido del inventario:')
    for llave in un_diccionario.keys():
        print(f'Codigo: {llave}')
        for detalle in un_diccionario[llave].keys():
            print(f'\t{detalle}: {un_diccionario[llave][detalle]}')

#Función para generar una cadena de caracteres con el encabezado del archivo
def genera_encabezado_archivo(un_diccionario):
    print('\nEl contenido del archivo será este:\n')

    #Utilizamos el primer elemento del diccionario para obtener sus llaves
    #pues serán los encabezados de las columnas
    primer_elemento = list(un_diccionario.keys())[0]
    columnas = ['Código'] + list(un_diccionario[primer_elemento].keys())
    encabezado = ';' .join(columnas) + '\n'
    return encabezado

#Función para generar una cadena de caracteres por cada elemento del diccionario
def genera_lineas_archivo(un_diccionario):
    lineas_diccionario = []
    for elemento in un_diccionario.keys():
        linea = elemento
        for detalle in un_diccionario[elemento].keys():
            linea = linea + ';' + str(un_diccionario[elemento][detalle])
        lineas_diccionario.append(linea)

    return lineas_diccionario

#Función para guardar el contenido del diccionario en un archivo de texto
def guarda_archivo_csv(un_diccionario,un_archivo_csv):

    el_encabezado = genera_encabezado_archivo(un_diccionario)
    las_lineas = genera_lineas_archivo(un_diccionario)

    with open(un_archivo_csv, 'w', encoding='utf-8') as el_archivo:
        #Escribimos en el archivo el encabezado
        el_archivo.write(el_encabezado)

        #Escribimos las líneas
        for linea_datos in las_lineas:
            el_archivo.write(linea_datos + '\n')

    print(f"Datos guardados en {un_archivo_csv}")

#Función para leer el contenido de un archivo CSV y almacenarlo en un diccionario
def lee_diccionario_desde_archivo(un_archivo_csv):
    diccionario_inventario = {}

    try:
        with open(un_archivo_csv,'r', encoding='utf-8') as el_archivo:
            lector = csv.reader(el_archivo,delimiter=';')

            #Leemos la primera linea que contiene los encabezado
            encabezado = next(lector)

            print(f'El encabezado: {encabezado}')

            #Leemos el resto de las lineas
            for fila in lector:
                if len(fila) >= 6: #Aseguramos que la fila tiene los 6 campos
                    codigo = fila[0]
                    diccionario_inventario[codigo] = {
                        'Marca': fila[1],
                        'Tamaño': fila[2],
                        'Cambios': int(fila[3]) if fila[3].isdigit() else fila[3],
                        'Color': fila[4],
                        'Tracción': fila[5]
                    }

    except FileNotFoundError as error:
        print(f'Error al cargar el archivo: {error}')

    return diccionario_inventario

#Funcion Principal
print('Programa para almacenar el inventario de Bicicletas en un archivo CSV')

tamaños = ['Gigante','Grande','Mediana','Pequeña','Infantil']
marcas = ['GW','BMX','Shimano','Haro','Trek']
colores = ['Rosa','Azul Eléctrico','Blanco', 'Negro', 'Rojo Carmesí']
tracciones = ['Eléctrica', 'Mecánica', 'Hibrida']

#Aqui generamos el diccionario a partir de las listas, usando dictionary comprenhension
total_bicicletas = 8
diccionario_bicicletas = {
    f'{codigo}':{
        'Marca': random.choice(marcas),
        'Tamaño': random.choice(tamaños),
        'Cambios': random.randint(2,10),
        'Color': random.choice(colores),
        'Tracción' : random.choice(tracciones)
    }
    for codigo in range(1,total_bicicletas+1)
}


visualiza_diccionario_biciletas(diccionario_bicicletas)

encabezado = genera_encabezado_archivo(diccionario_bicicletas)
print(encabezado)

lineas_archivo = genera_lineas_archivo(diccionario_bicicletas)
for linea in lineas_archivo:
    print(linea)

guarda_archivo_csv(diccionario_bicicletas,'Inventario_bicicletas.csv')

diccionario_recuperado = lee_diccionario_desde_archivo('Inventario_bicicletas.csv')

visualiza_diccionario_biciletas(diccionario_recuperado)