
print("\n📝Trabajo con Archivos de Texto📝")
# ---------------------------------------------------------------
# Este código crea un archivo de texto y escribe notas personales,
# Luego lee el archivo línea por línea y muestra su contenido.
# ---------------------------------------------------------------

# ----- ESCRITURA DEL ARCHIVO -----

# Definimos el nombre del archivo
file_name = "my_notes.txt"

# Abrimos o creamos el archivo "my_notes.txt" en modo escritura ('w') con UTF-8
# Se creará el archivo si no existe o sobrescribirá su contenido si ya existía.
archivo = open(file_name, "w", encoding="utf-8")

# Escribimos las líneas de notas personales en el archivo
archivo.write("¡Hola!\n")
archivo.write("📝Aquí se encuentran algunas de mis notas personales.\n")
archivo.write("Nota 1: Recordar estudiar Python todos los días.👩‍💻\n")
archivo.write("Nota 2: Comprar las croquetas y juguetes para los gatos.😺\n")
archivo.write("Nota 3: Revisar la plataforma EVA y finalizar las tareas pendientes.📌\n")

# Cerramos el archivo después de escribir
archivo.close()

# ----- LECTURA DEL ARCHIVO -----
# Abrimos el archivo en modo lectura ('r') con UTF-8
archivo = open(file_name, "r", encoding="utf-8")

# Leemos y mostramos cada línea del archivo utilizando readline()
print("\nContenido línea por línea usando readline():\n")
linea = archivo.readline()  # Leemos la primera línea
while linea != "":           # Mientras no lleguemos al final del archivo
    print(linea.strip())     # Mostramos la línea sin el salto de línea adicional
    linea = archivo.readline()  # Leemos la siguiente línea del archivo

# Cerramos el archivo después de leer
archivo.close()

print("\n😺¡Buen día!✨")