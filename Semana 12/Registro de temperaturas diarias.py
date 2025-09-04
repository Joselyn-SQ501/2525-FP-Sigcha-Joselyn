
print("\nRegistro de temperaturas diarias")

# Crear una matriz 3D para almacenar datos de temperaturas

# Primera dimensión: Ciudades (3 ciudades)
ciudades = ["Quito", "Seúl", "París"]

# Segunda dimensión: Días de la semana (7 días)
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Tercera dimensión: Semanas (4 semanas)
num_semanas = 4

# Matriz 3D con temperaturas simuladas: [ciudad][semana][día]
temperaturas = [
    [  # Quito
        [15,16,15,14,17,18,16],  # Semana 1
        [17,18,19,16,15,14,17],  # Semana 2
        [16,17,16,15,18,19,17],  # Semana 3
        [18,19,18,17,16,15,18],  # Semana 4
    ],
    [  # Seúl
        [22,23,21,24,22,23,21],  # Semana 1
        [23,24,22,25,23,24,22],  # Semana 2
        [21,22,23,24,22,21,23],  # Semana 3
        [24,25,23,26,24,25,23],  # Semana 4
    ],
    [  # París
        [12,13,14,12,13,14,12],  # Semana 1
        [13,14,15,13,14,15,13],  # Semana 2
        [14,15,16,14,15,16,14],  # Semana 3
        [15,16,17,15,16,17,15],  # Semana 4
    ]
]

# Calcular la suma total de la temperatura por ciudad
Promedio_ciudad = 0

# Calcular el promedio de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(ciudades):  #Recorre ciudades
    print(f"\nPromedios de temperatura en {ciudad}:")
    for semana in range(4):  #Semanas
        suma = 0
        for dia in range(7): #Días
            suma += temperaturas[i][semana][dia]
        promedio = suma / len(dias)
        # Mostrar promedio de temperatura para cada ciudad por semana
        print(f"Semana {semana + 1}: Promedio {promedio:.2f} °C")

        # Calcular la suma de los promedios semanales por ciudad
        Promedio_ciudad += promedio

    # Calcular el promedio de temperaturas para cada ciudad
    Promedio_generalc = Promedio_ciudad / num_semanas
    # Reiniciar la variable para el nuevo calculo
    Promedio_ciudad = 0
    # Mostrar el promedio de temperatura total para cada ciudad
    print(f"El promedio de temperatura total en la ciudad de {ciudad} es de {Promedio_generalc:.2f} °C")


print("\n😺¡Buen día!✨")