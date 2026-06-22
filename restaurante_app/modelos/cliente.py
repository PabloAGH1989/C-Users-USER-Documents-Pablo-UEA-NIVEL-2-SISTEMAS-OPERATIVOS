class Cliente:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.pedidos = []

    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Email: {self.email}")
        print(f"Telefono: {self.telefono}")


    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}, Telefono: {self.telefono}"