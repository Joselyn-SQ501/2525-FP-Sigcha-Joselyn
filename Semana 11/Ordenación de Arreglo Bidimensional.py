
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

# Ordenar cada fila de la matriz utilizando Bubble Sort
for fila in matriz:
    bubble_sort(fila)

# Mostrar la matriz ordenada
print("\nMatriz con las filas ordenadas ascendentemente:")
mostrar_matriz(matriz)


print("\n😺¡Buen día!✨")