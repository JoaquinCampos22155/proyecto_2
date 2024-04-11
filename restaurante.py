# Menú principal antes del inicio de sesión
def main_menu():
    print("Bienvenido al sistema de gestión de restaurante")
    print("Por favor, seleccione una opción:")
    print("1. Iniciar sesión")
    print("2. Salir")
    option = input("Seleccione una opción: ")
    return option

# Menú del chef
def chef_menu():
    while True:
        print("Menú del Chef")
        print("1. Agregar platos")
        print("2. Agregar bebidas")
        print("3. Realizar pedido")
        print("4. Confirmar pedido")
        print("5. Regresar al menú principal")
        option = input("Seleccione una opción: ")
        if option in ["1", "2", "3", "4"]:
            return option
        elif option == "5":
            return None
        else:
            print("Opción no válida.")

# Menú del host
def host_menu():
    while True:
        print("Menú del Host")
        print("1. Asignar cliente")
        print("2. Ver calificación")
        print("3. Modificar área")
        print("4. Capacidad de área")
        print("5. Regresar al menú principal")
        option = input("Seleccione una opción: ")
        if option in ["1", "2", "3", "4"]:
            return option
        elif option == "5":
            return None
        else:
            print("Opción no válida.")

# Menú del mesero
def waiter_menu():
    while True:
        print("Menú del Mesero")
        print("1. Modificar pedido")
        print("2. Cuenta")
        print("3. Ver pedido")
        print("4. Regresar al menú principal")
        option = input("Seleccione una opción: ")
        if option in ["1", "2", "3"]:
            return option
        elif option == "4":
            return None
        else:
            print("Opción no válida.")

# Función principal
def main():
    while True:
        main_option = main_menu()
        
        if main_option == "1":
            # Inicio de sesión
            print("Inicio de sesión")
            username = input("Usuario: ")
            password = input("Contraseña: ")
            
            # Evaluación del primer carácter del usuario para determinar el menú
            if username.startswith('h'):
                while True:
                    host_option = host_menu()
                    if host_option == None:
                        break
                    # Aquí puedes agregar la lógica para cada opción del host
            elif username.startswith('c'):
                while True:
                    chef_option = chef_menu()
                    if chef_option == None:
                        break
                    # Aquí puedes agregar la lógica para cada opción del chef
            elif username.startswith('m'):
                while True:
                    waiter_option = waiter_menu()
                    if waiter_option == None:
                        break
                    # Aquí puedes agregar la lógica para cada opción del mesero
            else:
                print("Usuario no reconocido.")
        
        elif main_option == "2":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

main()
