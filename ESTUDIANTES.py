def pedir_entero_positivo(mensaje: str) -> int:
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            print("Ingresa un número mayor que 0.")
        except ValueError:
            print("Entrada inválida. Escribe un número entero.")


def pedir_calificacion(mensaje: str) -> float:
    while True:
        try:
            calif = float(input(mensaje))
            if 0 <= calif <= 100:
                return calif
            print("La calificación debe estar entre 0 y 100.")
        except ValueError:
            print("Entrada inválida. Escribe un número entre 0 y 100.")


def main() -> None:
    num_estudiantes = pedir_entero_positivo("¿Cuántos estudiantes hay en el grupo? ")
    num_materias = pedir_entero_positivo("¿Cuántas materias tiene el grupo? ")

    matriz: list[list[float]] = []

    print("\n--- Captura de calificaciones (0 - 100) ---")
    for i in range(num_estudiantes):
        fila: list[float] = []
        for j in range(num_materias):
            calif = pedir_calificacion(f"Estudiante {i + 1}, Materia {j + 1}: ")
            fila.append(calif)
        matriz.append(fila)

    promedios_estudiantes = [sum(fila) / num_materias for fila in matriz]

    promedios_materias = [
        sum(matriz[i][j] for i in range(num_estudiantes)) / num_estudiantes
        for j in range(num_materias)
    ]

    todas_calificaciones = [calif for fila in matriz for calif in fila]
    calif_maxima = max(todas_calificaciones)
    calif_minima = min(todas_calificaciones)

    print("\n" + "=" * 45)
    print("RESULTADOS DEL GRUPO".center(45))
    print("=" * 45)

    print("\nPromedio por estudiante:")
    for i, prom in enumerate(promedios_estudiantes, start=1):
        print(f"  - Estudiante {i}: {prom:.2f}")

    print("\nPromedio por materia:")
    for j, prom in enumerate(promedios_materias, start=1):
        print(f"  - Materia {j}: {prom:.2f}")

    print("\nExtremos generales:")
    print(f"  - Calificación más alta: {calif_maxima:.2f}")
    print(f"  - Calificación más baja: {calif_minima:.2f}")
    print("=" * 45)


if __name__ == "__main__":
    main()