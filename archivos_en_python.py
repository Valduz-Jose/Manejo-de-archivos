# Archivos en python 
# Nos permiten guardar información de manera persistente, es decir, que no se pierde al cerrar el programa.
# Para trabajar con archivos en python, utilizamos la función open() 
# que nos permite abrir un archivo y realizar operaciones sobre él.
# La función open() recibe dos argumentos: el nombre del archivo y el modo de apertura.
# Modos de apertura:
# 'r' : lectura (read)
# 'w' : escritura (write)
# 'a' : agregar (append)

# Creacion de archivo

nombre_archivo = "mi_archivo.txt"
print(f"Creando mi archivo {nombre_archivo}...")

# Abrimos el archivo en modo escritura (write)
archivo = open(nombre_archivo, 'w')
# Escribimos una línea en el archivo
archivo.write("Hola, este es mi primer archivo en python.\n")
archivo.write("Estoy aprendiendo a trabajar con archivos.\n")
# Cerramos el archivo
archivo.close()

print("Archivo creado y escrito correctamente.")


nombre_archivo = "mi_archivo_conWith.txt"
with open(nombre_archivo, 'w') as archivo:#este bloque se encarga de abrir el archivo, 
    # escribir en él y cerrarlo automáticamente al finalizar
    archivo.write("Hola, este es mi primer archivo en python.\n")
    archivo.write("Estoy aprendiendo a trabajar con archivos.\n")

# Otra forma de abrir un archivo (archivo en modo expclusivo)
nombre_archivo = "mi_nuevo_archivo.txt"

try:
    with open(nombre_archivo, 'x') as archivo: #modo exclusivo (x) para evitar sobrescribir un archivo existente
        archivo.write("Este es un nuevo archivo creado en modo exclusivo.\n")
        archivo.write("Si el archivo ya existe, se generará un error.\n")
    print(f"Archivo '{nombre_archivo}' creado correctamente en modo exclusivo.")
except FileExistsError as e:
    print(f"Error: El archivo '{nombre_archivo}' ya existe. No se puede crear un nuevo archivo con el mismo nombre.")
    print(f"Detalle error:")
