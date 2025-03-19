#coding=utf-8

"""
 ======================================================================
 Programa:       Ex02_ColonizacionMarte
 Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Crear una aplicación de consola que permita monitoreo 4
  lanzamientos a las diferentes planicies de Marte
 ======================================================================
"""

#Aqui definimos la funcion
def calcular_promedio_efectividad(peso_carga, cantidad_lanzamientos):

    try:
        promedio = peso_carga / cantidad_lanzamientos
        return promedio
    except ZeroDivisionError:
        return 0

    """
    if cantidad_lanzamientos ==0:
        promedio = 0
    else:
        promedio = peso_carga / cantidad_lanzamientos
    
    return promedio
    """

#Aqui viene la función principal
#Las variables
print('Programa monitoreo lanzamientos a Marte')
print('Se lanzarán cargamentos a las planicies:')
print('- A - Acidalia')
print('- E - Elysium')
print('- U - Utopia')

carga_utopia = 0
carga_acidalia = 0
carga_elysium = 0

lanzamientos_utopia = 0
lanzamientos_acidalia = 0
lanzamientos_elysium = 0

carga_minima = 0
carga_maxima = 10000

total_lanzamientos = 15
lanzamiento_actual = 1

while lanzamiento_actual <= total_lanzamientos:
    planicie = input(f'\nPara el lanzamiento No. {lanzamiento_actual}, ingresa la inicial de la planicie (A/E/U): ').upper()

    #Aqui identificamos si el dato de la planicie es válido
    if planicie != 'A' and planicie != 'E' and planicie != 'U':
        print('Dato de planicie equivocada. Intenta nuevamente.')
        continue

    #Aqui leemos el dato del cargamento que llego

    try:
        peso_carga = float(input('Ingresa el peso de la carga que llegó a la planicie: '))

        if peso_carga < carga_minima or peso_carga > carga_maxima:
            print(f'Peso de la carga no está en el rango [{carga_minima};{carga_maxima}]. Intenta nuevamente.')
            continue

        if planicie == 'A':
            lanzamientos_acidalia +=1
            carga_acidalia += peso_carga

        if planicie == 'E':
            lanzamientos_elysium += 1
            carga_elysium += peso_carga

        if planicie == 'U':
            lanzamientos_utopia += 1
            carga_utopia += peso_carga

    except ValueError:
        print('El dato ingresado no es un número. Intenta nuevamente.')
        continue

    #Esta es la sentencia de salida
    lanzamiento_actual+=1

promedio_acidalia = calcular_promedio_efectividad(carga_acidalia,lanzamientos_acidalia)
promedio_elysium = calcular_promedio_efectividad(carga_elysium,lanzamientos_elysium)
promedio_utopia = calcular_promedio_efectividad(carga_utopia,lanzamientos_utopia)

#Visualizamos resultados
print('\n*** Resultados Obtenidos ***')
print(f'Acidalia: Carga: {carga_acidalia} \t lanzamientos: {lanzamientos_acidalia}, \t promedio: {promedio_acidalia:.2f}')
print(f'Elysium: Carga: {carga_elysium} \t lanzamientos: {lanzamientos_elysium}, \t promedio: {promedio_elysium:.2f}')
print(f'Utopia: Carga: {carga_utopia} \t lanzamientos: {lanzamientos_utopia}, \t promedio: {promedio_utopia:.2f}')