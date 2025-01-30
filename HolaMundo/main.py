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

# Aqui declaramos una variable y le asignamos el valor inicial
unaFrase = 'Esta es una frase almacenada en una variable'
print(unaFrase)

# Se pueden combinar varias frases utilizando el operador "+"
otraFrase = 'Esta es otra frase en otra variable'
print(unaFrase + "\n" + otraFrase)
