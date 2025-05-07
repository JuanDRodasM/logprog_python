import yaml
import random

# coding=utf-8
"""
===============================================================================
 Programa: TiendaZapatosArchivosYAML
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Aplicación que almacena un diccionario de inventario de zapatos en un
- archivo de texto plano en formato YAML (YAML Ain't Markup Language)
- La creación del diccionario se hace usando dictionary comprehension a partir
  de listas que tienen valores para los atributos
 ===============================================================================
"""


# Constantes globales
MARCAS = ['Puma','Nike','Adidas','Reebok']
COLORES = ['Blanco','Negro','Azul', 'Gris', 'Rojo']
ESTILOS = ['Running','Urbanos','Vintage', 'Corte Alto']
ARCHIVO_YAML_INVENTARIO = 'inventario_zapatos.yaml'

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

def guardar_inventario_yaml(inventario,ruta_archivo):
    """
    Guarda el diccionario de inventario en un archivo YAML

    Args:
    inventario (dict): Diccionario con el inventario de zapatos
    ruta_archivo (str): Ruta del archivo YAML donde se guardará el inventario
    """
    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo_destino:
            yaml.dump(inventario, archivo_destino, default_flow_style=False, allow_unicode=True, sort_keys=False)
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

    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

def main():
    """Función principal del programa"""

    # Generamos el inventario aleatorio
    CANTIDAD_ZAPATOS = 15
    inventario = generar_inventario_aleatorio(CANTIDAD_ZAPATOS)

    # Mostramos el inventario generado
    mostrar_inventario(inventario)

    # Guardamos en un archivo yaml
    guardar_inventario_yaml(inventario, ARCHIVO_YAML_INVENTARIO)

    # Leemos el archivo JSON y recuperamos el inventario
    inventario_recuperado = cargar_inventario_yaml(ARCHIVO_YAML_INVENTARIO)

    # Visualizamos el resultado
    print('\nEl contenido del inventario luego de leerlo del YAML es:\n')
    mostrar_inventario(inventario_recuperado)

    # Verificar que el diccionario reconstruido sea igual al original
    if inventario == inventario_recuperado:
        print("¡El diccionario reconstruido es idéntico al original!")
    else:
        print("Hay diferencias entre el diccionario original y el reconstruido")

if __name__ == "__main__":
    main()