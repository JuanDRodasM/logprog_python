import json
import random

#coding=utf-8
"""
===============================================================================
 Programa: TiendaBicicletasArchivosJSON
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Aplicación que almacena un diccionario de inventario de bicicletas en un
- archivo de texto plano en formato JSON (JavaScript Object Notation)
- La creación del diccionario se hace usando dictionary comprenhension a partir
  de listas que tienen valores para los atributos
 ===============================================================================
"""

#Definición de constantes globales
DIMENSIONES = ['Gigante', 'Grande', 'Mediana', 'Pequeña', 'Infantil']
MARCAS = ['GW', 'BMX', 'Shimano', 'Haro', 'Trek']
COLORES = ['Rosa', 'Azul Eléctrico', 'Blanco', 'Negro', 'Rojo Carmesí']
TRACCIONES = ['Eléctrica', 'Mecánica', 'Hibrida']
ARCHIVO_INVENTARIO_JSON = 'inventario_bicicletas.json'

def visualizar_diccionario_bicicletas(inventario):
    """
    Muestra el contenido del diccionario de inventario de bicicletas

    Args:
        inventario (dict): Diccionario con el inventario de bicicletas
    """

    print(f'\n Total entradas: {len(inventario)}. Contenido del inventario:')
    for llave in inventario.keys():
        print(f'código: {llave}')
        for detalle in inventario[llave].keys():
            print(f'\t{detalle}: {inventario[llave][detalle]}')

def guardar_archivo_json(inventario,ruta_archivo):
    """
    Guarda el diccionario de inventario en un archivo JSON

    Args:
        inventario (dict): Diccionario con el inventario de zapatos
        ruta_archivo (str): Ruta del archivo JSON donde se guardará el inventario
    """

    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo_destino:
            # El parámetro indent=4 hace que el JSON sea más legible con sangrías
            # ensure_ascii=False permite guardar caracteres no ASCII correctamente
            json.dump(inventario, archivo_destino, indent=4, ensure_ascii=False)
        print(f"Archivo '{ruta_archivo}' creado exitosamente.")
    except Exception as e:
        print(f"Error al escribir el archivo: {e}")

# Función para leer un archivo JSON y convertirlo en diccionario
def leer_archivo_json(ruta_archivo):
    """
    Lee un archivo JSON y reconstruye el diccionario de inventario

    Args:
        ruta_archivo (str): Ruta del archivo JSON con el inventario

    Returns:
        dict: Diccionario con el inventario de bicicletas
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo_fuente:
            un_diccionario = json.load(archivo_fuente)
        print(f"Archivo '{ruta_archivo}' leído exitosamente.")
        return un_diccionario
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def generar_inventario_aleatorio(cantidad):
    """
    Genera un inventario aleatorio de bicicletas

    Args:
        cantidad (int): Número de bicicletas a generar

    Returns:
        dict: Diccionario con el inventario generado
    """
    diccionario_inventario = {
        f'{codigo}':{
            'Marca': random.choice(MARCAS),
            'Tamaño': random.choice(DIMENSIONES),
            'Cambios': random.randint(2,10),
            'Color': random.choice(COLORES),
            'Tracción' : random.choice(TRACCIONES)
        }
        for codigo in range(1,cantidad+1)
    }

    return diccionario_inventario


def main():
    """Función principal del programa"""
    print('Programa para almacenar el inventario de Bicicletas en un archivo JSON')

    # Generamos el inventario aleatorio
    TOTAL_BICICLETAS = 7
    diccionario_bicicletas = generar_inventario_aleatorio(TOTAL_BICICLETAS)

    visualizar_diccionario_bicicletas(diccionario_bicicletas)

    guardar_archivo_json(diccionario_bicicletas,ARCHIVO_INVENTARIO_JSON)

    diccionario_recuperado = leer_archivo_json(ARCHIVO_INVENTARIO_JSON)

    print('\nEste es el contenido del diccionario luego de leerlo desde el JSON: \n')
    visualizar_diccionario_bicicletas(diccionario_recuperado)


if __name__ == "__main__":
    main()