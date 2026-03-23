# Lectura de archivos 'r' usando read() readline() y readlines()
print("***Leer Archivo con Python***")

nombre_archivo = "mi_archivo.txt"

#leer un archivo usando readlines
with open(nombre_archivo, 'r') as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea.strip())  # Eliminar el salto de línea al imprimir

#leer usando read
print("\n***Leer Archivo usando read()***")
with open(nombre_archivo, 'r') as archivo:
    contenido = archivo.read()
    print(contenido)