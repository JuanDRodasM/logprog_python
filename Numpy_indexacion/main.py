# coding=utf-8

"""
============================
Programa:       numpy_indexacion
Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

Propósito:
----------
- Demostrar cómo acceder a elementos individuales en arrays de diferentes dimensiones.
============================
"""

import numpy as np

print("=" * 60)
print("INDEXACIÓN EN ARREGLOS 1D (VECTORES)")
print("=" * 60)

arreglo_1d = np.array([10, 20, 30, 40, 50])
print("\nArreglo 1D:", arreglo_1d)
print(f"Índices:   [0] [1] [2] [3] [4]")

print("\n" + "-" * 60)
print("Acceso por índice positivo:")
print("-" * 60)
print(f"arreglo_1d[0] = {arreglo_1d[0]}  (primer elemento)")
print(f"arreglo_1d[2] = {arreglo_1d[2]}  (tercer elemento)")
print(f"arreglo_1d[4] = {arreglo_1d[4]}  (quinto elemento)")

print("\n" + "-" * 60)
print("Acceso por índice negativo:")
print("-" * 60)
print(f"arreglo_1d[-1] = {arreglo_1d[-1]}  (último elemento)")
print(f"arreglo_1d[-2] = {arreglo_1d[-2]}  (penúltimo elemento)")
print(f"arreglo_1d[-5] = {arreglo_1d[-5]}  (primer elemento desde el final)")

print("\n💡 Los índices negativos cuentan desde el final del arreglo")

print("\n" + "=" * 60)
print("INDEXACIÓN EN ARREGLOS 2D (MATRICES)")
print("=" * 60)

arreglo_2d = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

print("\nArreglo 2D:")
print(arreglo_2d)

print("\n" + "-" * 60)
print("Acceso a elementos individuales [fila, columna]:")
print("-" * 60)
print(f"arreglo_2d[0, 0] = {arreglo_2d[0, 0]}  (fila 0, columna 0)")
print(f"arreglo_2d[0, 2] = {arreglo_2d[0, 2]}  (fila 0, columna 2)")
print(f"arreglo_2d[1, 3] = {arreglo_2d[1, 3]}  (fila 1, columna 3)")
print(f"arreglo_2d[2, 3] = {arreglo_2d[2, 3]}  (fila 2, columna 3)")

print("\n" + "-" * 60)
print("Acceso a filas completas:")
print("-" * 60)
print(f"arreglo_2d[0] = {arreglo_2d[0]}  (primera fila)")
print(f"arreglo_2d[1] = {arreglo_2d[1]}  (segunda fila)")
print(f"arreglo_2d[-1] = {arreglo_2d[-1]}  (última fila)")

print("\n" + "-" * 60)
print("Acceso con índices negativos:")
print("-" * 60)
print(f"arreglo_2d[-1, -1] = {arreglo_2d[-1, -1]}  (última fila, última columna)")
print(f"arreglo_2d[-2, -3] = {arreglo_2d[-2, -3]}  (penúltima fila, antepenúltima columna)")

print("\n" + "=" * 60)
print("INDEXACIÓN EN ARREGLOS 3D (TENSORES)")
print("=" * 60)

# Crear un tensor 3D: 2 bloques, 3 filas, 4 columnas
arreglo_3d = np.array([[[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12]],

                   [[13, 14, 15, 16],
                    [17, 18, 19, 20],
                    [21, 22, 23, 24]]])

print(f"\nArreglo 3D shape: {arreglo_3d.shape}")
print("(2 bloques × 3 filas × 4 columnas)\n")
print(arreglo_3d)

print("\n" + "-" * 60)
print("Acceso a elementos [bloque, fila, columna]:")
print("-" * 60)
print(f"arreglo_3d[0, 0, 0] = {arreglo_3d[0, 0, 0]}  (bloque 0, fila 0, columna 0)")
print(f"arreglo_3d[0, 1, 2] = {arreglo_3d[0, 1, 2]}  (bloque 0, fila 1, columna 2)")
print(f"arreglo_3d[1, 2, 3] = {arreglo_3d[1, 2, 3]}  (bloque 1, fila 2, columna 3)")

print("\n" + "-" * 60)
print("Acceso a bloques y sub-matrices:")
print("-" * 60)
print(f"arreglo_3d[0] =\n{arreglo_3d[0]}")
print(f"\narreglo_3d[1, 0] = {arreglo_3d[1, 0]}  (primera fila del segundo bloque)")

print("\n" + "=" * 60)
print("MODIFICACIÓN DE ELEMENTOS")
print("=" * 60)

arreglo_ejemplo = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("\nArreglo original:")
print(arreglo_ejemplo)

# Modificar un elemento
arreglo_ejemplo[0, 1] = 99
print("\nDespués de arreglo_ejemplo[0, 1] = 99:")
print(arreglo_ejemplo)

# Modificar una fila completa
arreglo_ejemplo[2] = [70, 80, 90]
print("\nDespués de arreglo_ejemplo[2] = [70, 80, 90]:")
print(arreglo_ejemplo)

print("\n💡 Los arreglos de NumPy son mutables (se pueden modificar)")
