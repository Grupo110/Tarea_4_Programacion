# =========================================================
# SISTEMA DE RESERVAS - SOFTWARE FJ
# Código original realizado por Yuliana Cometa
# Revisado y modificado por: JULIO CESAR SALGADO MARIN
# Archivo: Reservas.py
# =========================================================

# MODIFICACIONES REALIZADAS:
#
# 1. Se corrigieron las importaciones
#    de Cliente y Servicio.
#
# 2. Se agregó manejo de logs utilizando
#    datetime y archivos.
#
# 3. Se fortalecieron las validaciones
#    de fecha y duración.
#
# 4. Se implementó manejo avanzado
#    de excepciones.
#
# 5. Se agregó encadenamiento de
#    excepciones usando "from e".
#
# 6. Se mejoró el método mostrar_info()
#    aplicando polimorfismo.
#
# 7. Se agregó el método procesar_reserva().
#
# 8. Se mejoró la integración con:
#    cliente.py, servicio.py y main.py.
#
# 9. Se añadieron comentarios y mejor
#    organización del código.
#
# =========================================================


# ==========================================
# IMPORTACIONES
# ==========================================

import datetime

from cliente import Cliente
from servicio import Servicio


# ==========================================
# EXCEPCIÓN PERSONALIZADA
# ==========================================

class ReservaError(Exception):
    pass


# ==========================================
# CLASE RESERVA
# ==========================================

class Reserva:

    # Constructor
    def __init__(
        self,
        id_reserva,
        cliente,
        servicio,
        fecha,
        duracion_horas
    ):

        try:

            # Validar cliente
            if not isinstance(
                cliente,
                Cliente
            ):

                raise ReservaError(
                    "Cliente inválido"
                )

            # Validar servicio
            if not isinstance(
                servicio,
                Servicio
            ):

                raise ReservaError(
                    "Servicio inválido"
                )

            # Validar fecha
            if not fecha.strip():

                raise ReservaError(
                    "La fecha no puede estar vacía"
                )

            # Validar duración
            if duracion_horas <= 0:

                raise ReservaError(
                    "La duración debe ser mayor a cero"
                )

            # Encapsulación
            self._id_reserva = id_reserva
            self._cliente = cliente
            self._servicio = servicio
            self._fecha = fecha
            self._duracion_horas = duracion_horas

            # Estado inicial
            self._estado = "pendiente"

        except ReservaError as e:

            # Registro del error
            self.log_error(e)

            # Encadenamiento
            raise ReservaError(
                "Error al crear la reserva"
            ) from e

    # ======================================
    # CONFIRMAR RESERVA
    # ======================================

    def confirmar(self):

        try:

            # Verificar estado
            if self._estado != "pendiente":

                raise ReservaError(
                    "Solo se pueden confirmar reservas pendientes"
                )

            self._estado = "confirmada"

        except ReservaError as e:

            self.log_error(e)

            raise ReservaError(
                "Error al confirmar reserva"
            ) from e

    # ======================================
    # CANCELAR RESERVA
    # ======================================

    def cancelar(self):

        try:

            # Validar cancelación
            if self._estado == "cancelada":

                raise ReservaError(
                    "La reserva ya está cancelada"
                )

            self._estado = "cancelada"

        except ReservaError as e:

            self.log_error(e)

            raise ReservaError(
                "Error al cancelar reserva"
            ) from e

    # ======================================
    # PROCESAR RESERVA
    # ======================================

    def procesar_reserva(self):

        try:

            if self._estado == "cancelada":

                raise ReservaError(
                    "No se puede procesar una reserva cancelada"
                )

            return (
                f"Procesando reserva "
                f"{self._id_reserva}"
            )

        except ReservaError as e:

            self.log_error(e)

            raise ReservaError(
                "Error al procesar reserva"
            ) from e

    # ======================================
    # MOSTRAR INFORMACIÓN
    # ======================================

    def mostrar_info(self):

        return (

            f"Reserva {self._id_reserva} | "

            f"Cliente: "
            f"{self._cliente.mostrar_info()} | "

            f"Servicio: "
            f"{self._servicio.descripcion()} | "

            f"Fecha: "
            f"{self._fecha} | "

            f"Duración: "
            f"{self._duracion_horas}h | "

            f"Estado: "
            f"{self._estado}"
        )

    # ======================================
    # REGISTRO DE ERRORES
    # ======================================

    @staticmethod
    def log_error(error):

        try:

            with open(
                "logs.txt",
                "a",
                encoding="utf-8"
            ) as f:

                f.write(
                    f"[{datetime.datetime.now()}] "
                    f"ERROR RESERVA: "
                    f"{str(error)}\n"
                )

        except PermissionError:

            print(
                "No se pudo escribir "
                "en logs.txt"
            )

        except Exception as e:

            print(
                "Error inesperado "
                "al registrar log:",
                e
            )


# ==========================================
# FUNCIÓN PARA REGISTRAR EVENTOS
# ==========================================

def registrar_log(mensaje):

    try:

        with open(
            "logs.txt",
            "a",
            encoding="utf-8"
        ) as f:

            f.write(
                f"[{datetime.datetime.now()}] "
                f"{mensaje}\n"
            )

    except Exception as e:

        print(
            "Error registrando evento:",
            e
        )