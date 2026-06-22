class Producto:
    
    def __init__(self, id_producto, nombre, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
    
    def mostrar_informacion(self):
        print(f"ID: {self.id_producto}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")    
    
    def __str__(self):
        return f"Producto(id_producto={self.id_producto}, nombre='{self.nombre}', precio={self.precio})"
    