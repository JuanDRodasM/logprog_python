#coding=utf-8

"""
 ======================================================================
 Programa:       PavimentacionCalles
 Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Crear una aplicación de consola que permita identificación de los
  tramos pavimentados en una ciudad
 ======================================================================

Pavimentación de Calles

La Alcaldía municipal está buscando mejorar la calidad de las vías que actualmente
están deterioradas por agrietamientos, ondulamientos y hundimientos. Para ello se
ha propuesto pavimentar 5 km en tramos identificados en los diferentes barrios que
tienen longitudes entre 200 y 600 m.

Se desea realizar un programa en Python que permita registrar como se está cumpliendo
la meta de pavimentación, discriminando la cantidad de tramos por tipo de deterioro
y longitud total pavimentada para ésta.

Posteriormente se generarán los siguientes resultados por cada tipo de deterioro:

•	Cuantos tramos se pavimentaron para cada tipo de deterioro.
•	Cuantos metros fueron pavimentados por cada tipo de deterioro.
•	El promedio de pavimentación por cada tipo de deterioro: Total metros pavimentados / cantidad de tramos.

El programa debe:
•	Implementar una función calcular_promedio_pavimentacion que recibe como parámetro
    la cantidad de metros y el total de tramos para un tipo de deterioro específico.
    Al ser tres tipos de deterioros, la función debe invocarse tres veces.

•	Visualizar el resumen por cada tipo de deterioro: Cuantos tramos, Total metros
    pavimentados y promedio de pavimentación.

•	Usar control de excepciones en caso de que se presenten errores por valor inválido al
    momento de ingresar valores por parte del usuario. Adicionalmente, tener presente que
    se pueden presentar situaciones de divisiones por cero.

 ======================================================================

"""

def calcular_promedio_pavimentacion(total_metros, total_tramos):
    if total_tramos == 0:
        return 0.0
    else:
        return (total_metros / total_tramos)


#Función Principal
print('Programa para identificación de los tramos pavimentados en una ciudad')

# Variables utilizadas como contadores y acumuladores
tramos_agrietamientos = 0
tramos_ondulaciones = 0
tramos_hundimientos = 0

metros_agrietamientos = 0
metros_ondulaciones = 0
metros_hundimientos = 0

meta_pavimentacion = 5000
metros_actuales = 0

while metros_actuales <= meta_pavimentacion:
    tipo_deterioro = input(f'\nIngresa la inicial del tipo de deterioro: (a)grietamiento, (o)ndulacion, (h)undimiento): ').lower()

    if tipo_deterioro != 'a' and tipo_deterioro != 'o' and tipo_deterioro != 'h':
        print('El tipo de deterioro ingresado no es válido. Intenta nuevamente. \n')
        continue
    else:
        try:
            cantidad_metros = int(input('Ingresa la cantidad de metros pavimentados en este tramo: '))

            #Validamos si el dato de la cantidad de metros es válida
            if cantidad_metros <200 or cantidad_metros > 600:
                print('La cantidad de metros ingresada no es válida. Intenta nuevamente. \n')
                continue

            if tipo_deterioro  == 'a':
                tramos_agrietamientos += 1
                metros_agrietamientos += cantidad_metros

            if tipo_deterioro == 'o':
                tramos_ondulaciones += 1
                metros_ondulaciones += cantidad_metros

            if tipo_deterioro == 'h':
                tramos_hundimientos += 1
                metros_hundimientos += cantidad_metros

            metros_actuales = metros_hundimientos + metros_ondulaciones + metros_agrietamientos # Modificación de la variable de control
            print(f'Tramo registrado. Se han pavimentado {metros_actuales} metros')

        except ValueError:
            print('El dato ingresado no es válido. Intenta nuevamente\n')
            continue

#Cálculo de promedios de afectación
promedio_pavimentacion_hundimiento = calcular_promedio_pavimentacion(metros_hundimientos,tramos_hundimientos)
promedio_pavimentacion_ondulacion = calcular_promedio_pavimentacion(metros_ondulaciones,tramos_ondulaciones)
promedio_pavimentacion_agrietamiento = calcular_promedio_pavimentacion(metros_agrietamientos,tramos_agrietamientos)

#Visualización de resultados
print('\n\n*** Resultados Obtenidos ***')
print(f'Se pavimentaron en total {metros_actuales} metros')

print(f'Tramos por deterioro hundimiento: {tramos_hundimientos}, '
      f'metros pavimentados: {metros_hundimientos} m, '
      f'Promedio pavimentación: {promedio_pavimentacion_hundimiento:.2f} m/tramo')

print(f'Tramos por deterioro ondulación: {tramos_ondulaciones}, '
      f'metros pavimentados: {metros_ondulaciones} m, '
      f'Promedio pavimentación: {promedio_pavimentacion_ondulacion:.2f} m/tramo')

print(f'Tramos por deterioro agrietamiento: {tramos_agrietamientos}, '
      f'metros pavimentados: {metros_agrietamientos} m, '
      f'Promedio pavimentación: {promedio_pavimentacion_agrietamiento:.2f} m/tramo')