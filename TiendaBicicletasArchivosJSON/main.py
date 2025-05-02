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

#Función para visualizar el contenido del diccionario
def visualiza_diccionario_bicicletas(un_diccionario):
    print(f'\n Total entradas: {len(un_diccionario)}. Contenido del inventario:')
    for llave in un_diccionario.keys():
        print(f'código: {llave}')
        for detalle in un_diccionario[llave].keys():
            print(f'\t{detalle}: {un_diccionario[llave][detalle]}')

# Función para escribir el diccionario en un archivo JSON
def guarda_archivo_json(un_diccionario,un_archivo_json):
    try:
        with open(un_archivo_json, 'w', encoding='utf-8') as archivo_destino:
            # El parámetro indent=4 hace que el JSON sea más legible con sangrías
            # ensure_ascii=False permite guardar caracteres no ASCII correctamente
            json.dump(un_diccionario, archivo_destino, indent=4, ensure_ascii=False)
        print(f"Archivo '{un_archivo_json}' creado exitosamente.")
    except Exception as e:
        print(f"Error al escribir el archivo: {e}")

# Función para leer un archivo JSON y convertirlo en diccionario
def leer_archivo_json(un_archivo_json):
    try:
        with open(un_archivo_json, 'r', encoding='utf-8') as archivo_fuente:
            un_diccionario = json.load(archivo_fuente)
        print(f"Archivo '{un_archivo_json}' leído exitosamente.")
        return un_diccionario
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None


#Funcion Principal
print('Programa para almacenar el inventario de Bicicletas en un archivo JSON')

dimensiones = ['Gigante','Grande','Mediana','Pequeña','Infantil']
marcas = ['GW','BMX','Shimano','Haro','Trek']
colores = ['Rosa','Azul Eléctrico','Blanco', 'Negro', 'Rojo Carmesí']
tracciones = ['Eléctrica', 'Mecánica', 'Hibrida']

#Aqui generamos el diccionario a partir de las listas, usando dictionary comprenhension
total_bicicletas = 1000
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

visualiza_diccionario_bicicletas(diccionario_bicicletas)

guarda_archivo_json(diccionario_bicicletas,'inventario_bicicletas.json')

diccionario_recuperado = leer_archivo_json('inventario_bicicletas.json')

print('\nEste es el contenido del diccionario luego de leerlo desde el JSON: \n')
visualiza_diccionario_bicicletas(diccionario_recuperado)