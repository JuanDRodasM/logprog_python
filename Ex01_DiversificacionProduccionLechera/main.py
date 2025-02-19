# coding=utf-8

# ======================================================================
# Programa:       DiversificacionProduccionLechera
# Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

# Propósito:
# ----------

#Diversificación de producción lechera

#Teniendo presente los cambiantes gustos del mercado, la finca Lácteos Gratavista
#ha decidido diversificar su producción lechera diaria. La finca tiene tres tipos
# de animales productores: vacas, cabras y búfalas, de las cuales puede obtener
# producción de leche que va entre 0.5 y 1.5 litros en cada ordeño.

#Es necesario conseguir la meta de producción mínima de 10 litros diarios, como
# una combinación de producción de cada una de las especies previamente indicadas.

#Para ello, los trabajadores de la finca indicarán cual tipo de animal se ordeñó y
# cuanto obtuvo de su producción. Solo si el volumen obtenido está en el rango de
# 0.5 y 1.5 litros se considerará válido. Si no es válido, este contenido no será
# tenido en cuenta y no se actualizarán los totalizadores de producción ni los
# contadores de animales ordeñados.

#Cuando la producción iguale o sobrepase la meta mínima de producción, se terminará
# el proceso de registro y se procede a visualizar los resultados.

#Se debe indicar por cada tipo de animal, cuánta producción se obtuvo y cuántos animales
# se ordeñaron. Finalmente se debe indicar cuanto fue la producción total obtenida de
# todos los procesos de ordeño válidos que fueron registrados.

# ======================================================================

# Partes de un ciclo de control
# 1  Variable de control
# 2  Condición de ejecución
# 3  Sentencia de salida o cambio de variable de control

# El tipo de animal: Vaca, Cabra, Búfala
# el volumen esté en el rango válido entre 0.5 y 1.5

print('Programa para Calcular cuanto se ordeño de leche por animal\n')

# Variables utilizadas como contadores y acumuladores
volumen_meta_minima = 10
minimo_volumen = 0.5
maximo_volumen = 1.5

total_vacas = 0
total_cabras = 0
total_bufalas = 0

volumen_vacas = 0
volumen_cabras = 0
volumen_bufalas = 0

# Variables requeridas en el ciclo de control
volumen_recolectado = 0

# Mientras el volumen recolectado sea menor a la meta mínima
while volumen_recolectado <= volumen_meta_minima:
    volumen_ordeñado = float(input(f'Ingrese el volumen de ordeño obtenido: '))

    #Si el volumen no está en el rango válido, se continua en el ciclo sin modificar el volumen recolectado
    if volumen_ordeñado < minimo_volumen or volumen_ordeñado > maximo_volumen:
        print('Volumen inválido. Intenta nuevamente\n')
        continue

    tipo_animal = input('Ingrese el tipo de animal: ').lower()

    #Si el tipo de animal no es de los esperados, se continua en el ciclo sin modificar el volumen recolectado
    if tipo_animal != 'vaca' and tipo_animal != 'cabra' and tipo_animal != 'búfala':
        print('Tipo de animal inválido. Intenta nuevamente\n')
        continue

    if tipo_animal == 'vaca':
        total_vacas += 1
        volumen_vacas += volumen_ordeñado

    if tipo_animal == 'cabra':
        total_cabras += 1
        volumen_cabras += volumen_ordeñado

    if tipo_animal == 'búfala':
        total_bufalas += 1
        volumen_bufalas += volumen_ordeñado

    #Sentencia de salida: recalcular el volumen recolectado para saber si se cumplió la meta
    volumen_recolectado = volumen_cabras + volumen_vacas + volumen_bufalas

    if volumen_recolectado <= volumen_meta_minima:
        print(f'El volumen recolectado hasta el momento es {volumen_recolectado:.2f} lts, falta mínimo {(volumen_meta_minima - volumen_recolectado):.2f} lts\n')
    else:
        print('Meta alcanzada!')

# Visualizacion de resultados
print('\n*** Resultados Obtenidos *** \n')
print(f'Cabras: Total cabras ordeñadas: {total_cabras}, total volumen obtenido {volumen_cabras:.2f} lts.')
print(f'Búfalas: Total búfalas ordeñadas: {total_bufalas}, total volumen obtenido {volumen_bufalas:.2f} lts.')
print(f'Vacas: Total vacas ordeñadas: {total_vacas}, total volumen obtenido {volumen_vacas:.2f} lts.')

print(f'\nEn total se obtuvo una producción de {volumen_recolectado:.2f} Lts')