# coding=utf-8

"""
 ======================================================================
 Programa:       ColonizacionMarteListas
 Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Crear una aplicación de consola que permita monitoreo 4
  lanzamientos a las diferentes planicies de Marte
- Actualización del proyecto Ex02_ColonizacionMarte utilizando listas
 ======================================================================
"""


# Aqui definimos la funcion
def calcular_promedio_efectividad(peso_carga, cantidad_lanzamientos):
    try:
        promedio = peso_carga / cantidad_lanzamientos
        return promedio
    except ZeroDivisionError:
        return 0

# Aqui viene la función principal
# Las variables
print('Programa monitoreo lanzamientos a Marte')
print('Se lanzarán cargamentos a las planicies:')
print('- A - Acidalia')
print('- E - Elysium')
print('- U - Utopia')

planicies = ['A','E','U']
cargas = [0, 0, 0]
lanzamientos = [0, 0, 0]

carga_minima = 0
carga_maxima = 10000

total_lanzamientos = 15
lanzamiento_actual = 1

while lanzamiento_actual <= total_lanzamientos:
    dato_planicie = input(
        f'\nPara el lanzamiento No. {lanzamiento_actual}, ingresa la inicial de la planicie (A/E/U): ').upper()

    # Aqui identificamos si el dato de la planicie es válido
    if dato_planicie not in planicies:
        print('Dato de planicie equivocada. Intenta nuevamente.')
        continue

    # Aqui leemos el dato del cargamento que llego
    try:
        peso_carga = float(input('Ingresa el peso de la carga que llegó a la planicie: '))

        #Validamos si el peso está en el rango
        if peso_carga < carga_minima or peso_carga > carga_maxima:
            print(f'Peso de la carga no está en el rango [{carga_minima};{carga_maxima}]. Intenta nuevamente.')
            continue

        #Dependiendo del dato ingresado para la planicie, se almacena en el indice correspondiente
        #en cada uno de las listas lanzamientos y cargas
        for indice in range(len(planicies)):
            if planicies[indice] == dato_planicie:
                lanzamientos[indice] += 1
                cargas[indice] += peso_carga

    except ValueError:
        print('El dato ingresado no es un número. Intenta nuevamente.')
        continue

    # Esta es la sentencia de salida del ciclo while
    lanzamiento_actual += 1

#Aqui calculamos promedios
promedios = [0, 0, 0]

for indice in range(len(planicies)):
    promedios[indice] = calcular_promedio_efectividad(cargas[indice], lanzamientos[indice])

# Visualizamos resultados
print('\n*** Resultados Obtenidos ***')

for indice in range(len(planicies)):
    print(f'Planicie: {planicies[indice]}, carga: {cargas[indice]:.2f}, lanzamientos: {lanzamientos[indice]}, promedio: {promedios[indice]:.2f}')
