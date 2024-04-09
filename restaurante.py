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
    print("Menú del Chef")
    print("1. Agregar platos")
    print("2. Agregar bebidas")
    print("3. Realizar pedido")
    print("4. Confirmar pedido")
    option = input("Seleccione una opción: ")
    return option

# Menú del host
def host_menu():
    print("Menú del Host")
    print("1. Asignar cliente")
    print("2. Ver calificación")
    print("3. Modificar área")
    print("4. Capacidad de área")
    option = input("Seleccione una opción: ")
    return option

# Menú del mesero
def waiter_menu():
    print("Menú del Mesero")
    print("1. Modificar pedido")
    print("2. Cuenta")
    print("3. Ver pedido")
    option = input("Seleccione una opción: ")
    return option

# Función principal
def main():
    while True:
        main_option = main_menu()
        
        if main_option == "1":
            # Inicio de sesión
            print("Inicio de sesión")
            username = input("Usuario: ")
            password = input("Contraseña: ")
            # Aquí puedes agregar la lógica de inicio de sesión, como verificar credenciales en la base de datos
            # Después de verificar las credenciales, puedes determinar el rol del usuario y mostrar el menú correspondiente
            
            # Ejemplo de menú del chef
            while True:
                chef_option = chef_menu()
                # Aquí puedes agregar la lógica para cada opción del chef
                if chef_option == "1":
                    pass
                elif chef_option == "2":
                    pass
                elif chef_option == "3":
                    pass
                elif chef_option == "4":
                    pass
                else:
                    print("Opción no válida.")
        
        elif main_option == "2":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

main()