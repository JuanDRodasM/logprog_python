# ======================================================================
# Programa:       AnalisisTemperatur
# Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

# Propósito:
# ----------
# Permitir analizar la temperatura de un día a partir de varias mediciones
# Se debe calcular la temperatura mínima, máxima, promedio, y visualizar
# cuantas mediciones se hicieron

print('Programa para Analizar las mediciones de temperatura de una ciudad')

#Variables
temperatura_minima = 0.0
temperatura_maxima = 0.0
temperatura_promedio = 0.0
conteo_mediciones = 0
temperatura_ingresada = 0.0

limite_superior = 50.0
limite_inferior = -5.0

#Variable de control
mediciones_adicionales = 'SI'

#ciclo de control
while mediciones_adicionales == 'SI':
    temperatura_ingresada = float(input(f'\nIngresa el dato de temperatura entre {limite_inferior} y {limite_superior}: '))

    # Aqui validamos si la temperatura está en el rango válido
    if temperatura_ingresada > limite_superior or temperatura_ingresada < limite_inferior:
        print(f'Dato fuera del rango [{limite_inferior};{limite_superior}]. Intenta nuevamente.')
        continue

    conteo_mediciones += 1

    if conteo_mediciones == 1:
        temperatura_minima = temperatura_ingresada
        temperatura_maxima = temperatura_ingresada

    #Identificamos si es temperatura máxima o temperatura mínima
    if temperatura_ingresada > temperatura_maxima:
        temperatura_maxima = temperatura_ingresada

    if temperatura_ingresada < temperatura_minima:
        temperatura_minima = temperatura_ingresada

    temperatura_promedio += temperatura_ingresada

    mediciones_adicionales = input('Desea registrar otra medición (SI/NO): ').upper()

# Calculamos la temperatura promedio
temperatura_promedio = temperatura_promedio / conteo_mediciones
temperatura_media = (temperatura_maxima - temperatura_minima) / 2

#Visualización de resultados
print('*** Resultados Obtenidos *** \n')
print(f'En total fueron {conteo_mediciones} mediciones')
print(f'La temperatura máxima fue {temperatura_maxima} y la mínima fue {temperatura_minima}')
print(f'La temperatura promedio fue {temperatura_promedio:.2f}')
print(f'La temperatura media fue {temperatura_media:.2f}')