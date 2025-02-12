#coding=utf-8

# ======================================================================
# Programa:       RegistroConsumoAgua
# Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

# Propósito:
# ----------
#- Demostrar el funcionamiento del ciclo de control While,
# Condicionales, contadores y totalizadores.
# ======================================================================

meta_diaria = 2000
volumen_minimo = 100
volumen_maximo = 400
total_porciones = 0

#Inicialización de la variable de control
volumen_total = 0

print('Programa para el registro de consumo diario de agua')
print(f'Meta diaria: {meta_diaria} ml')
print(f'Rango válido por porción: {volumen_minimo} - {volumen_maximo} ml\n')

while volumen_total <= meta_diaria:
    volumen_porcion = float(input('\nIngrese el volumen de agua consumido (en ml): '))

    if  volumen_porcion >= volumen_minimo and volumen_porcion <= volumen_maximo:
        volumen_total+=volumen_porcion # Condición de salida del condicional
        total_porciones+=1
    else:
        print(f"\nError: El volumen debe estar entre {volumen_minimo} y {volumen_maximo} ml")
        print("Por favor, registre nuevamente la porción\n")

    print(f'Llevas registradas {total_porciones} porciones para un total de {volumen_total} ml')

#Aqui se visualizan resultados
print("\nSe ha logrado la meta diaria de consumo de agua")
print(f"Resumen del día:")
print(f"- Volumen total consumido: {volumen_total} ml")
print(f"- Número de porciones: {total_porciones}")
