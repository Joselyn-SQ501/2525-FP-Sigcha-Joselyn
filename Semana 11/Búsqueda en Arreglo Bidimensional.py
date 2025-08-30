
print("\nBúsqueda de un valor en un Arreglo Bidimensional")

# Crear una matriz bidimensional (3x3)
matriz = [
    [10, 20, 30],
    [5,  15, 25],
    [40, 50, 60]
]

# Valor que estamos buscando
valor_buscado = 50

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):         # Recorre filas
        for j in range(len(matriz[i])):  # Recorre columnas
            if matriz[i][j] == valor:
                return (i, j)  # Devuelve la posición una vez que se encuentra el valor
    return None  # Sale del bucle si no encuentra el valor

# Llamamos a la función
posicion = buscar_valor(matriz, valor_buscado)

# Mostrar resultado, verificando si se encontró el valor y su posición
if posicion:
    print(f"\n✅ El valor {valor_buscado} se encontró en la posición: fila {posicion[0]}, columna {posicion[1]}")
else:
    print(f"\n❌ El valor {valor_buscado} no se encontró en la matriz.")

print("\n😺¡Buen día!✨")
