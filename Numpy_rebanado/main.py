# coding=utf-8

"""
============================
Programa:       numpy_rebanado
Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

Propósito:
----------
- Demostrar técnicas de slicing (rebanado) para extraer porciones de arrays, incluyendo indexación booleana y fancy indexing.
============================
"""

import numpy as np

print("=" * 60)
print("SLICING EN ARREGLOS 1D")
print("=" * 60)

arreglo = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print("\nArray original:", arreglo)
print("Índices:        [0] [1] [2] [3] [4] [5] [6] [7] [8]")

print("\n" + "-" * 60)
print("Sintaxis básica: arreglo[inicio:fin:paso]")
print("-" * 60)

print(f"\narreglo[0:3]   = {arreglo[0:3]}  (del índice 0 al 2)")
print(f"arreglo[2:7]   = {arreglo[2:7]}  (del índice 2 al 6)")
print(f"arreglo[2:]    = {arreglo[2:]}  (del índice 2 al final)")
print(f"arreglo[:5]    = {arreglo[:5]}  (desde el inicio hasta el índice 4)")
print(f"arreglo[:]     = {arreglo[:]}  (todo el array)")

print("\n" + "-" * 60)
print("Usando pasos (step):")
print("-" * 60)

print(f"\narreglo[::2]   = {arreglo[::2]}  (cada 2 elementos)")
print(f"arreglo[1::2]  = {arreglo[1::2]}  (desde índice 1, cada 2 elementos)")
print(f"arreglo[::3]   = {arreglo[::3]}  (cada 3 elementos)")
print(f"arreglo[::-1]  = {arreglo[::-1]}  (invertir el array)")
print(f"arreglo[::-2]  = {arreglo[::-2]}  (cada 2 elementos, invertido)")

print("\n" + "-" * 60)
print("Con índices negativos:")
print("-" * 60)

print(f"\narreglo[-3:]   = {arreglo[-3:]}  (últimos 3 elementos)")
print(f"arreglo[:-3]   = {arreglo[:-3]}  (todo excepto los últimos 3)")
print(f"arreglo[-5:-2] = {arreglo[-5:-2]}  (del índice -5 al -3)")

print("\n" + "=" * 60)
print("SLICING EN ARREGLOS 2D")
print("=" * 60)

arreglo_2d = np.array([[1, 2, 3, 4, 5],
                   [6, 7, 8, 9, 10],
                   [11, 12, 13, 14, 15],
                   [16, 17, 18, 19, 20]])

print("\nArray 2D:")
print(arreglo_2d)

print("\n" + "-" * 60)
print("Slicing por filas:")
print("-" * 60)

print("\narreglo_2d[0:2] (primeras 2 filas):")
print(arreglo_2d[0:2])

print("\narreglo_2d[1:3] (filas 1 y 2):")
print(arreglo_2d[1:3])

print("\narreglo_2d[::2] (cada 2 filas):")
print(arreglo_2d[::2])

print("\n" + "-" * 60)
print("Slicing por filas y columnas [filas, columnas]:")
print("-" * 60)

print("\narreglo_2d[0:2, 0:3] (2 filas, 3 columnas):")
print(arreglo_2d[0:2, 0:3])

print("\narreglo_2d[:, 0:2] (todas las filas, primeras 2 columnas):")
print(arreglo_2d[:, 0:2])

print("\narreglo_2d[1:3, 2:5] (filas 1-2, columnas 2-4):")
print(arreglo_2d[1:3, 2:5])

print("\narreglo_2d[:, ::2] (todas las filas, cada 2 columnas):")
print(arreglo_2d[:, ::2])

print("\narreglo_2d[::2, ::2] (cada 2 filas, cada 2 columnas):")
print(arreglo_2d[::2, ::2])

print("\n" + "=" * 60)
print("SLICING EN ARREGLOS 3D")
print("=" * 60)

arreglo_3d = np.arange(24).reshape(2, 3, 4)

print(f"\nArray 3D shape: {arreglo_3d.shape}")
print(arreglo_3d)

print("\n" + "-" * 60)
print("Slicing en 3D [bloques, filas, columnas]:")
print("-" * 60)

print("\narreglo_3d[0, :, :] (todo el primer bloque):")
print(arreglo_3d[0, :, :])

print("\narreglo_3d[:, 0:2, :] (ambos bloques, primeras 2 filas):")
print(arreglo_3d[:, 0:2, :])

print("\narreglo_3d[:, :, 0:2] (ambos bloques, primeras 2 columnas):")
print(arreglo_3d[:, :, 0:2])

print("\n" + "=" * 60)
print("INDEXACIÓN BOOLEANA (BOOLEAN INDEXING)")
print("=" * 60)

arreglo_datos = np.array([5, 12, 3, 18, 7, 25, 9, 15])
print(f"\nArray original: {arreglo_datos}")

print("\n" + "-" * 60)
print("Crear máscaras booleanas:")
print("-" * 60)

mascara = arreglo_datos > 10
print(f"\nMáscara (datos > 10):")
print(f"  {mascara}")
print(f"  {arreglo_datos}")
print(f"  → Resultado: {arreglo_datos[mascara]}")

print(f"\nElementos menores que 10:")
print(f"  {arreglo_datos[arreglo_datos < 10]}")

print(f"\nElementos pares (divisibles entre 2):")
print(f"  {arreglo_datos[arreglo_datos % 2 == 0]}")

print("\n" + "-" * 60)
print("Condiciones múltiples (AND, OR):")
print("-" * 60)

# AND: ambas condiciones deben ser verdaderas
print(f"\nElementos entre 5 y 15 (inclusivo):")
print(f"  {arreglo_datos[(arreglo_datos >= 5) & (arreglo_datos <= 15)]}")

# OR: al menos una condición debe ser verdadera
print(f"\nElementos menores que 5 O mayores que 20:")
print(f"  {arreglo_datos[(arreglo_datos < 5) | (arreglo_datos > 20)]}")

# Negar una condición
print(f"\nElementos que NO son mayores que 10:")
print(f"  {arreglo_datos[~(arreglo_datos > 10)]}")

print("\nOperadores: & (AND), | (OR), ~ (NOT)")
print("¡Importante! Usar paréntesis en condiciones múltiples")

print("\n" + "=" * 60)
print("INDEXACIÓN BOOLEANA EN ARREGLOS 2D")
print("=" * 60)

matriz = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

print("\nMatriz original:")
print(matriz)

print("\n" + "-" * 60)
print("Filtrado de elementos:")
print("-" * 60)

print(f"\nElementos mayores que 5:")
print(f"  {matriz[matriz > 5]}")

print(f"\nElementos divisibles entre 3:")
print(f"  {matriz[matriz % 3 == 0]}")

# Modificar elementos usando máscaras
print("\n" + "-" * 60)
print("Modificar elementos con máscaras:")
print("-" * 60)

copia = matriz.copy()
print("\nAntes de modificar:")
print(copia)

copia[copia > 8] = 99
print("\nDespués de copia[copia > 8] = 99:")
print(copia)

print("\n" + "=" * 60)
print("FANCY INDEXING (INDEXACIÓN AVANZADA)")
print("=" * 60)

arreglo = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print(f"\nArreglo original: {arreglo}")

print("\n" + "-" * 60)
print("Seleccionar elementos específicos con lista de índices:")
print("-" * 60)

indices = [0, 2, 5, 7]
print(f"\nÍndices: {indices}")
print(f"arr[[0, 2, 5, 7]] = {arreglo[indices]}")

print(f"\narr[[1, 1, 3, 3]] = {arreglo[[1, 1, 3, 3]]}  (puede repetir índices)")

print("\n" + "-" * 60)
print("Fancy indexing en 2D:")
print("-" * 60)

matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("\nMatriz:")
print(matriz)

filas = [0, 2, 2]
columnas = [1, 0, 2]
print(f"\nFilas: {filas}, Columnas: {columnas}")
print(f"matriz[[0, 2, 2], [1, 0, 2]] = {matriz[filas, columnas]}")
print("  → Elementos: (0,1), (2,0), (2,2)")