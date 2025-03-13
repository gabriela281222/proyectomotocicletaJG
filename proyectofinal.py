############################################################
# Nombre del Programa: Registro de venta de moto toro JG   #
# Autor: Jocely Garcia                                     #
# Versión: 1.0                                             #
# Descripción: programa de regsitro de venta de            #         
# moto toro JG                                             #
############################################################

# INICIALIZANDO LAS VARIABLES NECESARIAS
nombre_cliente = ''
direccion = ''
marca_moto = ''
modelo_moto = ''
cantidad = 0
precio = 0

import re

# Lista de modelos de motos permitidos
MODELOS_PERMITIDOS = ["Jaguar Tr150cc", "Leon Tr200cc", "Rex Tr250cc","Fox TR180cc","Power Tr180cc", "tank Tr180cc"]

# Diccionario de precios fijos por modelo
PRECIOS_POR_MODELO = {
    "Jaguar Tr150cc": 1500.0,
    "Leon Tr200cc": 2000.0,
    "Rex Tr250cc": 2500.0,
    "Fox TR180cc": 1800.0,
    "Power Tr180cc": 1800.0,
    "tank Tr180cc": 1800.0
}

# Función para validar el nombre del cliente
def validar_nombre_cliente(nombre_cliente):
    return len(nombre_cliente) > 0

# Función para validar la dirección
def validar_direccion(direccion):
    return len(direccion) > 0

# Función para validar la marca de la moto
def validar_marca_moto(marca_moto):
    return marca_moto == "Toro"

# Función para validar el modelo de la moto
def validar_modelo_moto(modelo_moto):
    return modelo_moto in MODELOS_PERMITIDOS

# Función para validar la cantidad
def validar_cantidad(cantidad):
    try:
        cantidad = int(cantidad)
        return cantidad > 0
    except ValueError:
        return False

# Función para introducir un nuevo registro
def introducir_registro(registros):

    nombre_cliente = input("Introduce el nombre del cliente: ")
    while not validar_nombre_cliente(nombre_cliente):
        print("Nombre del cliente inválido.")
        nombre_cliente = input("Introduce el nombre del cliente: ")

    direccion = input("Introduce la dirección del cliente: ")
    while not validar_direccion(direccion):
        print("Dirección inválida.")
        direccion = input("Introduce la dirección del cliente: ")

    marca_moto = input("Introduce la marca de la moto: ")
    while not validar_marca_moto(marca_moto):
        print("Marca de la moto inválida.")
        marca_moto = input("Introduce la marca de la moto: ")

    modelo_moto = input("Introduce el modelo de la moto: ")
    while not validar_modelo_moto(modelo_moto):
        print("Modelo de la moto inválido.")
        modelo_moto = input("Introduce el modelo de la moto: ")

    precio = PRECIOS_POR_MODELO[modelo_moto]

    cantidad = input("Introduce la cantidad: ")
    while not validar_cantidad(cantidad):
        print("Cantidad inválida. Debe ser un número entero positivo.")
        cantidad = input("Introduce la cantidad: ")

    registros.append({
        
        'nombre_cliente': nombre_cliente,
        'direccion': direccion,
        'marca_moto': marca_moto,
        'modelo_moto': modelo_moto,
        'precio': precio,
        'cantidad': int(cantidad)
    })
    print("Registro introducido con éxito.")

    # Función para modificar un registro existente
def modificar_registro(registros):
    nombre_cliente = input("Introduce el nuevo nombre del cliente: ")
    while not validar_nombre_cliente(nombre_cliente):
        print("Nombre del cliente inválido.")
        nombre_cliente = input("Introduce el nuevo nombre del cliente: ")

    direccion = input("Introduce la nueva dirección del cliente: ")
    while not validar_direccion(direccion):
        print("Dirección inválida.")
        direccion = input("Introduce la nueva dirección del cliente: ")

    marca_moto = input("Introduce la nueva marca de la moto: ")
    while not validar_marca_moto(marca_moto):
        print("Marca de la moto inválida.")
        marca_moto = input("Introduce la nueva marca de la moto: ")

    modelo_moto = input("Introduce el nuevo modelo de la moto: ")
    while not validar_modelo_moto(modelo_moto):
        print("Modelo de la moto inválido.")
        modelo_moto = input("Introduce el nuevo modelo de la moto: ")

    precio = PRECIOS_POR_MODELO[modelo_moto]

    cantidad = input("Introduce la nueva cantidad: ")
    while not validar_cantidad(cantidad):
        print("Cantidad inválida. Debe ser un número entero positivo.")
        cantidad = input("Introduce la nueva cantidad: ")

    for registro in registros:
        if registro['nombre_cliente'] == nombre_cliente:
            registro['nombre_cliente'] = nombre_cliente
            registro['direccion'] = direccion
            registro['marca_moto'] = marca_moto
            registro['modelo_moto'] = modelo_moto
            registro['precio'] = precio
            registro['cantidad'] = int(cantidad)
            print("Registro modificado con éxito.")
            return
    print("Registro no encontrado.")

# Función para imprimir la lista de registros
def imprimir_lista_registros(registros):
    if not registros:
        print("No hay registros para mostrar.")
        return

    for registro in registros:
        print(f"Nombre del Cliente: {registro['nombre_cliente']}, Dirección: {registro['direccion']}, Marca de la Moto: {registro['marca_moto']}, Modelo de la Moto: {registro['modelo_moto']}, Precio: {registro['precio']}, Cantidad: {registro['cantidad']}")

# Función principal del menú
def menu():
    registros = []
    while True:
        print("\nMenú:")
        print("1. Introducir Registro")
        print("2. Modificar Registro")
        print("3. Imprimir Lista de Registros")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            introducir_registro(registros)
        elif opcion == '2':
            modificar_registro(registros)
        elif opcion == '3':
            imprimir_lista_registros(registros)
        elif opcion == '4':
            break
        else:
            print("Opción inválida. Por favor, elige una opción válida.")

if __name__ == "__main__":
    menu()