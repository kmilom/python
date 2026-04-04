"""Ejercicios de POO con Python"""

# 1. Clase básica

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

p1 = Persona("Camilo Moran", 26)
print(p1.presentarse())

# 2. Producto

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def aplicar_descuento(self, porcentaje):
        self.precio -= self.precio * porcentaje / 100
        return self.precio
    
p2 = Producto("manzana", 100)
print(f"El precio del producto con 10% de descuento: {p2.aplicar_descuento(10)}")

# 3. Cuenta bancaria

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("Error. Monto incorrecto")
        self.saldo += monto
        return self.saldo
    
    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            raise ValueError("Error. Saldo insuficiente")
        return self.saldo

c1 = CuentaBancaria("Camilo", 100)
print(c1.depositar(50))
print(c1.retirar(100))
#print(c1.retirar(100))

# 4. Estudiante

class Estudiante:
    def __init__(self, nombre, lista_notas):
        self.nombre = nombre
        self.lista_notas = lista_notas
    
    def promedio(self):
        return sum(n for n in self.lista_notas) / len(self.lista_notas)
    
    def estado(self):
        if self.promedio() >= 3:
            return "Aprobado"
        else:
            return "Reprobado"

e1 = Estudiante("Camilo", [3,1.5,4.5])
print(f"Promedio: {e1.promedio()}")
print(f"Estado: {e1.estado()}")

# 5. Carrito

class ProductoCarrito:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Carrito:
    def __init__(self):
        self.lista_productos = []
    
    def agregar_producto(self, producto):
        self.lista_productos.append(producto)

    def mostrar_carrito(self):
        for p in self.lista_productos:
            print(p.nombre, p.precio, p.cantidad)

    def calcular_total(self):
        return sum(p.cantidad * p.precio for p in self.lista_productos)

carrito = Carrito()
producto1 = ProductoCarrito("bolsa de arroz", 5, 3)
producto2 = ProductoCarrito("bolsa de azucar", 5, 3)
carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)

carrito.mostrar_carrito()
print(f"Total: {carrito.calcular_total()}")