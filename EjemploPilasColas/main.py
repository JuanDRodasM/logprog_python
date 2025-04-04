from collections import deque
#coding=utf-8

"""
===============================================================================
 Programa: EjemploPilasColas
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Demostración inicial del funcionamiento y diferencias entre una pila y una cola

 ===============================================================================
"""

def visualiza_participantes(una_pila):
    print(f'\nLa cantidad participantes es: {len(una_pila)}')
    print('Los participantes son:')

    for participante in una_pila:
        print(f' - {participante}')

def visualiza_pacientes(una_cola):
    print(f'\nLa cantidad de pacientes es: {len(una_cola)}')

    for paciente in una_cola:
        print(f' - {paciente}')


print('Programa para demostrar el funcionamiento de una pila y una cola')
print('\nPara una pila - Principio LIFO:')

pila_participantes = []

#Agregar elementos - Push
pila_participantes.append('Miguel')
pila_participantes.append('Matias')
pila_participantes.append('Samuel')
pila_participantes.append('Emanuel')

visualiza_participantes(pila_participantes)

#Quitamos el último de la cola - pop
ultimo_participante = pila_participantes.pop()
print(f'\nEl último participante es {ultimo_participante}')

visualiza_participantes(pila_participantes)

siguiente_en_salir = pila_participantes.pop()
print(f'\nEl siguiente participante es {siguiente_en_salir}')
visualiza_participantes(pila_participantes)

print('\nPara una Cola - Principio FIFO:')
cola_pacientes = deque()

#Añadir pacientes a la cola (enqueue - encolamiento)
cola_pacientes.append('Miguel')
cola_pacientes.append('Matias')
cola_pacientes.append('Samuel')
cola_pacientes.append('Emanuel')

visualiza_pacientes(cola_pacientes)

#Sacar el proximo paciente (dequeque - desencolamiento)
proximo_paciente = cola_pacientes.popleft()
print(f'\nEl proximo_paciente es {proximo_paciente}')
visualiza_pacientes(cola_pacientes)

el_siguiente_paciente = cola_pacientes.popleft()
print(f'\nEl siguiente es {el_siguiente_paciente}')
visualiza_pacientes(cola_pacientes)
