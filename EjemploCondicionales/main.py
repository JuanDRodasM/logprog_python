#coding=utf-8

# ============================
# Programa:       HolaMundo
# Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

# Propósito:
# ----------
# - Demostrar el funcionamiento de condicionales

# ============================

print('Este programa pregunta una hora y dice si es de dia o tarde\n')

hora = int(input('Introduce una hora del día: '))
print('La hora ingresada fue: ', hora)

#Condicional
if hora < 12:
   print('Es de dia')
   print('Que hay para desayunar?')
elif hora == 12:
    print('Es mediodia')
    print('Se me antoja frijolitos')
else:
  print('Es de tarde')
  print('Esta haciendo ganas de una cervecitaaaaa')


# Aqui se demuestra los condicionales compuestos
# Utilizando if-elif-else y los operadores lógicos and y or

#Tabla de verdad para and y para or
# P    Q    P y Q    P o Q
# V    V    V        V
# V    F    F        V
# F    V    F        V
# F    F    F        F

print('Programa para demostrar condicionales compuestos')
print('Utilizando if-elif-else y los operadores lógicos and y or')

edad = int(input('Ingrese su edad: '))
nacionalidad = input('Ingrese su nacionalidaSd: ').lower()

if nacionalidad == 'colombiano' and edad >= 18:
  print('Eres colombiano y mayor de edad, puedes votar')
elif nacionalidad == 'colombiano':
  print('Eres colombiano pero no mayor de edad, no puedes votar')

if nacionalidad == 'extranjero' and edad >= 21:
  print('Eres extranjero y mayor de edad, puedes votar')
elif nacionalidad == 'extranjero':
  print('Eres extranjero pero no mayor de edad, no puedes votar')

