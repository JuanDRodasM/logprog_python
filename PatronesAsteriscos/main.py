#coding=utf-8

# ============================
# Programa:       PatronesAsteriscos
# Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

# Propósito:
# ----------
#- Demostrar el funcionamiento del ciclo de control While, generando patrones de asteriscos en forma de arbolitos.
# ============================

print('Programa para imprimir arbolitos ladeados')

#Partes de un ciclo de control
# 1. Variable de control
# 2. Condición de repetición
# 3. sentencia de salida


total_niveles = 10

print('\nPrimer arbolito: alineado a la izquierda, de menor a mayor')
nivel_actual = 1
while nivel_actual <= total_niveles:
  print(nivel_actual * '*')
  nivel_actual += 1

print('\nSegundo arbolito: alineado a la izquierda, de mayor a menor')
nivel_actual = total_niveles
while nivel_actual >0:
  print(nivel_actual * '*')
  nivel_actual -= 1

print('\nTercer arbolito: alineado a la derecha, de menor a mayor')
cantidad_espacios = total_niveles -1
nivel_actual = 1 #Variable de Control
while nivel_actual <= total_niveles: # Condición a cumplir
  print(' ' * cantidad_espacios + nivel_actual * '*')
  nivel_actual += 1
  cantidad_espacios -= 1

print('\nCuarto arbolito: alineado a la derecha, de mayor a menor')
cantidad_espacios = 0
nivel_actual = total_niveles #Variable de Control
while nivel_actual > 0: # Condición a cumplir
  print(' ' * cantidad_espacios + nivel_actual * '*')
  nivel_actual -= 1
  cantidad_espacios += 1

print('\nQuinto arbolito, centrado de menor a mayor')
nivel_actual = 1
cantidad_espacios = 10
while nivel_actual <= (2*total_niveles):
  print(' ' * cantidad_espacios + nivel_actual * '*')
  nivel_actual += 2
  cantidad_espacios -= 1

print('\nSexto arbolito, centrado de mayor a menor')
nivel_actual = (2*total_niveles -1)
cantidad_espacios = 0
while nivel_actual >= 0:
  print(' ' * cantidad_espacios + nivel_actual * '*')
  nivel_actual -= 2
  cantidad_espacios += 1