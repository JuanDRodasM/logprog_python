#coding=utf-8

"""
 ======================================================================
 Programa:       RiesgosInundaciones
 Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Crear una aplicación de consola que permita cuantificar la afectación de
    hogares por inundaciones
 ======================================================================


DAGRAN – Riesgos Inundaciones en Antioquia

La Gobernación de Antioquia ha declarado la emergencia climática ante los evidentes
cambios ambientales que están causando desastres naturales en el departamento.
Para ello, ha comisionado al DAGRAN (Departamento Administrativo de Gestión del
Riesgo de Desastres de Antioquia), la implementación de un mecanismo de monitoreo
del nivel de riesgo de las diferentes zonas del territorio, asociados a inundaciones.

Se pueden presentar inundaciones de los siguientes tipos:
•	Inundaciones fluviales: Son causadas por el desbordamiento de ríos, arroyos o
    canales de agua debido a lluvias intensas, deshielos o acumulación de agua en la cuenca.
•	Inundaciones costeras: Se producen por la subida del nivel del mar o por tormentas
    marinas que causan olas gigantes que invaden las zonas costeras.
•	Inundaciones urbanas: Son generadas por la acumulación de agua de lluvia en zonas
    urbanas debido a la falta de drenaje, el mal funcionamiento de las alcantarillas o
    el exceso de pavimento que impide la absorción del agua.

Para validar el funcionamiento del mecanismo de monitoreo, se realizará la prueba con 12
eventos de inundaciones.
Se requiere hacer un programa que permita capturar para cada evento de inundación, de que
tipo fue y cuantos hogares fueron afectados. Si el tipo de inundación no está dentro de los
valores válidos, debe repetirse el ingreso del dato.

Posteriormente se generarán los siguientes resultados por cada tipo de inundación:
•	Cuantos eventos de inundación se presentaron para cada tipo.
•	Cuantos hogares fueron afectados por cada tipo de inundación.
•	El promedio de afectación por cada tipo de inundación: Total hogares afectados / cantidad
    de eventos.

El programa debe:
•	Implementar una función calcular_promedio_afectacion que recibe como parámetro la
    cantidad de hogares y el total de eventos para un tipo de inundación específica. Al
    ser tres tipos de inundaciones, la función debe invocarse tres veces.

•	Visualizar el resumen por cada tipo de inundación: Cuantos eventos, Total hogares
    afectados y promedio de afectación.

•	Usar control de excepciones en caso de que se presenten errores por valor inválido
    al momento de ingresar valores por parte del usuario. Adicionalmente, tener presente
    que se pueden presentar situaciones de divisiones por cero.

 ======================================================================
"""

def calcular_promedio_afectacion(total_hogares, total_eventos):
    if total_eventos == 0:
        return 0.0
    else:
        return (total_hogares / total_eventos)


#Función Principal
print('Programa para cuantificar los hogares afectados por riesgos de inundaciones')

# Variables utilizadas como contadores y acumuladores
eventos_fluviales = 0
eventos_costeros = 0
eventos_urbanos = 0
hogares_afectados_fluvial = 0
hogares_afectados_costero = 0
hogares_afectados_urbano = 0

evento_actual = 1
total_eventos = 12

while evento_actual <= total_eventos:
    tipo_evento = input(f'\nIngresa el tipo de riesgo para el evento {evento_actual} (fluvial, costero, urbano): ')

    if tipo_evento != 'fluvial' and tipo_evento != 'costero' and tipo_evento != 'urbano':
        print('El tipo de riesgo ingresado no es válido. Intenta nuevamente. \n')
        continue
    else:
        try:
            cantidad_hogares = int(input('Ingresa la cantidad de hogares afectados: '))
            if tipo_evento  == 'fluvial':
                eventos_fluviales+=1
                hogares_afectados_fluvial += cantidad_hogares

            if tipo_evento == 'costero':
                eventos_costeros += 1
                hogares_afectados_costero += cantidad_hogares

            if tipo_evento == 'urbano':
                eventos_urbanos += 1
                hogares_afectados_urbano += cantidad_hogares

            evento_actual +=1 # Modificación de la variable de control

        except ValueError:
            print('El dato ingresado no es válido. Intenta nuevamente\n')
            continue

#Cálculo de promedios de afectación
promedio_afectacion_fluvial = calcular_promedio_afectacion(hogares_afectados_fluvial,eventos_fluviales)
promedio_afectacion_costero = calcular_promedio_afectacion(hogares_afectados_costero,eventos_costeros)
promedio_afectacion_urbano = calcular_promedio_afectacion(hogares_afectados_urbano,eventos_urbanos)

#Visualización de resultados
print('\n\n*** Resultados Obtenidos ***')
print(f'Eventos de inundación fluvial: {eventos_fluviales}, '
      f'Hogares afectados: {hogares_afectados_fluvial}, '
      f'Promedio afectacíón: {promedio_afectacion_fluvial:.2f}')

print(f'Eventos de inundación costera: {eventos_costeros}, '
      f'Hogares afectados: {hogares_afectados_costero}, '
      f'Promedio afectacíón: {promedio_afectacion_costero:.2f}')

print(f'Eventos de inundación costera: {eventos_urbanos}, '
      f'Hogares afectados: {hogares_afectados_urbano}, '
      f'Promedio afectacíón: {promedio_afectacion_urbano:.2f}')