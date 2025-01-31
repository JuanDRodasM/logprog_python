# coding=utf-8

# ============================
# Programa:       HolaMundo
# Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

# Propósito:
# ----------
# - Demostrar el funcionamiento básico del Entorno Integrado de Desarrollo (IDE).
# - Visualizar información en la consola, en forma de cadena de caracteres.
# - Declarar variables asignando valores string y visualizar su contenido en la consola.
# - Demostrar el funcionamiento de la función print().

# ============================

# Este es un comentario, que no se ejecuta. Comienza con el caracter "#"

#Caracteres:
#Simbolos: . = , $ # & *
#cifras: 1 2 3 4 5 6 7 8 9 0
#Letras: a b c A B C ñ Ñ á â

# Comenzamos con la forma mas básica de colocar informacion en consola.
# Utilizamos la función print()
# Escribe una cadena de caracteres, delimitada por comillas simples

print('Hola Mundo!')

# Aqui utilizamos el caracter especial \n para agregar saltos de linea
print('\nEsta frase se escribe en una línea \ny esta en otra\n')

# Aqui utilizamos el caracter especial \t para separar en una misma con tabuladores
print("Primera parte \t Segunda Parte \t Tercera Parte")

# Aqui colocamos un salto de linea
print()

# Aqui colocamos en la consola el valor de un numero
print(3.14159265)

#Aqui se puede escribir una combinacion de cadena de caracteres y numeros
print('El valor de PI es',3.14159265)

# O convirtiendo el número a una cadena de caracteres
print('Usando la función \'str\', el valor de PI es ' + str(3.14159265))

#Variables: Son definiciones de datos que pueden cambiar
#Declarar una variable: Es asignarle el nombre y un valor
#La asignación se hace utilizando el símbolo "="
#La asignación no es conmutativa. Primero va el nombre y luego el valor
unaFrase = 'Esta es una frase almacenada en una variable'
print(unaFrase)

# Se pueden combinar/concatenar varias frases utilizando el operador "+"
otraFrase = 'Esta es otra frase en otra variable'
print(unaFrase + "\n" + otraFrase)

numero_pi = 3.14159265
print('El valor de pi es: ' + str(numero_pi))

# Aqui declaramos implicitamente una variable de tipo entero
# asignandole un dato de tipo entero
un_numero = -38
print(un_numero)
#la función type nos indica cual es el tipo de la variable
print(type(un_numero))

#aqui reutilizamos la variable un_numero pero le cambiamos el
#el tipo, asignandole un valor de tipo flotante
un_numero = 8.654
print(un_numero)
print(type(un_numero))

#Operadores matemáticos
print('\nUtilización de Operadores matemáticos')
suma = 3 + 8
resta = 15 - 7
multiplicacion = 12 * 6
division = 14 / 5
division_entera = 14 // 5

print('\nDivisión 14/3:',division)
print(type(division))
print('\nDivisión entera 14/3:',division_entera)
print(type(division_entera))

potencia = 3 ** 3
print('\nPotencia 3 a la 3:',potencia)
print(type(potencia))

raiz_cuadrada = 25 ** 0.5
print('\nRaiz Cuadrada de 25:',raiz_cuadrada)
print(type(raiz_cuadrada))

raiz_cubica = 27 ** (1/3)
print('\nRaiz Cúbica de 27:',raiz_cubica)
print(type(raiz_cubica))