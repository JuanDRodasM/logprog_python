#coding=utf-8

"""
===============================================================================
 Programa: ConvierteTiempo
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Crear una aplicación de consola que implemente un menú de opciones.
- Crear una conversión de datos de tiempo desde y a segundos.
- Integrar conceptos de control de excepciones y ciclos de control
 ===============================================================================
"""

# Función que convierte desde segundos a horas y minutos
def convertir_desde_segundos():
    print(' *** Función que convierte a horas y minutos desde segundos ***')

    dato_correcto = False
    while dato_correcto is False:
        try:
            segundos = int(input('Ingresa un valor entero para los segundos: '))
            horas = segundos // 3600
            minutos = (segundos - (horas*3600)) // 60
            segundos_restantes = segundos - (horas*3600) - (minutos * 60)

            print(f'{segundos} segundos equivalen a {horas} horas, {minutos} minutos, {segundos_restantes} segundos')
            dato_correcto = True

        except ValueError:
            print('El dato ingresado no es válido. Intenta nuevamente')


# Función que convierte desde horas y minutos a segundos
def convertir_a_segundos():
    print(' *** Función que convierte desde horas y minutos a segundos ***')
    dato_correcto = False
    while dato_correcto is False:
        try:
            horas = int(input('Ingresa un valor entero para las horas: '))
            minutos = float(input('Ingresa un valor decimal para los minutos: '))
            segundos = (horas * 3600) + (minutos * 60)

            print(f'{horas} horas y {minutos} minutos equivalen a {segundos} segundos')
            dato_correcto = True

        except ValueError:
            print('El dato ingresado para la hora o los minutos no es válido. Intenta nuevamente')


# Sección principal del programa
print('Programa para demostrar uso de Menu de Opciones - Conversión de tiempo')

finaliza_ejecucion = False
while finaliza_ejecucion is False:
    print('\n************ OPCIONES DISPONIBLES ******************\n')
    print('   1.  Convierte segundos a horas y minutos')
    print('   2.  Convierte horas y minutos a segundos')
    print('   3.  Salir\n')

    opcion = input('Ingresa el número de la opción deseada: ')

    if opcion != '1' and opcion !='2' and opcion!='3':
        print('Opción inválida. Intenta nuevamente')
        continue

    if opcion == '1':
        convertir_desde_segundos()
        continue

    if opcion == '2':
        convertir_a_segundos()
        continue

    #Con esta opción se sale del ciclo
    if opcion == '3':
        finaliza_ejecucion = True

print('********** Programa Finalizado **************')
