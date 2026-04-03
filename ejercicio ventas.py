"""Ejercicio práctico en Python"""


ventas = [
    {"cliente": "Camilo", "producto": "Laptop", "precio": 3000, "cantidad": 1},
    {"cliente": "Ana", "producto": "Mouse", "precio": 50, "cantidad": 2},
    {"cliente": "Camilo", "producto": "Teclado", "precio": 100, "cantidad": 1},
    {"cliente": "Luis", "producto": "Monitor", "precio": 800, "cantidad": 2},
    {"cliente": "Ana", "producto": "Laptop", "precio": 3000, "cantidad": 1},
]

def calcular_total_ventas(ventas):
    for venta in ventas:
        venta["total"] = venta["precio"] * venta["cantidad"]
    total_ventas = sum(venta["total"] for venta in ventas)
    return total_ventas
    
def buscar_mejor_cliente(totales):
    mejor_cliente = max(totales, key=totales.get)
    return mejor_cliente

def armar_diccionario(ventas, clave, valor):
    resultado = {}
    for venta in ventas:
        clave_resultado = venta[clave]
        valor_resultado = venta[valor]   
        if clave_resultado in resultado:
            resultado[clave_resultado] += valor_resultado
        else:
            resultado[clave_resultado] = valor_resultado
    return resultado

def calcular_total_ventas_x_cliente(ventas):
    dict_ventas = armar_diccionario(ventas, "cliente", "total")
    return dict_ventas

def buscar_mas_vendido(ventas):
    productos_vendidos = armar_diccionario(ventas, "producto", "cantidad")
    producto_mas_vendido = max(productos_vendidos, key=productos_vendidos.get)
    return productos_vendidos, producto_mas_vendido

def set_productos(productos_vendidos):
    return set(productos_vendidos.keys())

def filtrar_mejores_ventas(ventas):
    lista_mejores_ventas = [venta for venta in ventas if venta["total"] > 500]
    return lista_mejores_ventas

total_ventas = calcular_total_ventas(ventas)
print(f"El total de ventas es: $ {total_ventas}")
totales = calcular_total_ventas_x_cliente(ventas)
print(f"El total de ventas por cliente es:\n{totales}")
mejor_cliente = buscar_mejor_cliente(totales)
print(f"El cliente con la mayor compra es: {mejor_cliente}")
productos_vendidos, producto_mas_vendido = buscar_mas_vendido(ventas)
print(f"El producto más vendido es: {producto_mas_vendido}")
productos = set_productos(productos_vendidos)
print(f"Lista de productos vendidos:\n{productos}")
mejores_ventas = filtrar_mejores_ventas(ventas)
print(f"Lista de mejores ventas:\n{mejores_ventas}")