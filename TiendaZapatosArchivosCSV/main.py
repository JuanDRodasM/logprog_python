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
def visualiza_diccionario_zapatos(un_diccionario):
    for llave in un_diccionario.keys():
        print(f'Llave: {llave}')

    print('Las llaves en el detalle son:')
    for subllave in un_diccionario["detalle"].keys():
        print(f' - {subllave}')


#Funcion Principal
print('Programa para almacenar el inventario de Zapatos en un archivo CSV')

diccionario_zapatos = {
    "consecutivo":1,
    "detalle":{ "marca":"Puma", "referencia":"Caven 2.0 Mid", "talla":7.5,"cantidad":42}
    }

visualiza_diccionario_zapatos(diccionario_zapatos)