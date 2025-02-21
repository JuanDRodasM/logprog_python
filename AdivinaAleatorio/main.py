import random
# coding=utf-8

# ======================================================================
# Programa:       AdivinaNumeroAleatorio
# Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

# Propósito:
# ----------
# Generar un número aleatorio entre 1 y 100 y que el usuario lo pueda adivinar.

print('Programa para adivinar un número aleatorio entre 1 y 100.')

#Variables
limite_inferior = 1
limite_superior = 100

numero_secreto = random.randint(limite_inferior, limite_superior)
#print('El número aleatorio es: ', numero_secreto)

conteo_intentos = 0
dato_ingresado = 0

#Ciclo de control
while dato_ingresado != numero_secreto:
  dato_ingresado = int(input(f'\nIngrese un número entre {limite_inferior} y {limite_superior}: '))
  conteo_intentos += 1

  # Validar que el dato esté en el rango
  if dato_ingresado < limite_inferior or dato_ingresado > limite_superior:
    print(f'Error. El número ingresado debe estar entre {limite_inferior} y {limite_superior}')
    continue

  # Validar si el dato ingresado es mayor que el numero secreto
  if dato_ingresado > numero_secreto:
    print(f'El número {dato_ingresado} es mayor que el número secreto. Intente nuevamente.')
  else:
    if dato_ingresado < numero_secreto:
      print(f'El número {dato_ingresado} es menor que el número secreto. Intente nuevamente.')

# Final del programa - Felicitar al usuario
print(f'¡Felicitaciones! Adivinaste el número secreto {numero_secreto} en {conteo_intentos} intentos.')
