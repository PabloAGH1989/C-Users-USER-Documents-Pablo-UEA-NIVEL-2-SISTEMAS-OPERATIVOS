from modelos.cliente import Cliente
from modelos.producto import Producto
from servicios.restaurante import Restaurante

cliente1 = Cliente("Juan", "Perez", "123456789")
restaurante1 = Restaurante("Restaurante X", "Dirección X", "987654321")
plato1 = Producto(1, "Plato A", 10.99)
bebida1 = Producto(2, "Bebida B", 5.99) 
restaurante1.agregar_plato(plato1)
restaurante1.agregar_bebida(bebida1)    
print("Información del cliente:")
cliente1.mostrar_informacion()  
print("\nMenú del restaurante:")
restaurante1.mostrar_menu()

cliente2 = Cliente("Maria", "Gomez", "987654321")
restaurante2 = Restaurante("Restaurante Y", "Dirección Y", "123456789   ")
plato2 = Producto(3, "Plato C", 12.99)
bebida2 = Producto(4, "Bebida D", 6.99) 
restaurante2.agregar_plato(plato2)
restaurante2.agregar_bebida(bebida2)    
print("\nInformación del cliente:")
cliente2.mostrar_informacion()
print("\nMenú del restaurante:")
restaurante2.mostrar_menu()

cliente3 = Cliente("Carlos", "Lopez", "555555555")
restaurante3 = Restaurante("Restaurante Z", "Dirección Z", "111111111")
plato3 = Producto(5, "Plato E", 15.99)
bebida3 = Producto(6, "Bebida F", 7.99)
restaurante3.agregar_plato(plato3)
restaurante3.agregar_bebida(bebida3)
print("\nInformación del cliente:")
cliente3.mostrar_informacion()
print("\nMenú del restaurante:")
restaurante3.mostrar_menu()

restaurante = Restaurante()

restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)
restaurante.agregar_cliente(cliente3)

restaurante.agregar_plato(plato1)
restaurante.agregar_plato(plato2)
restaurante.agregar_plato(plato3)

restaurante.agregar_bebida(bebida1)
restaurante.agregar_bebida(bebida2)
restaurante.agregar_bebida(bebida3)

print("\nClientes registrados en el restaurante:")
restaurante.mostrar_clientes()
