# ==========================================
# SISTEMA PRINCIPAL DE RESERVAS
# ==========================================

# Importamos la clase Cliente desde cliente.py
from cliente import Cliente

# Importamos las clases de servicios desde servicio.py
from servicio import (
    ServicioSala,
    ServicioEquipo,
    ServicioAsesoria
)

# Importamos la clase Reserva y la función de logs
from Reservas import Reserva, registrar_log


# ==========================================
# LISTAS INTERNAS
# ==========================================

# Lista para almacenar los clientes registrados
clientes = []

# Lista para almacenar los servicios creados
servicios = []

# Lista para almacenar las reservas realizadas
reservas = []


# ==========================================
# FUNCIÓN MENÚ
# ==========================================

# Función que muestra el menú principal
def mostrar_menu():

    # Título del sistema
    print("\n========= SOFTWARE FJ =========")

    # Opciones del menú
    print("1. Registrar cliente")
    print("2. Crear servicio")
    print("3. Crear reserva")
    print("4. Ver clientes")
    print("5. Ver reservas")
    print("6. Salir")


# ==========================================
# CICLO PRINCIPAL DEL SISTEMA
# ==========================================

# Ciclo infinito para mantener activo el sistema
while True:

    # Mostramos el menú
    mostrar_menu()

    try:

        # Solicitamos al usuario una opción
        opcion = int(
            input("Seleccione una opción: ")
        )

        # ==================================
        # OPCIÓN 1: REGISTRAR CLIENTE
        # ==================================
        if opcion == 1:

            try:

                # Pedimos datos del cliente
                id_cliente = int(input("ID: "))
                nombre = input("Nombre: ")
                email = input("Email: ")

                # Creamos objeto Cliente
                cliente = Cliente(
                    id_cliente,
                    nombre,
                    email
                )

                # Guardamos cliente en la lista
                clientes.append(cliente)

                # Mensaje de éxito
                print("✅ Cliente registrado")

                # Registramos evento en logs
                registrar_log(
                    "Cliente registrado correctamente"
                )

            except Exception as e:

                # Guardamos error en logs
                registrar_log(
                    f"Error cliente: {str(e)}"
                )

                # Mostramos mensaje al usuario
                print(
                    "❌ Error al registrar cliente"
                )

        # ==================================
        # OPCIÓN 2: CREAR SERVICIO
        # ==================================
        elif opcion == 2:

            # Mostramos tipos de servicio
            print("\n1. Sala")
            print("2. Equipo")
            print("3. Asesoría")

            # Pedimos tipo de servicio
            tipo = int(
                input("Tipo de servicio: ")
            )

            # Pedimos datos generales
            nombre = input("Nombre: ")

            precio = float(
                input("Precio base: ")
            )

            try:

                # Crear servicio sala
                if tipo == 1:

                    capacidad = int(
                        input("Capacidad: ")
                    )

                    servicio = ServicioSala(
                        nombre,
                        precio,
                        capacidad
                    )

                # Crear servicio equipo
                elif tipo == 2:

                    tipo_equipo = input(
                        "Tipo de equipo: "
                    )

                    servicio = ServicioEquipo(
                        nombre,
                        precio,
                        tipo_equipo
                    )

                # Crear servicio asesoría
                elif tipo == 3:

                    especialidad = input(
                        "Especialidad: "
                    )

                    servicio = ServicioAsesoria(
                        nombre,
                        precio,
                        especialidad
                    )

                # Error si el tipo no existe
                else:

                    raise ValueError(
                        "Tipo de servicio inválido"
                    )

                # Guardamos servicio en lista
                servicios.append(servicio)

                # Mensaje de éxito
                print("✅ Servicio creado")

                # Registro en logs
                registrar_log(
                    "Servicio creado correctamente"
                )

            except Exception as e:

                # Registro de error
                registrar_log(
                    f"Error servicio: {str(e)}"
                )

                # Mensaje al usuario
                print(
                    "❌ Error al crear servicio"
                )

        # ==================================
        # OPCIÓN 3: CREAR RESERVA
        # ==================================
        elif opcion == 3:

            try:

                # Validamos que existan clientes
                if not clientes:

                    raise ValueError(
                        "No hay clientes registrados"
                    )

                # Validamos que existan servicios
                if not servicios:

                    raise ValueError(
                        "No hay servicios registrados"
                    )

                # Seleccionamos primer cliente
                cliente = clientes[0]

                # Seleccionamos primer servicio
                servicio = servicios[0]

                # Pedimos fecha
                fecha = input(
                    "Fecha de reserva: "
                )

                # Pedimos duración
                duracion = int(
                    input("Duración: ")
                )

                # Creamos objeto Reserva
                reserva = Reserva(
                    len(reservas) + 1,
                    cliente,
                    servicio,
                    fecha,
                    duracion
                )

                # Confirmamos reserva
                reserva.confirmar()

                # Guardamos reserva
                reservas.append(reserva)

                # Mensaje de éxito
                print(
                    "✅ Reserva creada correctamente"
                )

                # Mostramos información
                print(
                    reserva.mostrar_info()
                )

                # Registro en logs
                registrar_log(
                    "Reserva creada correctamente"
                )

            except Exception as e:

                # Registro de error
                registrar_log(
                    f"Error reserva: {str(e)}"
                )

                # Mensaje al usuario
                print(
                    "❌ Error al crear reserva"
                )

        # ==================================
        # OPCIÓN 4: VER CLIENTES
        # ==================================
        elif opcion == 4:

            # Validamos si hay clientes
            if not clientes:

                print(
                    "No hay clientes registrados"
                )

            else:

                # Recorremos lista de clientes
                for cliente in clientes:

                    # Mostramos información
                    print(
                        cliente.mostrar_info()
                    )

        # ==================================
        # OPCIÓN 5: VER RESERVAS
        # ==================================
        elif opcion == 5:

            # Validamos si hay reservas
            if not reservas:

                print(
                    "No hay reservas registradas"
                )

            else:

                # Recorremos lista de reservas
                for reserva in reservas:

                    # Mostramos información
                    print(
                        reserva.mostrar_info()
                    )

        # ==================================
        # OPCIÓN 6: SALIR
        # ==================================
        elif opcion == 6:

            # Mensaje de salida
            print(
                "Saliendo del sistema..."
            )

            # Registro en logs
            registrar_log(
                "Sistema finalizado"
            )

            # Finalizamos ciclo
            break

        # ==================================
        # OPCIÓN INVÁLIDA
        # ==================================
        else:

            print("❌ Opción inválida")

    # ======================================
    # ERROR GENERAL
    # ======================================
    except ValueError:

        # Error si el usuario ingresa
        # un dato no numérico
        print(
            "❌ Debe ingresar un número válido"
        )

    finally:

        # Mensaje final de operación
        print(
            "\n--- Operación finalizada ---"
        )