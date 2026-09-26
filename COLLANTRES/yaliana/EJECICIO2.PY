# Variables iniciales
saldo = 1000.0
movimientos = [100, -50, 200, -30]

opcion = 0

while opcion != 5:
    # Menú principal
    print("\n=== SIMULADOR DE CAJERO AUTOMÁTICO ===")
    print("1. Consultar saldo")
    print("2. Depositar")
    print("3. Retirar")
    print("4. Mostrar movimientos")
    print("5. Salir")
    
    opcion = int(input("Selecciona una opción (1-5): "))
    
    if opcion == 1:
        # Consultar saldo
        print(f"\nTu saldo actual es: ${saldo:.2f}")
        
    elif opcion == 2:
        # Depositar dinero
        monto = float(input("\n¿Cuánto dinero deseas depositar?: $"))
        if monto > 0:
            saldo += monto
            movimientos.append(monto)  # Se guarda como valor positivo
            print(f"¡Depósito exitoso! Has ingresado ${monto:.2f}")
        else:
            print("El monto a depositar debe ser mayor a 0.")
            
    elif opcion == 3:
        # Retirar dinero
        monto = float(input("\n¿Cuánto dinero deseas retirar?: $"))
        if monto <= 0:
            print("El monto a retirar debe ser mayor a 0.")
        elif monto > saldo:
            print("Fondos insuficientes. No puedes retirar más de tu saldo disponible.")
        else:
            saldo -= monto
            movimientos.append(-monto)  # Se guarda como valor negativo
            print(f"¡Retiro exitoso! Has retirado ${monto:.2f}")
            
    elif opcion == 4:
        # Mostrar movimientos
        print("\n--- HISTORIAL DE MOVIMIENTOS ---")
        if len(movimientos) == 0:
            print("No hay movimientos registrados.")
        else:
            for i, mov in enumerate(movimientos, 1):
                if mov > 0:
                    print(f"{i}. Depósito: +${mov:.2f}")
                else:
                    print(f"{i}. Retiro: -${abs(mov):.2f}")
                    
    elif opcion == 5:
        # Salir del sistema
        print("\nGracias por usar el cajero automático. ¡Hasta luego!")
        
    else:
        print("\nOpción no válida. Por favor, elige un número del 1 al 5.")