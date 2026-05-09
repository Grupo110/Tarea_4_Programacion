# Código original realizado por la compañera Yuliana Cometa
# Código revisado y modificado por Julio Cesar Salgado Marín

import datetime

# Importación de clases necesarias
from cliente import Cliente
from servicio import Servicio


# Excepción personalizada para manejar errores de reservas
class ReservaError(Exception):
    pass


# Clase Reserva
class Reserva:

    def __init__(self, id_reserva, cliente, servicio, fecha, duracion_horas):

        try:

            # Verificación:
            # el cliente debe ser una instancia válida de Cliente
            if not isinstance(cliente, Cliente):
                raise ReservaError("Cliente inválido")

            # Verificación:
            # el servicio debe ser una instancia válida de Servicio
            if not isinstance(servicio, Servicio):
                raise ReservaError("Servicio inválido")

            # Mejora realizada:
            # validar que la fecha no esté vacía
            if fecha == "":
                raise ReservaError("La fecha no puede estar vacía")

            # Mejora realizada:
            # validar que la duración sea positiva
            if duracion_horas <= 0:
                raise ReservaError("La duración debe ser mayor a cero")

            # Asignación de atributos protegidos
            self._id_reserva = id_reserva
            self._cliente = cliente
            self._servicio = servicio
            self._fecha = fecha
            self._duracion_horas = duracion_horas

            # Estado inicial de la reserva
            self._estado = "pendiente"

        except ReservaError as e:

            # Registro del error en archivo log
            self.log_error(e)

            # Relanzar excepción
            raise

    # Método para confirmar reserva
    def confirmar(self):

        try:

            # Solo se pueden confirmar reservas pendientes
            if self._estado != "pendiente":
                raise ReservaError(
                    "Solo se pueden confirmar reservas pendientes"
                )

            self._estado = "confirmada"

        except ReservaError as e:
            self.log_error(e)
            raise

    # Método para cancelar reserva
    def cancelar(self):

        try:

            # Evitar cancelar una reserva ya cancelada
            if self._estado == "cancelada":
                raise ReservaError("La reserva ya está cancelada")

            self._estado = "cancelada"

        except ReservaError as e:
            self.log_error(e)
            raise

    # Método para mostrar información de la reserva
    def mostrar_info(self):

        # Observación:
        # verificar que Cliente tenga implementado mostrar_info()

        return (
            f"Reserva {self._id_reserva} - "
            f"Cliente: {self._cliente.mostrar_info()}, "
            f"Servicio: {self._servicio._nombre}, "
            f"Fecha: {self._fecha}, "
            f"Duración: {self._duracion_horas}h, "
            f"Estado: {self._estado}"
        )

    # Método estático para registrar errores
    @staticmethod
    def log_error(error):

        # Los errores se almacenan en logs.txt
        with open("logs.txt", "a") as f:
            f.write(
                f"[{datetime.datetime.now()}] ERROR: {str(error)}\n"
            )