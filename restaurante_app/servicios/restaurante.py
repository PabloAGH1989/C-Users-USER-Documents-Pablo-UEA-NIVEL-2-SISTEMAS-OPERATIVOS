class Restaurante:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.clientes = []
        self.plato = []
        self.bebida = []

    def mostrar_clientes(self):
        for cliente in self.clientes:
            cliente.mostrar_informacion()
    def agregar_cliente(self):
        self.clientes.append(cliente)
    def agregar_plato(self, plato):
        self.plato.append(plato)    
    def agregar_bebida(self, bebida):
        self.bebida.append(bebida)  
    def mostrar_menu(self):
        for plato in self.plato:
            print(f"Plato: {plato.nombre}, Precio: {plato.precio}")
        for bebida in self.bebida:
            print(f"Bebida: {bebida.nombre}, Precio: {bebida.precio}")
      
    