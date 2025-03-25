#coding=utf-8

"""
 ======================================================================
 Programa:       TransicionEnergeticaDiccionario
 Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Crear una aplicación de consola que permita monitoreo de generación de energía
- Actualización del proyecto Ex02_TransicionEnergetica utilizando diccionarios
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

#Aqui comienza nuestro programa
potencia_generada = 0 # Variable de Control
meta_potencia = 5
potencia_minima = 0.75
potencia_maxima = 1.75

diccionario_fuentes = {
    "hidrica": { "eventos": 0, "potencia":0, "promedio":0},
    "eolica": { "eventos": 0, "potencia":0, "promedio":0},
    "solar": { "eventos": 0, "potencia":0, "promedio":0},
    "nuclear": { "eventos": 0, "potencia":0, "promedio":0},
    "termica": { "eventos": 0, "potencia":0, "promedio":0}
}

print('Programa para monitorear la generación energética - Versión usando Diccionario')
print(f'El rango de generación por evento de cada fuente está entre [{potencia_minima};{potencia_maxima}] GWh')
print('Las fuentes pueden ser: ')

#Recorremos las llaves del diccionario ordenado alfabéticamente
for fuente in dict(sorted(diccionario_fuentes.items())).keys():
    print(f'- {fuente}')

#Ciclo que se repite mientras no se alcance la meta de potencia
while potencia_generada < meta_potencia:

    #Aqui leemos el tipo de fuente
    tipo_fuente = input('\nIngresa el tipo de fuente: ').lower()

    if tipo_fuente not in diccionario_fuentes.keys():
        print('La fuente ingresada no es válida. Intenta nuevamente')
        continue

    #Aqui leemos la potencia ingresada
    try:
        potencia_ingresada = float(input('Ingresa la potencia generada: '))

        if potencia_ingresada < potencia_minima or potencia_ingresada > potencia_maxima:
            print(f'Potencia ingresada no está en el rango: [{potencia_minima};{potencia_maxima}]. Intenta nuevamente')
            continue

    except ValueError:
        print('El dato ingresado no es correcto. Intenta nuevamente.')
        continue

    #Aqui colocamos los valores según la fuente seleccionada
    diccionario_fuentes[tipo_fuente]['potencia'] += potencia_ingresada
    diccionario_fuentes[tipo_fuente]['eventos'] += 1

    #Sentencia de salida - Calculamos la potencia generada usando un for
    #que recorra toda la lista de potencias
    potencia_generada = 0
    for la_fuente in diccionario_fuentes.keys():
        potencia_generada += diccionario_fuentes[la_fuente]['potencia']

#Aqui calculamos los promedios
for la_fuente in diccionario_fuentes.keys():
    diccionario_fuentes[la_fuente]['promedio'] = (
        calcular_promedio_generacion(
            diccionario_fuentes[la_fuente]['potencia'],
            diccionario_fuentes[la_fuente]['eventos']))

# Visualizamos resultados
print('\n*** Resultados Obtenidos ****')
print(f'Potencia total generada: {potencia_generada:.2f}')

for la_fuente in diccionario_fuentes.keys():
    print(f'{la_fuente}: Eventos: {diccionario_fuentes[la_fuente]['eventos']}, potencia: {diccionario_fuentes[la_fuente]['potencia']:.2f}, promedio: {diccionario_fuentes[la_fuente]['promedio']:.2f}')
