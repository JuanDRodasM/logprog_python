# coding=utf-8

"""
 ======================================================================
 Programa:       ColonizacionMarteDiccionario
 Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Crear una aplicación de consola que permita monitoreo 4
  lanzamientos a las diferentes planicies de Marte
- Actualización del proyecto Ex02_ColonizacionMarte utilizando diccionario
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
diccionario_planicies = {
    "Acidalia" : { "inicial":"A", "carga" : 0, "lanzamientos" : 0, "promedio" : 0.0 },
    "Elysium": {"inicial": "E", "carga": 0, "lanzamientos": 0, "promedio": 0.0},
    "Utopia": {"inicial": "U", "carga": 0, "lanzamientos": 0, "promedio": 0.0},
    "Hellas" : {"inicial": "H", "carga": 0, "lanzamientos": 0, "promedio": 0.0}
}

print('Programa monitoreo lanzamientos a Marte')
print('Se lanzarán cargamentos a las planicies:')

for llave in diccionario_planicies.keys():
    print(f'- {diccionario_planicies[llave]["inicial"]} - {llave}')

carga_minima = 0
carga_maxima = 10000

total_lanzamientos = 6
lanzamiento_actual = 1

while lanzamiento_actual <= total_lanzamientos:
    dato_planicie = input(
        f'\nPara el lanzamiento No. {lanzamiento_actual}, ingresa la planicie (Acidalia/Elysium/Utopia/Hellas): ')

    # Aqui identificamos si el dato de la planicie es válido
    if dato_planicie not in diccionario_planicies.keys():
        print('Dato de planicie equivocada. Intenta nuevamente.')
        continue

    # Aqui leemos el dato del cargamento que llego
    try:
        peso_carga = float(input('Ingresa el peso de la carga que llegó a la planicie: '))

        #Validamos si el peso está en el rango
        if peso_carga < carga_minima or peso_carga > carga_maxima:
            print(f'Peso de la carga no está en el rango [{carga_minima};{carga_maxima}]. Intenta nuevamente.')
            continue

        #Dependiendo del dato ingresado para la planicie, se almacena en el
        #registro de la llave correspondiente en el diccionario
        diccionario_planicies[dato_planicie]["lanzamientos"] += 1
        diccionario_planicies[dato_planicie]["carga"] += peso_carga

    except ValueError:
        print('El dato ingresado no es un número. Intenta nuevamente.')
        continue

    # Esta es la sentencia de salida del ciclo while
    lanzamiento_actual += 1

#Aqui calculamos promedios

for llave in diccionario_planicies.keys():
    diccionario_planicies[llave]["promedio"] = calcular_promedio_efectividad(
        diccionario_planicies[llave]["carga"],
        diccionario_planicies[llave]["lanzamientos"])

# Visualizamos resultados
print('\n*** Resultados Obtenidos ***')

for llave in diccionario_planicies.keys():
    print(f'Planicie: {llave} - {diccionario_planicies[llave]["inicial"]}, ',end="")
    print(f'carga: {diccionario_planicies[llave]["carga"]:.2f}, ',end="")
    print(f'lanzamientos: {diccionario_planicies[llave]["lanzamientos"]:.2f}, ',end="")
    print(f'promedio: {diccionario_planicies[llave]["promedio"]:.2f}')