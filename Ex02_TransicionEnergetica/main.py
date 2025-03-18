#coding=utf-8

"""
 ======================================================================
 Programa:       Ex02_TransicionEnergetica
 Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Crear una aplicación de consola que permita identificación de los
  tramos pavimentados en una ciudad
 ======================================================================

Transición Energética

El gobierno nacional está buscando la implementación de un modelo energético del país que
permita brindar un crecimiento estable a las necesidades de electricidad del país,
diversificando sus fuentes entre hídricas, eólicas, solares y térmicas. Para ello se ha propuesto
monitorear la generación de 5 GWh en diferentes centrales de energía que producen entre 0.75
y 1.25 GWh.

Se desea realizar un programa en Python que permita registrar como se está cumpliendo la
meta de generación, discriminando la cantidad de aportes por tipo de fuente y la cantidad total
de GWh generada por ésta.

Posteriormente se generarán los siguientes resultados por cada tipo de fuente:

- Cuantos GWh se generaron para cada tipo de fuente.
- Cuantos eventos de aporte se presentaron por cada tipo de fuente.
- El promedio de generación por cada tipo de fuente: Total GWh / cantidad de eventos.

El programa debe:
- Implementar una función calcular_promedio_generacion que recibe como
parámetro la cantidad de GWh y el total de eventos de generación para un tipo de
fuente específica. Al ser cuatro tipos de fuente, la función debe invocarse cuatro
veces.
- Visualizar el resumen por cada tipo de fuente: Cuantos eventos de generación, Total
GWH generados y promedio de generación.
- Usar control de excepciones en caso de que se presenten errores por valor inválido al
momento de ingresar valores por parte del usuario. Adicionalmente, tener presente
que se pueden presentar situaciones de divisiones por cero.

"""
#Aqui definimos la función para calcular el promedio de generación
def calcular_promedio_generacion(potencia_fuente, eventos_fuente):
    # Esta es la versión de prevención usando el control de excepciones
    try:
        return (potencia_fuente / eventos_fuente)
    except ZeroDivisionError:
        return 0
"""

    # Esta es la versión de prevención usando el condicional
    if eventos_fuente ==0:
        return 0
    else:
        return (potencia_fuente / eventos_fuente)
"""

#Aqui comienza nuestro programa
eventos_eolica = 0
eventos_hidrica = 0
eventos_solar = 0
eventos_termica = 0

potencia_elolica = 0
potencia_hidrica = 0
potencia_solar = 0
potencia_termica = 0

potencia_generada = 0 # Variable de Control
meta_potencia = 5
potencia_minima = 0.75
potencia_maxima = 1.75

print('Programa para monitorear la generación energética')
print(f'El rango de generación por evento de cada fuente está entre [{potencia_minima};{potencia_maxima}] GWh')
print('Las fuentes pueden ser: ')
print('H: Hídrica ')
print('E: Eólica ')
print('T: Térmica ')
print('S: Solar ')

while potencia_generada < meta_potencia:
    tipo_fuente = input('\nIngresa el tipo de fuente (H/E/T/S): ').upper()

    if tipo_fuente != 'H' and tipo_fuente !='E' and tipo_fuente != 'T' and tipo_fuente != 'S':
        print('Tipo de fuente errónea. El dato a ingresar debe ser (H/E/T/S). ')
        continue
    try:
        potencia_ingresada = float(input('Ingresa la potencia generada: '))

        if potencia_ingresada < potencia_minima or potencia_ingresada > potencia_maxima:
            print(f'Potencia ingresada no está en el rango: [{potencia_minima};{potencia_maxima}]. Intenta nuevamente')
            continue

    except ValueError:
        print('El dato ingresado no es correcto. Intenta nuevamente.')
        continue

    if tipo_fuente == 'H':
        potencia_hidrica += potencia_ingresada
        eventos_hidrica +=1

    if tipo_fuente == 'E':
        potencia_elolica += potencia_ingresada
        eventos_eolica +=1

    if tipo_fuente == 'T':
        potencia_termica += potencia_ingresada
        eventos_termica +=1

    if tipo_fuente == 'S':
        potencia_solar += potencia_ingresada
        eventos_solar +=1

    #Sentencia de salida
    potencia_generada = potencia_hidrica + potencia_elolica + potencia_solar + potencia_termica

# Calculamos resultados
promedio_termica = calcular_promedio_generacion(potencia_termica,eventos_termica)
promedio_eolica = calcular_promedio_generacion(potencia_elolica,eventos_eolica)
promedio_solar = calcular_promedio_generacion(potencia_solar,eventos_solar)
promedio_hidrica = calcular_promedio_generacion(potencia_hidrica,eventos_hidrica)

# Visualizamos resultados
print('\n*** Resultados Obtenidos ****')
print(f'Potencia total generada: {potencia_generada:.2f}')
print(f'Hidrica: Eventos: {eventos_hidrica}, potencia: {potencia_hidrica}, promedio {promedio_hidrica:.2f}')
print(f'Solar: Eventos: {eventos_solar}, potencia: {potencia_solar}, promedio {promedio_solar:.2f}')
print(f'Térmica: Eventos: {eventos_termica}, potencia: {potencia_termica}, promedio {promedio_termica:.2f}')
print(f'Eólica: Eventos: {eventos_eolica}, potencia: {potencia_elolica}, promedio {promedio_eolica:.2f}')