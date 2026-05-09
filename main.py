# Importamos la clase Cliente desde el archivo cliente.py
from cliente import Cliente

# Importamos las clases de servicios desde servicio.py
from servicio import ServicioSala, ServicioEquipo, ServicioAsesoria

# Importamos la clase Reserva y la función de logs
from reserva import Reserva, registrar_log


# Creamos una lista vacía para almacenar los clientes
clientes = []

# Creamos una lista vacía para almacenar los servicios
servicios = []


# Definimos una función para mostrar el menú
def mostrar_menu():
    # Imprime el título del sistema
    print("\n--- SISTEMA DE RESERVAS ---")

    # Muestra las opciones disponibles
    print("1. Registrar cliente")
    print("2. Crear servicio")
    print("3. Crear reserva")
    print("4. Ver clientes")
    print("5. Salir")


# Iniciamos un ciclo infinito para que el sistema siga funcionando
while True:

    # Llamamos la función para mostrar el menú
    mostrar_menu()

    try:
        # Pedimos al usuario que ingrese una opción y la convertimos a entero
        opcion = int(input("Seleccione una opción: "))

        # ================================
        # OPCIÓN 1: REGISTRAR CLIENTE
        # ================================
        if opcion == 1:
            try:
                # Pedimos los datos del cliente
                id = int(input("ID: "))
                nombre = input("Nombre: ")
                email = input("Email: ")

                # Creamos un objeto Cliente con los datos ingresados
                cliente = Cliente(id, nombre, email)

                # Guardamos el cliente en la lista
                clientes.append(cliente)

                # Mostramos mensaje de éxito
                print("✅ Cliente registrado")

            except Exception as e:
                # Si ocurre un error, lo guardamos en logs
                registrar_log(f"Error cliente: {str(e)}")

                # Mostramos mensaje al usuario
                print("❌ Error al registrar cliente")


        # ================================
        # OPCIÓN 2: CREAR SERVICIO
        # ================================
        elif opcion == 2:

            # Mostramos tipos de servicio
            print("1. Sala")
            print("2. Equipo")
            print("3. Asesoría")

            # Pedimos el tipo de servicio
            tipo = int(input("Tipo de servicio: "))

            # Pedimos datos generales
            nombre = input("Nombre: ")
            precio = float(input("Precio base: "))

            try:
                # Si es sala
                if tipo == 1:
                    capacidad = int(input("Capacidad: "))
                    servicio = ServicioSala(nombre, precio, capacidad)

                # Si es equipo
                elif tipo == 2:
                    tipo_eq = input("Tipo de equipo: ")
                    servicio = ServicioEquipo(nombre, precio, tipo_eq)

                # Si es asesoría
                elif tipo == 3:
                    especialidad = input("Especialidad: ")
                    servicio = ServicioAsesoria(nombre, precio, especialidad)

                # Si el tipo no existe
                else:
                    raise ValueError("Tipo inválido")

                # Guardamos el servicio en la lista
                servicios.append(servicio)

                # Mensaje de éxito
                print("✅ Servicio creado")

            except Exception as e:
                # Guardamos el error en logs
                registrar_log(f"Error servicio: {str(e)}")

                # Mensaje para el usuario
                print("❌ Error al crear servicio")


        # ================================
        # OPCIÓN 3: CREAR RESERVA
        # ================================
        elif opcion == 3:
            try:
                # Verificamos que existan datos
                if not clientes or not servicios:
                    raise ValueError("Debe haber clientes y servicios")

                # Seleccionamos el primer cliente (simplificado)
                cliente = clientes[0]

                # Seleccionamos el primer servicio
                servicio = servicios[0]

                # Pedimos duración
                duracion = int(input("Duración: "))

                # Creamos la reserva
                reserva = Reserva(cliente, servicio, duracion)

                # Procesamos la reserva y mostramos resultado
                print(reserva.procesar())

            except Exception as e:
                # Guardamos error en logs
                registrar_log(f"Error reserva: {str(e)}")

                # Mensaje para el usuario
                print("❌ Error al crear reserva")


        # ================================
        # OPCIÓN 4: VER CLIENTES
        # ================================
        elif opcion == 4:

            # Recorremos la lista de clientes
            for c in clientes:
                # Mostramos la información de cada cliente
                print(c.mostrar_info())


        # ================================
        # OPCIÓN 5: SALIR
        # ================================
        elif opcion == 5:
            # Mensaje de salida
            print("Saliendo del sistema...")

            # Rompe el ciclo infinito
            break


        # Si la opción no existe
        else:
            print("Opción inválida")

    except ValueError:
        # Si el usuario no ingresa un número válido
        print("❌ Debe ingresar un número")