# coding=utf-8

# ======================================================================
# Programa:       FumigacionesConjuntoResidencial
# Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

# Propósito:
# ----------
# Programa para Calcular las fumigaciones de un conjunto residencial

#Fumigación de Hogares
#El cambio climático es una realidad y uno de los efectos imprevistos de esta situación
# es la proliferación de roedores, insectos y hongos en los conjuntos residenciales.

#Para cumplir su labor, los conjuntos residenciales contratan empresas especializadas para
# que realicen actividades de fumigación en recintos cerrados con las debidas precauciones
# para los habitantes de los hogares.

#Dependiendo del control que se pretenda hacer, la empresa se prepara con el producto
# respectivo. Para nuestro caso, se limitarán las opciones a fumigación contra Roedores,
# Insectos y Hongos.

#Se requiere realizar un programa en Python que permita llevar el registro de las fumigaciones
# de un conjunto residencial conformado por 12 hogares, preguntando para cada uno de ellos
# por la plaga para la cual se fumigará.

#El programa visualizará los resultados indicando para cada plaga, cuantos hogares
# se fumigaron y que porcentaje del total representa.
# ======================================================================

# Partes de un ciclo de control
# 1  Variable de control
# 2  Condición de ejecución
# 3  Sentencia de salida o cambio de variable de control

# Variables utilizadas como contadores
fumigaciones_hongos = 0
fumigaciones_insectos = 0
fumigaciones_roedores = 0

# Variables requeridas en el ciclo de control
hogar_actual = 1
total_hogares = 12

print('Programa para registro de fumigaciones de un conjunto residencial')
print('Se fumigará por insectos, roedores y hongos\n')

while hogar_actual <= total_hogares:
    tipo_fumigacion = input(
        f'Ingrese el tipo de fumigación (insectos/roedores/hongos) para el hogar {hogar_actual}: ').lower()

    if tipo_fumigacion == 'insectos':
        fumigaciones_insectos += 1
    elif tipo_fumigacion == 'hongos':
        fumigaciones_hongos += 1
    elif tipo_fumigacion == 'roedores':
        fumigaciones_roedores += 1
    else:
        print('Tipo de fumigación no válida. Intente nuevamente\n')
        continue

    #Sentencia de salida - Cambio de la variable de control
    hogar_actual += 1

# Calculos finales
porcentaje_insectos = (fumigaciones_insectos / total_hogares) * 100
porcentaje_hongos = (fumigaciones_hongos / total_hogares) * 100
porcentaje_roedores = (fumigaciones_roedores / total_hogares) * 100

# Visualización de resultados
print('\nResultados obtenidos de la fumigación')
print(f'Se fumigaron {fumigaciones_insectos} hogares por insectos, que equivale al {porcentaje_insectos:.2f}%')
print(f'Se fumigaron {fumigaciones_hongos} hogares por hongos, que equivale al {porcentaje_hongos:.2f}%')
print(f'Se fumigaron {fumigaciones_roedores} hogares por roedores, que equivale al {porcentaje_roedores:.2f}%')

print(f'\nLos porcentajes suman: {porcentaje_hongos + porcentaje_insectos + porcentaje_roedores}%')

