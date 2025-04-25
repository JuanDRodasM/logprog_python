#coding=utf-8
"""
===============================================================================
 Programa: TiendaZapatosArchivosCSV
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Aplicación que almacena un diccionario de inventario de zapatos en un
- archivo de texto plano en formato CSV (Comma Separated Values)
 ===============================================================================
"""
#Función para visualizar el contenido del diccionario
def visualiza_diccionario_zapatos(un_diccionario):
    print('\nContenido del inventario:')
    for llave in un_diccionario.keys():
        print(f'Consecutivo: {llave}')
        for detalle in un_diccionario[llave].keys():
            print(f'\t{detalle}: {un_diccionario[llave][detalle]}')


#Función para generar una cadena de caracteres con el encabezado del archivo
def genera_encabezado_archivo(un_diccionario):
    print('\nEl contenido del archivo será este:\n')

    #Utilizamos el primer elemento del diccionario para obtener sus llaves
    #pues serán los encabezados de las columnas
    primer_elemento = list(un_diccionario.keys())[0]
    columnas = ['Consecutivo'] + list(un_diccionario[primer_elemento].keys())
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

#Funcion Principal
print('Programa para almacenar el inventario de Zapatos en un archivo CSV')

diccionario_zapatos = {
    '1': { 'Marca': 'Puma', 'Referencia': 'Caven 2.0 Mid', 'Talla': 7.5, 'Cantidad': 42},
    '2': { 'Marca': 'Nike', 'Referencia': 'Air Zoom Pegasus', 'Talla': 11.0, 'Cantidad':  47},
    '3': {'Marca': 'Adidas', 'Referencia': 'Adizero Adios Pro 4', 'Talla': 9.5, 'Cantidad': 82},
    '4': {'Marca': 'Reebok', 'Referencia': 'Floatzig X1', 'Talla': 8.0, 'Cantidad': 56}
}

"""
visualiza_diccionario_zapatos(diccionario_zapatos)

encabezado = genera_encabezado_archivo(diccionario_zapatos)
print(encabezado)

lineas_archivo = genera_lineas_archivo(diccionario_zapatos)
for linea in lineas_archivo:
    print(linea)
"""

guarda_archivo_csv(diccionario_zapatos,'inventario_zapatos.csv')
