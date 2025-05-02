import random
import xml.etree.ElementTree as et

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
        print(f'código: {llave}')
        for detalle in un_diccionario[llave].keys():
            print(f'\t{detalle}: {un_diccionario[llave][detalle]}')

def guarda_archivo_xml(un_diccionario,un_archivo_xml):

    # Creamos el elemento raíz
    nodo_raiz = et.Element("bicicletas")

    # Agregamos cada bicicleta como un elemento hijo
    for codigo, detalle in un_diccionario.items():
        bicicleta = et.SubElement(nodo_raiz, "bicicleta")

        # Agregamos el codigo como propiedad
        bicicleta.set("código", codigo)

        # Agregar los demás datos como sub-elementos
        for campo, valor in detalle.items():
            atributo = et.SubElement(bicicleta, campo.lower())
            atributo.text = str(valor)

    # Crear el árbol y guardarlo con declaración XML y codificación
    et.indent(nodo_raiz,space="   ")
    arbol_elementos = et.ElementTree(nodo_raiz)
    arbol_elementos.write(un_archivo_xml, encoding="utf-8", xml_declaration=True)

    print(f"Archivo XML guardado en {un_archivo_xml}")

#Funcion para leer un XML y reconstruir el diccionario
def leer_archivo_xml(un_archivo_xml):

    #Leemos el archivo y obtenemos el nodo raiz
    arbol_elementos = et.parse(un_archivo_xml)
    nodo_raiz = arbol_elementos.getroot()

    diccionario_inventario = {}

    #Procesamos cada elemento bicicleta
    for bicicleta in nodo_raiz.findall('bicicleta'):
        codigo = bicicleta.get('código')

        #creamos el sub-diccionario asociado a este codigo
        datos_bicicleta = {}

        #Procesamos cada uno de los campos para este zapato
        for campo in bicicleta:
            nombre_campo = campo.tag.lower()
            valor = campo.text

            #Tratamiento especial para los cambios, que es entero
            if nombre_campo == 'cambios' and valor.isdigit():
                valor = int(valor)

            datos_bicicleta[nombre_campo] = valor

        #finalmente agregamos el bicicleta al diccionario del inventario
        diccionario_inventario[codigo] = datos_bicicleta

    return diccionario_inventario


#Funcion Principal
print('Programa para almacenar el inventario de Bicicletas en un archivo CSV')

dimensiones = ['Gigante','Grande','Mediana','Pequeña','Infantil']
marcas = ['GW','BMX','Shimano','Haro','Trek']
colores = ['Rosa','Azul Eléctrico','Blanco', 'Negro', 'Rojo Carmesí']
tracciones = ['Eléctrica', 'Mecánica', 'Hibrida']

#Aqui generamos el diccionario a partir de las listas, usando dictionary comprenhension
total_bicicletas = 4
diccionario_bicicletas = {
    f'{codigo}':{
        'Marca': random.choice(marcas),
        'Tamaño': random.choice(dimensiones),
        'Cambios': random.randint(2,10),
        'Color': random.choice(colores),
        'Tracción' : random.choice(tracciones)
    }
    for codigo in range(1,total_bicicletas+1)
}

visualiza_diccionario_biciletas(diccionario_bicicletas)

guarda_archivo_xml(diccionario_bicicletas,'Inventario_bicicletas.xml')

#Aqui leemos
diccionario_recuperado = leer_archivo_xml('Inventario_bicicletas.xml')

#Visualizamos el resultado
print('\n EL contenido del diccionario luego de leerlo del XML es\n')
visualiza_diccionario_biciletas(diccionario_recuperado)

