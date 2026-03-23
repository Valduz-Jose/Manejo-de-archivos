from pelicula import Pelicula
from servicio_peliculas import ServicioPeliculas


class AppCatalogoPeliculas:
    def __init__(self):
        self.servicio_peliculas = ServicioPeliculas()
        
    def mostrar_menu(self):
        print("=== Catálogo de Películas ===")
        while True:
            try:
                print(f'''
                1. Agregar película
                2. Listar películas
                3. Eliminar archivo de películas
                 4. Salir
                      ''')
                opcion = int(input("Seleccione una opción: "))
                if opcion == 1:
                    nombre_pelicula = input("Ingrese el nombre de la película: ")
                    pelicula = Pelicula(nombre_pelicula)
                    self.servicio_peliculas.agregar_pelicula(pelicula)
                    print("Película agregada al catálogo.")
                elif opcion == 2:
                    self.servicio_peliculas.listar_peliculas()
                elif opcion == 3:
                    self.servicio_peliculas.eliminar_archivo_peliculas()
                elif opcion == 4:
                    print("Saliendo del programa.")
                    break
                else:
                    print("Opción no válida. Por favor, seleccione una opción del menú.")
                
            except ValueError:
                print("Opción no válida. Por favor, ingrese un número.")
            except Exception as e:
                print(f"Ocurrió un error: {e}")


if __name__ == "__main__":
    app = AppCatalogoPeliculas()
    app.mostrar_menu()