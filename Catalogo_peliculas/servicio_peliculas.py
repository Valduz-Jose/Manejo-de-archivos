import os

class ServicioPeliculas:

    def __init__(self):
        self.nombre_archivo = "peliculas.txt"

    def agregar_pelicula(self, pelicula):
        with open(self.nombre_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(pelicula.nombre + '\n')

    def listar_peliculas(self):
        try:
            with open(self.nombre_archivo, 'r', encoding='utf-8') as archivo:
                print("--- Películas en el catálogo ---")
                print(archivo.read())
        except FileNotFoundError:
            print("No se encontró el archivo de películas.")
    
    def eliminar_archivo_peliculas(self):
        if os.path.exists(self.nombre_archivo):
            os.remove(self.nombre_archivo)
            print("Archivo de películas eliminado.")
        else:
            print("No se encontró el archivo de películas para eliminar.")