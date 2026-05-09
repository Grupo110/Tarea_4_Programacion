# =========================================================
# SISTEMA DE RESERVAS - SOFTWARE FJ
# Código revisado y modificado por:
# JULIO CESAR SALGADO MARIN
# Archivo: main.py
# =========================================================

# MODIFICACIONES REALIZADAS:
#
# 1. Se corrigieron las importaciones
#    de cliente.py, servicio.py y Reservas.py.
#
# 2. Se agregaron listas internas para:
#    clientes, servicios y reservas.
#
# 3. Se fortaleció la integración total
#    entre todas las clases del sistema.
#
# 4. Se mejoró la creación de reservas
#    agregando validaciones completas.
#
# 5. Se implementó manejo avanzado
#    de excepciones.
#
# 6. Se agregó registro automático
#    de eventos y errores en logs.txt.
#
# 7. Se implementó contador de operaciones
#    realizadas en el sistema.
#
# 8. Se agregaron mensajes de control
#    y estabilidad del sistema.
#
# 9. Se mejoró la documentación interna
#    y organización general del código.
#
# =========================================================


# ==========================================
# IMPORTACIONES
# ==========================================

# Importamos clase Cliente
from cliente import Cliente

# Importamos clases de servicios
from servicio import (
    ServicioSala,
    ServicioEquipo,
    ServicioAsesoria
)

# Importamos Reserva y logs
from Reservas import (
    Reserva,
    registrar_log
)


# ==========================================
# LISTAS INTERNAS
# ==========================================

# Lista de clientes
clientes = []

# Lista de servicios
servicios = []

# Lista de reservas
reservas = []

# Contador de operaciones
operaciones = 0


# ==========================================
# MENÚ PRINCIPAL
# ==========================================

def mostrar_menu():

    print("\n========= SOFTWARE FJ =========")

    print("1. Registrar cliente")
    print("2. Crear servicio")
    print("3. Crear reserva")
    print("4. Ver clientes")
    print("5. Ver reservas")
    print("6. Salir")


# ==========================================
# CICLO PRINCIPAL
# ==========================================

while True:

    # Mostrar menú
    mostrar_menu()

    try:

        # Solicitar opción
        opcion = int(
            input(
                "Seleccione una opción: "
            )
        )

        # ==================================
        # OPCIÓN 1 - CLIENTES
        # ==================================
        if opcion == 1:

            try:

                # Solicitar datos
                id_cliente = int(
                    input("ID: ")
                )

                nombre = input(
                    "Nombre: "
                )

                email = input(
                    "Email: "
                )

                # Crear objeto cliente
                cliente = Cliente(
                    id_cliente,
                    nombre,
                    email
                )

                # Guardar cliente
                clientes.append(cliente)

                # Incrementar operaciones
                operaciones += 1

                print(
                    "✅ Cliente registrado"
                )

                registrar_log(
                    "Cliente registrado correctamente"
                )

            except Exception as e:

                registrar_log(
                    f"Error cliente: {str(e)}"
                )

                print(
                    "❌ Error al registrar cliente"
                )

        # ==================================
        # OPCIÓN 2 - SERVICIOS
        # ==================================
        elif opcion == 2:

            print("\n1. Sala")
            print("2. Equipo")
            print("3. Asesoría")

            tipo = int(
                input(
                    "Tipo de servicio: "
                )
            )

            nombre = input(
                "Nombre: "
            )

            precio = float(
                input(
                    "Precio base: "
                )
            )

            try:

                # Servicio Sala
                if tipo == 1:

                    capacidad = int(
                        input(
                            "Capacidad: "
                        )
                    )

                    servicio = ServicioSala(
                        nombre,
                        precio,
                        capacidad
                    )

                # Servicio Equipo
                elif tipo == 2:

                    tipo_equipo = input(
                        "Tipo de equipo: "
                    )

                    servicio = ServicioEquipo(
                        nombre,
                        precio,
                        tipo_equipo
                    )

                # Servicio Asesoría
                elif tipo == 3:

                    especialidad = input(
                        "Especialidad: "
                    )

                    servicio = ServicioAsesoria(
                        nombre,
                        precio,
                        especialidad
                    )

                else:

                    raise ValueError(
                        "Tipo inválido"
                    )

                # Guardar servicio
                servicios.append(servicio)

                # Incrementar operaciones
                operaciones += 1

                print(
                    "✅ Servicio creado"
                )

                registrar_log(
                    "Servicio creado correctamente"
                )

            except Exception as e:

                registrar_log(
                    f"Error servicio: {str(e)}"
                )

                print(
                    "❌ Error al crear servicio"
                )

        # ==================================
        # OPCIÓN 3 - RESERVAS
        # ==================================
        elif opcion == 3:

            try:

                # Validar clientes
                if not clientes:

                    raise ValueError(
                        "No hay clientes"
                    )

                # Validar servicios
                if not servicios:

                    raise ValueError(
                        "No hay servicios"
                    )

                # Seleccionar cliente
                cliente = clientes[0]

                # Seleccionar servicio
                servicio = servicios[0]

                # Pedir datos
                fecha = input(
                    "Fecha de reserva: "
                )

                duracion = int(
                    input(
                        "Duración: "
                    )
                )

                # Crear reserva
                reserva = Reserva(
                    len(reservas) + 1,
                    cliente,
                    servicio,
                    fecha,
                    duracion
                )

                # Confirmar reserva
                reserva.confirmar()

                # Guardar reserva
                reservas.append(reserva)

                # Incrementar operaciones
                operaciones += 1

                print(
                    "✅ Reserva creada correctamente"
                )

                print(
                    reserva.mostrar_info()
                )

                registrar_log(
                    "Reserva creada correctamente"
                )

            except Exception as e:

                registrar_log(
                    f"Error reserva: {str(e)}"
                )

                print(
                    "❌ Error al crear reserva"
                )

        # ==================================
        # OPCIÓN 4 - VER CLIENTES
        # ==================================
        elif opcion == 4:

            if not clientes:

                print(
                    "No hay clientes registrados"
                )

            else:

                for cliente in clientes:

                    print(
                        cliente.mostrar_info()
                    )

        # ==================================
        # OPCIÓN 5 - VER RESERVAS
        # ==================================
        elif opcion == 5:

            if not reservas:

                print(
                    "No hay reservas registradas"
                )

            else:

                for reserva in reservas:

                    print(
                        reserva.mostrar_info()
                    )

        # ==================================
        # OPCIÓN 6 - SALIR
        # ==================================
        elif opcion == 6:

            print(
                "Saliendo del sistema..."
            )

            print(
                f"Operaciones realizadas: "
                f"{operaciones}"
            )

            registrar_log(
                "Sistema finalizado"
            )

            break

        # ==================================
        # OPCIÓN INVÁLIDA
        # ==================================
        else:

            print(
                "❌ Opción inválida"
            )

    # ======================================
    # MANEJO GLOBAL DE ERRORES
    # ======================================
    except ValueError as e:

        registrar_log(
            f"Error general: {str(e)}"
        )

        print(
            "❌ Debe ingresar un número válido"
        )

    finally:

        print(
            "\n--- Operación finalizada ---"
        )