import random
import xml.etree.ElementTree as et
from xml.dom import minidom

#coding=utf-8
"""
===============================================================================
 Programa: TiendaBicicletasArchivosXML
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Aplicación que almacena un diccionario de inventario de bicicletas en un
- archivo de texto plano en formato XML (Extensible Markup Language)
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

def guarda_archivo_xml(un_diccionario,un_archivo_xml):

    # Creamos el elemento raíz
    nodo_raiz = et.Element("bicicletas")

    # Agregamos cada bicicleta como un elemento hijo
    for codigo, detalle in un_diccionario.items():
        bicicleta = et.SubElement(nodo_raiz, "bicicleta")

        # Agregamos el codigo como propiedad
        bicicleta.set("codigo", codigo)

        # Agregar los demás datos como sub-elementos
        for campo, valor in detalle.items():
            atributo = et.SubElement(bicicleta, campo)
            atributo.text = str(valor)

    # Creamos un string XML con formato bonito
    xml_generado = minidom.parseString(et.tostring(nodo_raiz)).toprettyxml(indent="    ")

    # Guardamos en el archivo
    with open(un_archivo_xml, "w", encoding="utf-8") as archivo:
        archivo.write(xml_generado)

    print(f"Archivo XML guardado en {un_archivo_xml}")


#Funcion Principal
print('Programa para almacenar el inventario de Bicicletas en un archivo CSV')

dimensiones = ['Gigante','Grande','Mediana','Pequeña','Infantil']
marcas = ['GW','BMX','Shimano','Haro','Trek']
colores = ['Rosa','Azul Eléctrico','Blanco', 'Negro', 'Rojo Carmesí']
tracciones = ['Eléctrica', 'Mecánica', 'Hibrida']

#Aqui generamos el diccionario a partir de las listas, usando dictionary comprenhension
total_bicicletas = 10
diccionario_bicicletas = {
    f'{codigo}':{
        'Marca': random.choice(marcas),
        'Dimension': random.choice(dimensiones),
        'Cambios': random.randint(2,10),
        'Color': random.choice(colores),
        'Traccion' : random.choice(tracciones)
    }
    for codigo in range(1,total_bicicletas+1)
}

visualiza_diccionario_biciletas(diccionario_bicicletas)

guarda_archivo_xml(diccionario_bicicletas,'Inventario_bicicletas.xml')

