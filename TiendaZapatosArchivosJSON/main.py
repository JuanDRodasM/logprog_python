import json
import random

# coding=utf-8
"""
===============================================================================
 Programa: TiendaZapatosArchivosJSON
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Aplicación que almacena un diccionario de inventario de zapatos en un
- archivo de texto plano en formato JSON (JavaScript Object Notation)
- La creación del diccionario se hace usando dictionary comprehension a partir
  de listas que tienen valores para los atributos
 ===============================================================================
"""


# Constantes globales
MARCAS = ['Puma','Nike','Adidas','Reebok']
COLORES = ['Blanco','Negro','Azul', 'Gris', 'Rojo']
ESTILOS = ['Running','Urbanos','Vintage', 'Corte Alto']
ARCHIVO_JSON_INVENTARIO = 'inventario_zapatos.json'

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

def guardar_inventario_json(inventario,ruta_archivo):
    """
    Guarda el diccionario de inventario en un archivo JSON

    Args:
    inventario (dict): Diccionario con el inventario de zapatos
    ruta_archivo (str): Ruta del archivo XML donde se guardará el inventario
    """
    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo_destino:
            # El parámetro indent=4 hace que el JSON sea más legible con sangrías
            # ensure_ascii=False permite guardar caracteres no ASCII correctamente
            json.dump(inventario, archivo_destino, indent=4, ensure_ascii=False)

        print(f"Archivo '{ruta_archivo}' creado exitosamente.")
    except Exception as e:
        print(f"Error al escribir el archivo: {e}")

def cargar_inventario_json(ruta_archivo):
    """
    Lee un archivo JSON y reconstruye el diccionario de inventario

    Args:
        ruta_archivo (str): Ruta del archivo JSON con el inventario

    Returns:
        dict: Diccionario con el inventario de zapatos
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo_origen:
            diccionario = json.load(archivo_origen)
        print(f"Archivo '{ruta_archivo}' leído exitosamente.")
        return diccionario

    except FileNotFoundError as fnfe:
        print(f"Error al leer el archivo: {fnfe}")
        return None

def main():
    """Función principal del programa"""

    # Generamos el inventario aleatorio
    CANTIDAD_ZAPATOS = 12
    inventario = generar_inventario_aleatorio(CANTIDAD_ZAPATOS)

    # Mostramos el inventario generado
    mostrar_inventario(inventario)

    # Guardamos en un archivo JSON
    guardar_inventario_json(inventario, ARCHIVO_JSON_INVENTARIO)

    # Leemos el archivo JSON y recuperamos el inventario
    inventario_recuperado = cargar_inventario_json(ARCHIVO_JSON_INVENTARIO)

    # Visualizamos el resultado
    print('\nEl contenido del inventario luego de leerlo del JSON es:\n')
    mostrar_inventario(inventario_recuperado)

if __name__ == "__main__":
    main()