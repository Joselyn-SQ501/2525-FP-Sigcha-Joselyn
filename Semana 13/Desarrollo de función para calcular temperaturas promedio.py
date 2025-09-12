
#Descripción:
#Este programa define una función en Python que calcula los promedios de temperatura
#semanal y general para varias ciudades durante cuatro semanas.
#Los datos se almacenan en una matriz 3D: [ciudad][semana][día].

print("\nCalcular el promedio de temperaturas en ciudades")

#Función para calcular promedios
def calcular_promedios(ciudades, dias, num_semanas, temperaturas):
    temperaturas_promedio = {}
    for i, ciudad in enumerate(ciudades):  # Recorre ciudades
        print(f"\nPromedios de temperatura en {ciudad}:")
        suma_ciudad = 0  # acumulador del promedio de la ciudad

        for semana in range(num_semanas):  # Recorre semanas
            suma_semana = 0 # acumulador de temperaturas de una sola semana

            for dia in range(len(dias)):  # Recorre días
                suma_semana += temperaturas[i][semana][dia]

            # Promedio semanal
            promedio_semana = suma_semana / len(dias)

            # Mostrar promedio de temperatura para cada ciudad por semana
            print(f"Semana {semana + 1}: Promedio {promedio_semana:.2f} °C")

            # Calcular la suma de los promedios semanales por ciudad
            suma_ciudad += promedio_semana  # acumula el promedio semanal

        # Promedio total de la ciudad
        promedio_general = suma_ciudad / num_semanas

        # Guarda el promedio en el diccionario con 2 decimales
        temperaturas_promedio[ciudad] = round(promedio_general, 2)

    # Devuelve los promedios finales de cada ciudad
    return temperaturas_promedio

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

# Llamada a la función principal
promedios_finales = calcular_promedios(ciudades, dias, num_semanas, temperaturas)

# Mostrar resumen de resultados
print("\n📌 Resumen de promedios generales por ciudad:")
for ciudad, promedio in promedios_finales.items():
    # Se muestran los promedios generales de cada ciudad
    print(f"El promedio de temperatura en {ciudad}: {promedio} °C")

print("\n😺¡Buen día!✨")