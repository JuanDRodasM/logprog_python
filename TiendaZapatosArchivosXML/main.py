import random
import xml.etree.ElementTree as ET

# coding=utf-8
"""
===============================================================================
 Programa: TiendaZapatosArchivosXML
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Aplicación que almacena un diccionario de inventario de zapatos en un
- archivo de texto plano en formato XML (Extensible Markup Language)
- La creación del diccionario se hace usando dictionary comprehension a partir
  de listas que tienen valores para los atributos
 ===============================================================================
"""
# Constantes globales
MARCAS = ['Puma','Nike','Adidas','Reebok']
COLORES = ['Blanco','Negro','Azul', 'Gris', 'Rojo']
ESTILOS = ['Running','Urbanos','Vintage', 'Corte Alto']
ARCHIVO_XML_INVENTARIO = 'inventario_zapatos.xml'

def mostrar_inventario(inventario):
    """
    Muestra el contenido del diccionario de inventario de zapatos

    Args:
        inventario (dict): Diccionario con el inventario de zapatos
    """
    print(f'\nTotal entradas: {len(inventario)}. Contenido del inventario:')
    for codigo, detalles in inventario.items():
        print(f'código: {codigo}')
        for atributo, valor in detalles.items():
            print(f'\t{atributo}: {valor}')

def guardar_inventario_xml(inventario, ruta_archivo):
    """
    Guarda el diccionario de inventario en un archivo XML

    Args:
        inventario (dict): Diccionario con el inventario de zapatos
        ruta_archivo (str): Ruta del archivo XML donde se guardará el inventario
    """
    # Creamos el elemento raíz
    nodo_raiz = ET.Element("zapatos")

    # Agregamos cada zapato como un elemento hijo
    for codigo, detalles in inventario.items():
        zapato = ET.SubElement(nodo_raiz, "zapato")

        # Agregamos el código como propiedad
        zapato.set("código", codigo)

        # Agregar los demás datos como subelementos
        for campo, valor in detalles.items():
            atributo = ET.SubElement(zapato, campo.lower())
            atributo.text = str(valor)

    # Crear el árbol y guardarlo con declaración XML y codificación
    ET.indent(nodo_raiz, space="   ")
    arbol_elementos = ET.ElementTree(nodo_raiz)
    arbol_elementos.write(ruta_archivo, encoding="utf-8", xml_declaration=True)

    print(f"Archivo XML guardado en {ruta_archivo}")

def cargar_inventario_xml(ruta_archivo):
    """
    Lee un archivo XML y reconstruye el diccionario de inventario

    Args:
        ruta_archivo (str): Ruta del archivo XML con el inventario

    Returns:
        dict: Diccionario con el inventario de zapatos
    """
    # Leemos el archivo y obtenemos el nodo raiz
    arbol_elementos = ET.parse(ruta_archivo)
    nodo_raiz = arbol_elementos.getroot()

    inventario = {}

    # Procesamos cada elemento zapato
    for zapato in nodo_raiz.findall('zapato'):
        codigo = zapato.get('código')

        # Creamos el sub-diccionario asociado a este código
        datos_zapato = {}

        # Procesamos cada uno de los campos para esta bicicleta
        for campo in zapato:
            nombre_campo = campo.tag.capitalize()
            valor = campo.text

            # Tratamiento especial para los cambios, que es entero
            if nombre_campo == 'cambios' and valor.isdigit():
                valor = int(valor)

            datos_zapato[nombre_campo] = valor

        # Finalmente agregamos la bicicleta al diccionario del inventario
        inventario[codigo] = datos_zapato

    return inventario

def generar_inventario_aleatorio(cantidad):
    """
    Genera un inventario aleatorio de zapatos

    Args:
        cantidad (int): Número de bicicletas a generar

    Returns:
        dict: Diccionario con el inventario generado
    """
    diccionario_inventario = {
        f'{codigo}': {
            'Marca': random.choice(MARCAS),
            'Color': random.choice(COLORES),
            'Talla': random.randint(5, 15),
            'Estilo': random.choice(ESTILOS)
        }
        for codigo in range(1, cantidad + 1)
    }

    return diccionario_inventario

def main():
    """Función principal del programa"""

    # Generamos el inventario aleatorio
    CANTIDAD_ZAPATOS = 10
    inventario = generar_inventario_aleatorio(CANTIDAD_ZAPATOS)

    # Mostramos el inventario generado
    mostrar_inventario(inventario)

    # Guardamos en XML
    guardar_inventario_xml(inventario, ARCHIVO_XML_INVENTARIO)

    # Leemos el XML y recuperamos el inventario
    inventario_recuperado = cargar_inventario_xml(ARCHIVO_XML_INVENTARIO)

    # Visualizamos el resultado
    print('\nEl contenido del inventario luego de leerlo del XML es:\n')
    mostrar_inventario(inventario_recuperado)

if __name__ == "__main__":
    main()