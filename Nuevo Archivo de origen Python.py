def cajero_automatico():
    saldo = 1000.0  # Saldo inicial de ejemplo

    while True:
        print("\n--- CAJERO AUTOMÁTICO ---")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = input("Selecciona una opción (1-4): ")

        if opcion == "1":
            print(f"\nTu saldo actual es: ${saldo:.2f}")

        elif opcion == "2":
            try:
                monto = float(input("Ingrese la cantidad a depositar: $"))
                if monto > 0:
                    saldo += monto
                    print(f"Depósito exitoso. Nuevo saldo: ${saldo:.2f}")
                else:
                    print("El monto debe ser mayor a cero.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

        elif opcion == "3":
            try:
                monto = float(input("Ingrese la cantidad a retirar: $"))
                if monto > 0:
                    if monto <= saldo:
                        saldo -= monto
                        print(f"Retiro exitoso. Nuevo saldo: ${saldo:.2f}")
                    else:
                        print("Fondos insuficientes.")
                else:
                    print("El monto debe ser mayor a cero.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

        elif opcion == "4":
            print("\nGracias por usar el cajero automático. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


# Ejecutar el cajero
if __name__ == "__main__":
    cajero_automatico()
