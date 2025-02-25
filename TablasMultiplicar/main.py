# ======================================================================
# Programa:       AnalisisTemperatur
# Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

# Propósito:
# ----------
# Programa para demostrar el ciclo "for"

print('Programa para generar las tablas de multiplicar de los números del 1 al 10')

for numero in range(1,11):
  print(f'\nTabla de multiplicar para el número {numero}:')

  for multiplicador in range(1,13):
    resultado = numero * multiplicador
    print(numero, 'x', multiplicador, '=', resultado)