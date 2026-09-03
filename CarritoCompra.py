class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} : ${self.precio}"


class CarritoCompra:
    def __init__(self):
        self.productos = []

    def agregar(self, producto):
        if producto.precio > 0:
            self.productos.append(producto)
        

    def total(self):
        total = 0

        for producto in self.productos:
            total += producto.precio

        return total

    def mostrar(self):
        for producto in self.productos:
            print(producto)
        print("Total a pagar: $",  self.total())

p1 = Producto("Aire acondicionado", 1000000)
p2 = Producto("ventilador", 500000)
p3 = Producto("Estufa", 300000)

carrito = CarritoCompra()

carrito.agregar(p1)
carrito.agregar(p2)
carrito.agregar(p3)

carrito.mostrar()



