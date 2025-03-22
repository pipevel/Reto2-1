# 📌 Diccionario para almacenar los vehículos
vehiculos = {}

# 📌 Función para registrar un vehículo
def registrar_vehiculo():
    while True:  # Bucle WHILE para repetir en caso de error
        try:
            id_vehiculo = int(input("🔹 Ingrese el ID del vehículo: "))
            if id_vehiculo in vehiculos:
                print("⚠️ Error: Este vehículo ya está registrado.")
                continue  # Repetir si el ID ya existe

            tipo_vehiculo = input("🔹 Ingrese el tipo de vehículo (camión/autobús/coche): ").strip().lower()
            kilometraje_inicial = float(input("🔹 Ingrese el kilometraje inicial: "))

            # Guardamos los datos en el diccionario
            vehiculos[id_vehiculo] = {
                "tipo_vehiculo": tipo_vehiculo,
                "kilometraje_inicial": kilometraje_inicial,
                "kilometraje_final": kilometraje_inicial,  # Se inicia igual al inicial
                "kilometros_recorridos": 0,
                "consumo_combustible": 0,
                "costo_mantenimiento": 0
            }
            print(f"✅ Vehículo {id_vehiculo} registrado exitosamente.")
            break  # Sale del bucle si todo es correcto
        except ValueError:
            print("⚠️ Error: Ingrese un número válido.")

# 📌 Función para registrar el kilometraje final
def registrar_kilometraje():
    while True:  # Bucle WHILE para validar la entrada
        try:
            id_vehiculo = int(input("🔹 Ingrese el ID del vehículo: "))
            if id_vehiculo not in vehiculos:
                print("⚠️ Error: Vehículo no encontrado.")
                continue

            kilometraje_final = float(input("🔹 Ingrese el kilometraje final: "))

            if kilometraje_final < vehiculos[id_vehiculo]["kilometraje_inicial"]:
                print("⚠️ Error: El kilometraje final no puede ser menor al inicial.")
                continue

            # Actualizar datos del vehículo
            vehiculos[id_vehiculo]["kilometraje_final"] = kilometraje_final
            vehiculos[id_vehiculo]["kilometros_recorridos"] = (
                kilometraje_final - vehiculos[id_vehiculo]["kilometraje_inicial"]
            )
            print(f"✅ Kilometraje actualizado para el vehículo {id_vehiculo}.")
            break
        except ValueError:
            print("⚠️ Error: Ingrese un número válido.")

# 📌 Función para registrar consumo de combustible
def registrar_consumo():
    while True:
        try:
            id_vehiculo = int(input("🔹 Ingrese el ID del vehículo: "))
            if id_vehiculo not in vehiculos:
                print("⚠️ Error: Vehículo no encontrado.")
                continue

            consumo = float(input("🔹 Ingrese el consumo de combustible en litros: "))
            vehiculos[id_vehiculo]["consumo_combustible"] = consumo
            print(f"✅ Consumo registrado para el vehículo {id_vehiculo}.")
            break
        except ValueError:
            print("⚠️ Error: Ingrese un número válido.")

# 📌 Función para calcular eficiencia (km/l)
def calcular_eficiencia():
    for id_vehiculo, datos in vehiculos.items():
        consumo = datos["consumo_combustible"]
        km_recorridos = datos["kilometros_recorridos"]

        if consumo > 0:
            eficiencia = km_recorridos / consumo
        else:
            eficiencia = 0  # Evitar división por cero

        print(f"🚗 Vehículo {id_vehiculo} - Eficiencia: {eficiencia:.2f} km/l")

# 📌 Función para generar un reporte de todos los vehículos
def generar_reporte():
    print("\n📊 REPORTE DE VEHÍCULOS 📊")
    for id_vehiculo, datos in vehiculos.items():
        print(f"\n🚗 Vehículo {id_vehiculo} ({datos['tipo_vehiculo']})")
        print(f"  🔹 Kilómetros recorridos: {datos['kilometros_recorridos']} km")
        print(f"  🔹 Consumo de combustible: {datos['consumo_combustible']} litros")
        print(f"  🔹 Costo de mantenimiento: ${datos['costo_mantenimiento']}")

# 📌 Función para optimizar rutas según tipo de vehículo
def optimizar_rutas():
    tipo = input("🔹 Ingrese el tipo de vehículo para optimizar rutas (camión/autobús/coche): ").strip().lower()
    total_km = 0
    contador = 0

    for id_vehiculo, datos in vehiculos.items():
        if datos["tipo_vehiculo"] == tipo:
            total_km += datos["kilometros_recorridos"]
            contador += 1

    if contador > 0:
        promedio_km = total_km / contador
        print(f"\n📍 Optimización de rutas para {tipo.upper()} 📍")
        print(f"  🔹 Kilómetros promedio recorridos: {promedio_km:.2f} km")
    else:
        print("⚠️ No hay vehículos de este tipo registrados.")

# 📌 Menú interactivo con WHILE
while True:
    print("\n🔹 MENU PRINCIPAL 🔹")
    print("1️⃣ Registrar un vehículo")
    print("2️⃣ Registrar kilometraje final")
    print("3️⃣ Registrar consumo de combustible")
    print("4️⃣ Calcular eficiencia de combustible")
    print("5️⃣ Generar reporte")
    print("6️⃣ Optimizar rutas")
    print("7️⃣ Salir")

    opcion = input("🔹 Seleccione una opción: ")

    if opcion == "1":
        registrar_vehiculo()
    elif opcion == "2":
        registrar_kilometraje()
    elif opcion == "3":
        registrar_consumo()
    elif opcion == "4":
        calcular_eficiencia()
    elif opcion == "5":
        generar_reporte()
    elif opcion == "6":
        optimizar_rutas()
    elif opcion == "7":
        print("👋 Saliendo del sistema. ¡Hasta luego!")
        break  # Sale del bucle y finaliza el programa
    else:
        print("⚠️ Opción no válida. Intente de nuevo.")