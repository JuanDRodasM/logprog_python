#coding=utf-8

# ============================
# Programa:       EjemploFunciones
# Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

# Propósito:
# ----------
# - Demostrar el funcionamiento de las funciones, los parametros y los tipos de retorno.

# ============================

from datetime import datetime

#Funcion que no recibe parametros y no retorna valores
def saludar():
    print('Hola a todo el que ejecute este programa')

#Funcion que recibe parametro y no retorna valores
def visualizar_tabla(numero):
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(numero, 'x', multiplicador, '=', resultado)

#Funcion que recibe parametros y retorna valores
def calcular_cubo(numero):
    cubo = numero ** 3
    return cubo

#Funcion que no recibe parametros y retorna valores
def obtener_fecha_actual():
    fecha_obtenida = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return fecha_obtenida

print('Programa para demostrar el uso de funciones')
for ciclo in range(10):
    saludar()

print('\nAhora generamos la tabla de multiplicar')
numero = int(input('Ingresa un numero entero: '))

visualizar_tabla(numero)

valor_cubico = calcular_cubo(numero)
print(f'\nEl valor cúbico del dato {numero} es {valor_cubico}')

dato_fecha = obtener_fecha_actual()
print(f'\nLa fecha obtenida es {dato_fecha}')