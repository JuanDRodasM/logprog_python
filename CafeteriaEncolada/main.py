from collections import deque
#coding=utf-8

"""
===============================================================================
 Programa: CafeteriaEncolada
 Contacto: Juan Dario Rodas - juand.rodasm@upb.edu.co

 Propósito:
 ----------
- Aplicación de una cola para gestionar clientes de una cafeteria

 ===============================================================================
"""

def agrega_cliente_producto(nombre_cliente, nombre_producto):
    nuevo_pedido = { "nombre": nombre_cliente,
                     "producto": nombre_producto
                    }
    cola_clientes.append(nuevo_pedido)

def visualiza_clientes_pendientes(una_cola):
    print(f'\nEn la cola hay actualmente {len(una_cola)} clientes');

    for cliente in una_cola:
        print(f'- {cliente["nombre"]} está esperando {cliente["producto"]}')

def visualiza_clientes_atendidos(una_lista):
    print(f'Se han atendido {len(una_lista)} clientes:')

    for cliente in una_lista:
        print(f'- {cliente["nombre"]} pidió {cliente["producto"]}')

def atiende_siguiente_cliente(una_cola):
    siguiente_cliente = una_cola.popleft()
    print(f'\nPreparando {siguiente_cliente["producto"]} para {siguiente_cliente["nombre"]}')
    clientes_atenidos.append(siguiente_cliente)

#Aqui comienza nuestro programa principal
print('Programa para gestionar clientes en cafetería JOSÉ TOSTAO')
cola_clientes = deque()
clientes_atenidos = []


agrega_cliente_producto('Sofia','Capuccino')
agrega_cliente_producto('Emanuel','Perico')
visualiza_clientes_pendientes(cola_clientes)
agrega_cliente_producto('Samuel','CocaCola original')
visualiza_clientes_pendientes(cola_clientes)

atiende_siguiente_cliente(cola_clientes)
visualiza_clientes_pendientes(cola_clientes)

print('\nLos clientes atendidos fueron:')
visualiza_clientes_atendidos(clientes_atenidos)