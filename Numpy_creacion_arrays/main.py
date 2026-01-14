# coding=utf-8

"""
============================
Programa:       numpy_creacion_arrays
Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

Propósito:
----------
- Demostrar la creación de arrays básicos desde listas usando la librería numpy
- Arreglos de valores especiales: ceros, unos, matriz identidad, matriz constante
- Creación de arreglos con secuencias numéricas
- Creación de arreglos con valores aleatorios
============================
"""

import numpy as np

print("=" * 60)
print("CREACIÓN DE ARREGLOS BÁSICOS")
print("=" * 60)

# 1. Crear arreglo 1D desde una lista
print("\n1. Arreglo 1D (vector) desde lista:")
arreglo_1d = np.array([1, 2, 3, 4, 5])
print(f"   {arreglo_1d}")
print(f"   Tipo: {type(arreglo_1d)}")

# 2. arreglo 2D (matriz) desde lista de listas
print("\n2. Arreglo 2D (matriz) desde lista de listas:")
arreglo_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(arreglo_2d)
print(f"   Dimensiones: {arreglo_2d.shape}")

print("\n" + "=" * 60)
print("ARRAYS CON VALORES ESPECIALES")
print("=" * 60)

# 3. arreglo de ceros
print("\n3. arreglo de ceros (3x4):")
arreglo_zeros = np.zeros((3, 4))
print(arreglo_zeros)

# 4. arreglo de unos
print("\n4. arreglo de unos (2x3):")
arreglo_unos = np.ones((2, 3))
print(arreglo_unos)

# 5. Matriz identidad
print("\n5. Matriz identidad (4x4):")
matriz_identidad = np.eye(4)
print(matriz_identidad)

# 6. matriz con un valor constante
print("\n6. Array con valor constante 7 (2x3):")
matriz_constante = np.full((2, 3), 7)
print(matriz_constante)

print("\n" + "=" * 60)
print("ARRAYS CON SECUENCIAS")
print("=" * 60)

# 7. Secuencia con arange (similar a range())
print("\n7. Secuencia con arange (0 a 10, paso 2):")
secuencia = np.arange(0, 10, 2)
print(f"   {secuencia}")

print("\n8. Arange con decimales (0 a 1, paso 0.2):")
secuencia_decimal = np.arange(0, 1, 0.2)
print(f"   {secuencia_decimal}")

# 9. Valores equiespaciados con linspace
print("\n9. Linspace (5 valores entre 0 y 1):")
equiespaciado = np.linspace(0, 1, 5)
print(f"   {equiespaciado}")

print("\n10. Linspace (10 valores entre 0 y 100):")
equiespaciado_100 = np.linspace(0, 100, 10)
print(f"   {equiespaciado_100}")

print("\n" + "=" * 60)
print("ARRAYS ALEATORIOS")
print("=" * 60)

# Configurar semilla para reproducibilidad
np.random.seed(42)

# 11. Array aleatorio con valores entre 0 y 1
print("\n11. Array aleatorio 2x3 (valores entre 0 y 1):")
aleatorio = np.random.rand(2, 3)
print(aleatorio)

# 12. Array aleatorio con distribución normal
print("\n12. Array aleatorio con distribución normal (3x3):")
normal = np.random.randn(3, 3)
print(normal)

# 13. Enteros aleatorios
print("\n13. Enteros aleatorios entre 0 y 10 (2x4):")
enteros = np.random.randint(0, 10, size=(2, 4))
print(enteros)

print("\n" + "=" * 60)
print("COMPARACIÓN DE MÉTODOS")
print("=" * 60)

print("\n📌 arange vs linspace:")
print("   arange(0, 10, 2):", np.arange(0, 10, 2))
print("   linspace(0, 10, 5):", np.linspace(0, 10, 5))
print("\n   → arange: especificas el PASO")
print("   → linspace: especificas CUÁNTOS valores quieres")