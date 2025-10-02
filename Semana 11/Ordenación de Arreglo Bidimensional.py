
print("\nOrdenación de un Arreglo Bidimensional")

# Crear una matriz bidimensional (3x3)
matriz = [
    [34, 12, 25],
    [9, 50, 18],
    [42, 7, 30]
]

# Función para ordenar una fila de manera ascendente utilizando Bubble Sort
def bubble_sort(fila):
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]  # Intercambiar valores
    return fila

# Función para mostrar la matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

    # Mostrar la matriz original
print("\nMatriz Original:")
mostrar_matriz(matriz)

# Opciones o instrucciones al usuario sobre la fila o filas que el usuario quiere ordenar
print("\n👉 OPCIONES:")
print("   - Digita el número de la fila (0, 1 o 2) para ordenarla.")
print("   - Digita -1 para ordenar todas las filas.")

# Preguntar al usuario qué fila quiere ordenar
opcion = int(input("\n¿Qué fila deseas ordenar? "))

# Ordenar las filas utilizando Bubble Sort según la elección del usuario
if opcion == -1:  # Ordenar todas las filas
    for fila in matriz:
        bubble_sort(fila)
    print("\n✅ Todas las filas fueron ordenadas ascendentemente.")
elif 0 <= opcion < len(matriz):  # Ordenar una fila específica
    bubble_sort(matriz[opcion])
    print(f"\n✅ La fila {opcion} fue ordenada ascendentemente.")
else:
    print("\n⚠️ Opción no válida. No se ordenó ninguna fila de la matriz.")

# Mostrar la matriz ordenada
print("\nMatriz resultante:")
mostrar_matriz(matriz)


print("\n😺¡Buen día!✨")