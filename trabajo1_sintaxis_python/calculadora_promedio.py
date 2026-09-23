def ingresar_calificaciones():
    nombres = []
    calificaciones = []

    while True:
        nombre = input("Cual es el nombre de la asignatura: ")

        while True:
            try:
                calificacion = float(input(f"Ingrese la calificación para {nombre} (0-10): "))
                if 0 <= calificacion <= 10:
                    break
                else:
                    print("La nota metida no esta en rango. Tiene que estar entre 0 y 10 contando los 2")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número. ")

        nombres.append(nombre)
        calificaciones.append(calificacion)

        continuar = input("¿Desa ingresar otra materia? (s/n): ").lower()
        if continuar not in ["s", "si"]:
            break

    return nombres, calificaciones

def calcular_promedio(calificaciones):
    if not calificaciones:
        return 0
    # suma_total = sum(calificaiones)
    return sum(calificaciones) / len(calificaciones)

def determinar_estado(calificaciones, umbral = 5.0):
    aprobadas = [i for i, cal in enumerate(calificaciones) if cal >= umbral]
    suspensos = [i for i, cal in enumerate(calificaciones) if cal < umbral]
    # for i in range(len(calificaciones)):
    #     cal = calificaciones[i]
    #     if cal >= umbral:
    #         aprobadas.append(cal)
    return aprobadas, suspensos

def encontrar_extremos(calificaiones):
    if not calificaiones:
        return None, None
    
    max_idx = calificaiones.index(max(calificaiones))
    min_idx = calificaiones.index(min(calificaiones))

    return max_idx, min_idx

def main():
    print("--- Calculadora de Promedios ---")
    nombres, calificaciones = ingresar_calificaciones()
    
    if not nombres:
        print("No se añadieron asignaturas")
    else:
        promedio = calcular_promedio(calificaciones)
        aprobadas_idx, suspensas_idx = determinar_estado(calificaciones, 4.3)
        max_idx, min_idx = encontrar_extremos(calificaciones)
        
        print("--- Reumen Final ---")
        for i in range(len(nombres)):
            print(f"{nombres[i]}: {calificaciones[i]}")
            
        print(f"Promeidio general: {promedio:.2f}")
        
        print("Asignaturas aprobadas: ")
        for idx in aprobadas_idx:
            print(f"- {nombres[idx]}")
            
        print("Asignaturas suspensas: ")
        for idx in suspensas_idx:
            print(f"- {nombres[idx]}")
            
        print(f"Mejor calificación: {nombres[max_idx]} con {calificaciones[max_idx]}")
        print(f"Peor calificación: {nombres[min_idx]} con {calificaciones[min_idx]}")
        
    print("Muchas gracias por utilizar la calculadora! Adiós")

if __name__ == "__main__":
    main()