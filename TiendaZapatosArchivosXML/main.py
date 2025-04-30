import random
import xml.etree.ElementTree as et

#coding=utf-8
"""
===============================================================================
 Programa: TiendaZapatosArchivosXML
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Aplicación que almacena un diccionario de inventario de zapatos en un
- archivo de texto plano en formato XML (Extensible Markup Language)
- La creación del diccionario se hace usando dictionary comprenhension a partir
  de listas que tienen valores para los atributos

 ===============================================================================
"""

#Función para visualizar el contenido del diccionario
def visualiza_diccionario_zapatos(un_diccionario):
    print(f'\nTotal entradas: {len(un_diccionario)}. Contenido del inventario:')
    for llave in un_diccionario.keys():
        print(f'Código: {llave}')
        for detalle in un_diccionario[llave].keys():
            print(f'\t{detalle}: {un_diccionario[llave][detalle]}')
        print()

#Función para guardar un diccionario en un archivo XML
def guarda_archivo_xml(un_diccionario,un_archivo_xml):

    # Creamos el elemento raíz
    nodo_raiz = et.Element("zapatos")

    # Agregamos cada bicicleta como un elemento hijo
    for codigo, detalle in un_diccionario.items():
        zapato = et.SubElement(nodo_raiz, "zapato")

        # Agregamos el codigo como propiedad
        zapato.set("codigo", codigo)

        # Agregar los demás datos como subelementos
        for campo, valor in detalle.items():
            atributo = et.SubElement(zapato, campo.lower())
            atributo.text = str(valor)

    # Crear el árbol y guardarlo con declaración XML y codificación
    et.indent(nodo_raiz,space="   ")
    arbol_elementos = et.ElementTree(nodo_raiz)
    arbol_elementos.write(un_archivo_xml, encoding="utf-8", xml_declaration=True)

    print(f"\nArchivo XML guardado en {un_archivo_xml}")

#Funcion para leer un XML y reconstruir el diccionario
def leer_archivo_xml(un_archivo_xml):

    #Leemos el archivo y obtenemos el nodo raiz
    arbol_elementos = et.parse(un_archivo_xml)
    nodo_raiz = arbol_elementos.getroot()

    diccionario_inventario = {}

    #Procesamos cada elemento zapato
    for zapato in nodo_raiz.findall('zapato'):
        codigo = zapato.get('codigo')

        #creamos el sub-diccionario asociado a este codigo
        datos_zapato = {}

        #Procesamos cada uno de los campos para este zapato
        for campo in zapato:
            nombre_campo = campo.tag.capitalize()
            valor = campo.text

            #Tratamiento especial para la talla, que es entero
            if nombre_campo == 'Talla' and valor.isdigit():
                valor = int(valor)

            datos_zapato[nombre_campo] = valor

        #finalmente agregamos el zapato al diccionario del inventario
        diccionario_inventario[codigo] = datos_zapato

    return diccionario_inventario



#Funcion Principal
print('Programa para gestionar el inventario de Zapatos en un archivo XML')

#Aquí generamos el diccionario a partir de las listas, usando dictionary comprenhension
marcas = ['Puma','Nike','Adidas','Reebok']
colores = ['Blanco','Negro','Azul', 'Gris', 'Rojo']
estilos = ['Running','Urbanos','Vintage', 'Corte Alto']

total_zapatos = 4

diccionario_zapatos = {
    f'{codigo}':{
        'Marca': random.choice(marcas),
        'Color': random.choice(colores),
        'Talla': random.randint(5,15),
        'Estilo': random.choice(estilos)
    }
    for codigo in range(1,total_zapatos+1)
}

visualiza_diccionario_zapatos(diccionario_zapatos)

guarda_archivo_xml(diccionario_zapatos,'inventario_zapatos.xml')

print('\nAqui visualizamos el XML recuperado: ')

diccionario_recuperado = leer_archivo_xml('inventario_zapatos.xml')

visualiza_diccionario_zapatos(diccionario_recuperado)