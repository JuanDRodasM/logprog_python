# coding=utf-8

# ======================================================================
# Programa:       PesoCachorroVeterinaria
# Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

# Propósito:
# ----------

#Control de peso de un Cachorro en Veterinaria

#Una clínica veterinaria necesita un programa para registrar la evolución
# del peso de los cachorros recién nacidos durante sus primeras semanas de
# vida. El veterinario debe ingresar el nombre del cachorro y registrar
# su peso diario (en gramos) durante los primeros 15 días. Al finalizar
# cada registro diario, el programa debe mostrar:
#El nombre del cachorro seguido de su peso actual
#El porcentaje de variación de peso respecto al día anterior
#Un mensaje personalizado que indique si el cachorro está ganando o perdiendo peso
#El número de días consecutivos que el cachorro ha mantenido un aumento de peso
# El programa debe continuar solicitando datos hasta que el veterinario indique
# que ha completado los 15 días de seguimiento o cuando ingrese una marca especial
# para terminar el registro anticipadamente."


# ======================================================================

print('Programa para controlar el peso de un cachorro en Veterinaria\n')

#Declaración de variables
peso_hoy = 0.0
peso_ayer = 0.0
dias_consecutivos_incremento = 0
maximo_dias_consecutivos = 0

#Variables de control para el ciclo
duracion_control_dias = 15
dia_actual = 1

nombre_cachorro = input('Ingresa el nombre del cachorro: ')

#El ciclo de control principal
while (dia_actual <= duracion_control_dias):
    peso_hoy = float(input(f'\nIngresa el peso en gr para {nombre_cachorro} en el dia {dia_actual+1}: '))

    # Validamos si el peso medido es positivo
    if peso_hoy <= 0:
        print('Dato del peso erróneo. Intenta nuevamente')
        continue

    #Identificamos acción según el número del día
    if dia_actual > 1:
        diferencia_peso = peso_hoy - peso_ayer
        print(f'La diferencia de peso con respecto al día anterior fue de {diferencia_peso}')

        # Validamos si el peso está aumentando
        if diferencia_peso > 0:
            dias_consecutivos_incremento +=1

            #Validamos si hemos encontrado un nuevo máximo de días consecutivos de incremento
            if dias_consecutivos_incremento > maximo_dias_consecutivos:
                maximo_dias_consecutivos = dias_consecutivos_incremento

            print(f'{nombre_cachorro} subió de peso. ')
            print(f'Lleva {dias_consecutivos_incremento} días incrementando. Maximo de días {maximo_dias_consecutivos}')
        else:
            print(f'{nombre_cachorro} no subió de peso')
            dias_consecutivos_incremento =0
            print('Se ha reiniciado el contador de días de días consecutivos')

    else:
        print('Es el primer dia, no hay diferencia de peso')

    #Aqui le preguntamos al veterinario si continua con otro día el control
    if(dia_actual< duracion_control_dias):
        respuesta_continuar = input('\nDesea registrar un siguiente dia (SI/NO): ').upper()

    if respuesta_continuar == 'NO':
        break

    #Registrar el peso del día anterior para siguiente iteración
    peso_ayer = peso_hoy

    #Sentencia de salida: Modificación de la variable de control
    dia_actual += 1



# Calculos

# Visualización de Resultados
print('\n*** Resultados ***')
print(f'El cachorro {nombre_cachorro} terminó el periodo de control con un peso de {peso_hoy} gr')
print(f'El control se realizó durante {dia_actual} días')
print(f'Subió de peso de manera consecutiva maximo {maximo_dias_consecutivos} dias')