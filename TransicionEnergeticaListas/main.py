#coding=utf-8

"""
 ======================================================================
 Programa:       TransicionEnergeticaListas
 Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Crear una aplicación de consola que permita monitoreo de generación de energía
- Actualización del proyecto Ex02_TransicionEnergetica utilizando listas
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

fuentes_energia = ['H','E','T','N','S']
eventos = [0,0,0,0,0]
potencias = [0.0, 0.0, 0.0, 0.0, 0.0]

print('Programa para monitorear la generación energética - Versión usando Listas')
print(f'El rango de generación por evento de cada fuente está entre [{potencia_minima};{potencia_maxima}] GWh')
print('Las fuentes pueden ser: ')
print('H: Hídrica ')
print('E: Eólica ')
print('T: Térmica ')
print('N: Nuclear')
print('S: Solar ')

while potencia_generada < meta_potencia:

    #Aqui leemos el tipo de fuente
    tipo_fuente = input('\nIngresa el tipo de fuente (H/E/N/T/S): ').upper()

    if tipo_fuente not in fuentes_energia:
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

    if tipo_fuente == 'H':
        potencias[0] += potencia_ingresada
        eventos[0] +=1

    if tipo_fuente == 'E':
        potencias[1] += potencia_ingresada
        eventos[1] +=1

    if tipo_fuente == 'T':
        potencias[2] += potencia_ingresada
        eventos[2] +=1

    if tipo_fuente == 'N':
        potencias[3] += potencia_ingresada
        eventos[3] +=1

    if tipo_fuente == 'S':
        potencias[4] += potencia_ingresada
        eventos[4] +=1

    #Sentencia de salida - Calculamos la potencia generada usando un for
    #que recorra toda la lista de potencias
    potencia_generada = 0
    for potencia_fuente in potencias:
        potencia_generada += potencia_fuente


# Calculamos resultados
promedios = [0.0,0.0,0.0,0.0,0.0]

for indice in range(len(promedios)):
    promedios[indice] = calcular_promedio_generacion(potencias[indice],eventos[indice])


# Visualizamos resultados
print('\n*** Resultados Obtenidos ****')
print(f'Potencia total generada: {potencia_generada:.2f}')

for indice in range(len(fuentes_energia)):
    print(f'{fuentes_energia[indice]}: Eventos: {eventos[indice]}, potencia: {potencias[indice]:.2f}, promedio: {promedios[indice]:.2f}')