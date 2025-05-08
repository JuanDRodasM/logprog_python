# Para instalar la librería de yaml, usa la siguiente instruccion
# pip install pyyaml

import yaml
import random

# coding=utf-8
"""
===============================================================================
 Programa: TiendaBicicletasArchivosYAML
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Aplicación que almacena un diccionario de inventario de bicicletas en un
- archivo de texto plano en formato YAML (YAML Ain't Markup Language)
- La creación del diccionario se hace usando dictionary comprehension a partir
  de listas que tienen valores para los atributos
 ===============================================================================
"""

# Constantes globales
#Definición de constantes globales
DIMENSIONES = ['Gigante', 'Grande', 'Mediana', 'Pequeña', 'Infantil']
MARCAS = ['GW', 'BMX', 'Shimano', 'Haro', 'Trek']
COLORES = ['Rosa', 'Azul Eléctrico', 'Blanco', 'Negro', 'Rojo Carmesí']
TRACCIONES = ['Eléctrica', 'Mecánica', 'Hibrida']
ARCHIVO_YAML_INVENTARIO = 'inventario_bicicletas.yaml'

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
    print()

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

def guardar_inventario_yaml(inventario,ruta_archivo):
    """
    Guarda el diccionario de inventario en un archivo YAML

    Args:
    inventario (dict): Diccionario con el inventario de bicicletas
    ruta_archivo (str): Ruta del archivo YAML donde se guardará el inventario
    """
    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo_destino:
            yaml.dump(inventario, archivo_destino, default_flow_style=False, allow_unicode=True, sort_keys=True)
        print(f"Archivo {ruta_archivo} creado exitosamente")
    except Exception as e:
        print(f"Error al escribir el archivo: {e}")
def cargar_inventario_yaml(ruta_archivo):
    """
    Lee un archivo YAML y reconstruye el diccionario de inventario

    Args:
        ruta_archivo (str): Ruta del archivo YAML con el inventario

    Returns:
        dict: Diccionario con el inventario de zapatos
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo_fuente:
            datos = yaml.safe_load(archivo_fuente)
        print(f"Archivo {ruta_archivo} leído exitosamente")
        return datos

    except FileNotFoundError as e:
        print(f"Error al leer el archivo: {e}")
        return None


def main():
    """Función principal del programa"""
    print('Programa para almacenar el inventario de Bicicletas en un archivo YAML')

    # Generamos el inventario aleatorio
    TOTAL_BICICLETAS = 7
    diccionario_bicicletas = generar_inventario_aleatorio(TOTAL_BICICLETAS)

    mostrar_inventario(diccionario_bicicletas)

    guardar_inventario_yaml(diccionario_bicicletas,ARCHIVO_YAML_INVENTARIO)

    inventario_recuperado = cargar_inventario_yaml(ARCHIVO_YAML_INVENTARIO)

    mostrar_inventario(inventario_recuperado)

    if diccionario_bicicletas == inventario_recuperado:
        print('Los diccionarios son iguales, no se perdió datos')
    else:
        print('Hubo un error al recuperar los datos, los diccionarios son distintos')

if __name__ == "__main__":
    main()