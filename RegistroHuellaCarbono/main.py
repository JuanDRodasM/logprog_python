#coding=utf-8

# ======================================================================
# Programa:       RegistroHuellaCarbono
# Contacto:       Juan Dario Rodas - juand.rodasm@upb.edu.co

# Propósito:
# ----------
#- Demostrar el funcionamiento del ciclo de control While,
# Condicionales, contadores y totalizadores.
# ======================================================================

total_servicios = 12
kms_minimos = 5
gr_co2_km = 43

servicios_registrados = 0
total_kilometros = 0

print('Registro de Huella de Carbono - Ligerini')

# Ciclo principal para registro de servicios
while servicios_registrados < total_servicios:

   distancia = float(input(f'\nIngrese la distancia recorrida en kilómetros para el recorrido No {servicios_registrados+1}: '))
   if distancia < kms_minimos:
       print(f'Registro inválido. La distancia mínima por recorrido debe ser de {kms_minimos} kms. Intente nuevamente.')
   else:
       total_kilometros += distancia
       servicios_registrados+=1

#Calculos finales y visualización de resultados
total_co2 = total_kilometros * gr_co2_km
promedio_co2 = total_co2 / total_servicios

print("RESULTADOS DEL REGISTRO")
print(f"Total de kilómetros recorridos: {total_kilometros:.2f} km")
print(f"Total de CO2 generado: {total_co2:.2f} gr")
print(f"En {total_servicios} servicios, el promedio de CO2 fue de: {promedio_co2:.2f} gr")
