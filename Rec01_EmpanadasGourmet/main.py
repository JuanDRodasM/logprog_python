import random

#coding=utf-8
"""
===============================================================================
 Programa: Rec01_EmpanadasGourmet
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Aplicación para gestionar la producción de empanadas gourmet
- Se generan 300 combinaciones aleatorias entre masa, color y relleno
- Se utiliza un diccionario para almacenar la cantidad de veces que la combinación es producida
- Se identifica la combinación que más veces fue producida usando una función
- Se visualizan resultados
 ===============================================================================
"""

#Función para hallar la empanada exitosa
def hallar_empanada_exitosa(diccionario_empanadas):
    maximo_valor = 0
    combinacion_existosa = ''

    #recorremos el diccionario identificando
    # cuál es la llave con el máximo valor
    for llave in diccionario_empanadas.keys():
        if diccionario_empanadas[llave] > maximo_valor:
            maximo_valor = diccionario_empanadas[llave]
            combinacion_existosa = llave

    return combinacion_existosa

#Función principal
print('Programa para simular la producción de empanadas gourmet')

colores = ['Amarillo', 'Verde', 'Morado']
masas = ['Maíz', 'Quinua', 'Trigo']
rellenos = ['Papa', 'Ranchera', 'Verduras']

# Inicializamos el diccionario
diccionario_empanadas = {}

# Cantidad de empanadas a simular
total_empanadas = 300

#Generamos las combinaciones al azar:
for indice in range(total_empanadas):
    # Selección aleatoria de elementos
    masa = random.choice(masas)
    color = random.choice(colores)
    relleno = random.choice(rellenos)

    # Creación de la llave única para la combinación
    llave = f"{masa}-{color}-{relleno}"

    # Validamos si existe la llave en el diccionario
    if llave in diccionario_empanadas.keys():
        diccionario_empanadas[llave] += 1
    else:
        diccionario_empanadas[llave] = 1

# Mostramos todas las combinaciones y sus frecuencias
print(f"Diccionario de empanadas contiene {len(diccionario_empanadas)} combinaciones:")
for llave in diccionario_empanadas.keys():
    print(f'{llave}: {diccionario_empanadas[llave]}')

# Encontramos la combinación más exitosa usando la función
llave_exitosa = hallar_empanada_exitosa(diccionario_empanadas)
cantidad_exitosa = diccionario_empanadas[llave_exitosa]

# Calculamos el porcentaje con respecto al total producido
porcentaje = (cantidad_exitosa / total_empanadas) * 100

# Separamos los componentes de la llave para presentar el informe
componentes_llave = llave_exitosa.split("-")
masa_exitosa = componentes_llave[0]
color_exitoso = componentes_llave[1]
relleno_exitoso = componentes_llave[2]

# Generamos el informe
print("\n*** Resultados ****")
print(f"La empanada más exitosa tiene las siguientes características:")
print(f"- Masa: {masa_exitosa}")
print(f"- Color: {color_exitoso}")
print(f"- Relleno: {relleno_exitoso}")
print(f"- Cantidad producida: {cantidad_exitosa} empanadas")
print(f"- Porcentaje del total: {porcentaje:.2f}%")



