import os

from snack import Snack


class ServicioSnacks:
    NOMBRE_ARCHIVO = "snacks.txt"

    def __init__(self):
        self.snacks = []
        # revisar si ya existe el archivo
        #Si ya existe obtenemos los snacks
        #si no existe el archivo se crea uno nuevo
        if os.path.exists(ServicioSnacks.NOMBRE_ARCHIVO):
            self.snacks = self.obtener_snacks()
        else:
            self.cargar_snacks_iniciales()
    
    def cargar_snacks_iniciales(self):
        snacks_iniciales = [
            Snack("Papas fritas", 1.5),
            Snack("Galletas", 1.0),
            Snack("Chocolates", 2.0),
            Snack("Refrescos", 1.25)
        ]
        self.snacks.extend(snacks_iniciales)
        self.guardar_snacks_archivo(snacks_iniciales)

    def guardar_snacks_archivo(self, snacks):
        try:
            with open(self.NOMBRE_ARCHIVO, 'a') as archivo:
                for snack in snacks:
                    archivo.write(snack.escribir_snack())
        except Exception as e:
            print(f"Error al guardar snacks: {e}")

    def obtener_snacks(self):
        snacks = []
        try:
            with open(self.NOMBRE_ARCHIVO, 'r') as archivo:
                for linea in archivo:
                    id_snack,nombre,precio = linea.strip().split(',')
                    snack = Snack(nombre, float(precio))
                    snack.id_snack = int(id_snack)  # Asignar el ID del snack
                    snacks.append(snack)
        except Exception as e:
            print(f"Error al obtener snacks: {e}")
        return snacks

    def agregar_snack(self, snack):
        self.snacks.append(snack)
        self.guardar_snacks_archivo([snack])

    def mostrar_snacks(self):
        print("------ Snacks disponibles -------")
        for snack in self.snacks:
            print(snack)

    def get_snacks(self):
        return self.snacks