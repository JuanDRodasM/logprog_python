#coding=utf-8

# ============================
# Programa:       EntradaDatos
# Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co
# Propósito:
# ----------
# - Demostrar el funcionamiento básico de la captura de datos desde la consola, utilizando el método input().
# - Demostrar el cambio de tipo de datos desde string hasta int y float, utilizando los métodos float() e int()
# - Demostrar condicionales básicos para la toma de decisiones

# ============================


# Programa que lee un dato de hora y lo convierte a minutos
# Entrada: El valor de la hora
# Salida: El valor de la hora en minutos

print('Programa que lee una hora y lo convierte a minutos')
hora_ingresada = input( 'Ingrese la hora: ')
print('El tipo de dato de la variable horas es: ', type(hora_ingresada))

# Identificamos si en la cadena hay el caracter "."
if '.' in hora_ingresada:
    # Si hay el caracter "." entonces se convierte a float
    hora_ingresada = float(hora_ingresada)
else:
    # Si no hay el caracter "." entonces se convierte a int
    hora_ingresada = int(hora_ingresada)

# Se calcula la hora en minutos
minutos = hora_ingresada * 60

print(f'Las horas {hora_ingresada} convertidas en minutos son: {minutos}')
print('El tipo de dato de la variable minutos es: ', type(minutos))

muchos_minutos = 120

if minutos > muchos_minutos:
    print(f'Los minutos son mayores a {muchos_minutos}, son muchos minutos')
elif minutos == muchos_minutos:
    print(f'Los minutos son iguales a {muchos_minutos}, son apenas {muchos_minutos}')
else:
    print(f'Los minutos son menores a {muchos_minutos}, son muy poquitos!')