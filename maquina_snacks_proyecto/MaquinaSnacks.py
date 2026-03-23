

from ServicioSnacks import ServicioSnacks
from snack import Snack


class MaquinaSnacks:
    def __init__(self):
        self.servicio_snacks = ServicioSnacks()
        self.productos = []

    def maquina_snacks(self):
        salir = False
        print("*** Maquina Snacks ***")
        self.servicio_snacks.mostrar_snacks()
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f"Error: {e}")
    
    def mostrar_menu(self):
        print(f'''Menu:
              1. Comprar Snack
              2. Mostrar Snacks
              3. Agregar Nuevo Snack al Inventario
              4. Inventario de Snacks
              5. Salir
              ''')
        return int(input("Seleccione una opción: "))
    
    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.comprar_snack()
        elif opcion == 2:
            self.mostrar_ticket()
        elif opcion == 3:
            self.agregar_snack()
        elif opcion == 4:
            self.servicio_snacks.mostrar_snacks()
        elif opcion == 5:
            print("Gracias por usar la Maquina de Snacks. ¡Hasta luego!")
            return True
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")
        return False
    
    def comprar_snack(self):
        id_snack = int(input("Ingrese el ID del snack que desea comprar: "))
        snacks = self.servicio_snacks.get_snacks()
        snack = next((snack for snack in snacks if snack.id_snack == id_snack), None)
        if snack:
            self.productos.append(snack)
            print(f"Snack '{snack.nombre}' agregado a su compra.")
        else:
            print("Snack no encontrado.")

    def mostrar_ticket(self):
        if not self.productos:
            print("No ha comprado ningún snack.")
            return
        print("Ticket de Compra:")
        total = sum(snack.precio for snack in self.productos)
        for producto in self.productos:
            print(f"{producto.nombre} - ${producto.precio}")
        print(f"Total: ${total}")

    def agregar_snack(self):
        nombre = input("Ingrese el nombre del nuevo snack: ")
        precio = float(input("Ingrese el precio del nuevo snack: "))
        nuevo_snack = Snack(nombre, precio)
        self.servicio_snacks.agregar_snack(nuevo_snack)
        print(f"Snack '{nombre}' agregado al inventario.")

if __name__ == "__main__":
    maquina = MaquinaSnacks()
    maquina.maquina_snacks()