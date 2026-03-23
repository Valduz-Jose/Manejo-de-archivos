print("Anexar info al archivo")

nombre_archivo = "mi_archivo.txt"

with open(nombre_archivo, 'a') as archivo:
    archivo.write("Esta es una nueva línea añadida al archivo.\n")
    archivo.write("Otra línea más para el archivo.\n")
print(f"Información anexada al archivo {nombre_archivo} exitosamente.")

