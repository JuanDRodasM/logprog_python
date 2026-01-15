# coding=utf-8

"""
============================
Programa:       Numpy_operaciones_aritmeticas
Contacto:       Juan Dario Rodas - jdrodas@hotmail.com

Propósito:
----------
- Demostrar operaciones matemáticas elemento a elemento y operaciones con escalares en arreglo de NumPy.
- Demostrar operaciones con matrices y operaciones como ecuaciones lineales y cuadráticas
- Demostrar operaciones de comparación y funciones de redondeo
============================
"""

import numpy as np

print("=" * 60)
print("OPERACIONES ELEMENTO A ELEMENTO")
print("=" * 60)

arreglo1 = np.array([1, 2, 3, 4])
arreglo2 = np.array([10, 20, 30, 40])

print(f"\nArreglo 1: {arreglo1}")
print(f"Arreglo 2: {arreglo2}")

print("\n" + "-" * 60)
print("Operaciones básicas:")
print("-" * 60)

print(f"\nSuma (arreglo1 + arreglo2):")
print(f"   {arreglo1} + {arreglo2} = {arreglo1 + arreglo2}")

print(f"\nResta (arreglo1 - arreglo2):")
print(f"   {arreglo1} - {arreglo2} = {arreglo1 - arreglo2}")

print(f"\nMultiplicación (arreglo1 * arreglo2):")
print(f"   {arreglo1} * {arreglo2} = {arreglo1 * arreglo2}")

print(f"\nDivisión (arreglo2 / arreglo1):")
print(f"   {arreglo2} / {arreglo1} = {arreglo2 / arreglo1}")

print(f"\nDivisión entera (arreglo2 // arreglo1):")
print(f"   {arreglo2} // {arreglo1} = {arreglo2 // arreglo1}")

print(f"\nMódulo (arreglo2 % arreglo1):")
print(f"   {arreglo2} % {arreglo1} = {arreglo2 % arreglo1}")

print(f"\nPotencia (arreglo1 ** 2):")
print(f"   {arreglo1} ** 2 = {arreglo1 ** 2}")

print("\n" + "=" * 60)
print("OPERACIONES CON ESCALARES")
print("=" * 60)

arreglo = np.array([1, 2, 3, 4, 5])
print(f"\nArreglo original: {arreglo}")

print("\n" + "-" * 60)
print("Broadcasting con escalares:")
print("-" * 60)

print(f"\narr * 5 = {arreglo * 5}")
print(f"arr + 10 = {arreglo + 10}")
print(f"arr - 3 = {arreglo - 3}")
print(f"arr / 2 = {arreglo / 2}")
print(f"arr ** 3 = {arreglo ** 3}")

print("\nEl escalar se 'difunde' a cada elemento del arreglo")

print("\n" + "=" * 60)
print("OPERACIONES CON MATRICES 2D")
print("=" * 60)

matriz1 = np.array([[1, 2, 3],
                    [4, 5, 6]])

matriz2 = np.array([[10, 20, 30],
                    [40, 50, 60]])

print("\nMatriz 1:")
print(matriz1)

print("\nMatriz 2:")
print(matriz2)

print("\n" + "-" * 60)
print("Operaciones elemento a elemento:")
print("-" * 60)

print("\nMatriz 1 + Matriz 2:")
print(matriz1 + matriz2)

print("\nMatriz 2 - Matriz 1:")
print(matriz2 - matriz1)

print("\nMatriz 1 * Matriz 2 (elemento a elemento):")
print(matriz1 * matriz2)

print("\nMatriz 1 * 10 (escalar):")
print(matriz1 * 10)

print("\n" + "=" * 60)
print("OPERACIONES COMBINADAS")
print("=" * 60)

x = np.array([1, 2, 3, 4, 5])
print(f"\nx = {x}")

print("\n" + "-" * 60)
print("Expresiones matemáticas complejas:")
print("-" * 60)

# y = 2x + 1
y = 2 * x + 1
print(f"\ny = 2x + 1 = {y}")

# z = x² + 3x - 5
z = x ** 2 + 3 * x - 5
print(f"z = x² + 3x - 5 = {z}")

# Fórmula cuadrática: a*x² + b*x + c
a, b, c = 2, -3, 1
resultado = a * x ** 2 + b * x + c
print(f"\n{a}x² + {b}x + {c} = {resultado}")

print("\n" + "=" * 60)
print("OPERACIONES DE COMPARACIÓN")
print("=" * 60)

arreglo = np.array([1, 5, 10, 15, 20])
print(f"\nArray: {arreglo}")

print("\n" + "-" * 60)
print("Comparaciones (retornan arrays booleanos):")
print("-" * 60)

print(f"\narreglo > 10:")
print(f"  {arreglo > 10}")

print(f"\narreglo >= 10:")
print(f"  {arreglo >= 10}")

print(f"\narreglo == 10:")
print(f"  {arreglo == 10}")

print(f"\narreglo != 10:")
print(f"  {arreglo != 10}")

# Comparación entre arrays
arreglo2 = np.array([2, 4, 8, 16, 18])
print(f"\n\narreglo 1: {arreglo}")
print(f"arreglo 2: {arreglo2}")
print(f"\narreglo > arreglo2:")
print(f"  {arreglo > arreglo2}")

print("\n" + "=" * 60)
print("FUNCIONES DE REDONDEO")
print("=" * 60)

arreglo = np.array([1.234, 2.567, 3.891, -4.567, -5.123])
print(f"\nArray original: {arreglo}")

print("\n" + "-" * 60)
print("Diferentes tipos de redondeo:")
print("-" * 60)

print(f"\nnp.round(arreglo, 2) - Redondeo a 2 decimales:")
print(f"  {np.round(arreglo, 2)}")

print(f"\nnp.floor(arreglo) - Redondeo hacia abajo:")
print(f"  {np.floor(arreglo)}")

print(f"\nnp.ceil(arreglo) - Redondeo hacia arriba:")
print(f"  {np.ceil(arreglo)}")

print(f"\nnp.trunc(arreglo) - Truncar (eliminar decimales):")
print(f"  {np.trunc(arreglo)}")