# Inicialización de variables
nombre_tamagotchi = input("Dale un nombre a tu Tamagotchi: ")
energia = 50
hambre = 50

# Función para mostrar el estado actual del Tamagotchi
def mostrar_estado():
    print(f"\nEstado de {nombre_tamagotchi}:")
    print(f"Energía: {energia}")
    print(f"Hambre: {hambre}")

# Bucle principal
while True:
    print("\nMENU:")
    print("(1) Jugar")
    print("(2) Comer")
    print("(3) Dormir")
    print("(4) Ver estado")
    print("(5) Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        while True:
            print("\nSubmenú de Jugar:")
            print("(1) Jugar a la pelota")
            print("(2) Jugar videojuegos")
            print("(3) Regresar al menú principal")
            
            opcion_jugar = input("Selecciona una opción de Jugar: ")
            
            if opcion_jugar == "1":
                # Jugar a la pelota
                energia -= 20
                hambre += 5
            elif opcion_jugar == "2":
                # Jugar videojuegos
                energia -= 10
                hambre += 10
            elif opcion_jugar == "3":
                # Regresar al menú principal
                break
            else:
                print("Opción no válida. Selecciona una opción válida del submenú de Jugar.")
    elif opcion == "2":
        while True:
            print("\nSubmenú de Comer:")
            print("(1) Comer sopa de verduras que hizo la abuela")
            print("(2) Comer kfc cruji")
            print("(3) Regresar al menú principal")
            
            opcion_comer = input("Selecciona una opción de Comer: ")
            
            if opcion_comer == "1":
                # Comer sopa de verduras que hizo la abuela
                hambre += 30
            elif opcion_comer == "2":
                # Comer kfc cruji
                hambre += 15
            elif opcion_comer == "3":
                # Regresar al menú principal
                break
            else:
                print("Opción no válida. Selecciona una opción válida del submenú de Comer.")
    elif opcion == "3":
        while True:
            print("\nSubmenú de Dormir:")
            print("(1) Dormir en el piso")
            print("(2) Dormir en la cama")
            print("(3) Regresar al menú principal")
            
            opcion_dormir = input("Selecciona una opción de Dormir: ")
            
            if opcion_dormir == "1":
                # Dormir en el piso
                energia += 20
                hambre += 5
            elif opcion_dormir == "2":
                # Dormir en la cama
                energia += 40
                hambre += 10
            elif opcion_dormir == "3":
                # Regresar al menú principal
                break
            else:
                print("Opción no válida. Selecciona una opción válida del submenú de Dormir.")
    elif opcion == "4":
        # Ver estado
        mostrar_estado()
    elif opcion == "5":
        # Salir del juego
        print(f"{nombre_tamagotchi} está tieso.")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida del menú principal.")

    # Verificar si el Tamagotchi ya anda con chabelo 
    if energia <= 0 or hambre <= 0:
        print(f"{nombre_tamagotchi} ya anda con la reina isabel.")
        break

    # Limitar la energía y el hambre a un rango de 0 a 100
    energia = max(0, min(energia, 100))
    hambre = max(0, min(hambre, 100))

# Fin del juego
print("¡Gracias por jugar!")
