# Código original realizado por la compañera Yuliana Cometa
# Código revisado y modificado por Julio Cesar Salgado Marín

# Comentarios de revisión y mejoras realizadas:
#
# 1. Se corrigieron las importaciones de Cliente y Servicio.
#
# 2. Se agregó la importación de datetime
# para el registro de logs.
#
# 3. Se agregó validación para fecha vacía.
#
# 4. Se mejoró la validación de duración
# de la reserva.
#
# 5. Se verificó el manejo de excepciones
# personalizadas mediante ReservaError.
#
# 6. Se mejoró el método mostrar_info()
# utilizando descripcion() para aplicar
# mejor polimorfismo.
#
# 7. Se agregó la función registrar_log()
# para registrar eventos del sistema.
#
# 8. Se fortaleció la integración con
# cliente.py, servicio.py y main.py.
#
# 9. Se mejoraron los comentarios y la
# documentación interna del código.
#
# 10. Se mantuvo el registro de errores
# en logs.txt.
# ==========================================
# IMPORTACIONES
# ==========================================

# Importamos datetime para logs
import datetime

# Importamos clases necesarias
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
            if not isinstance(cliente, Cliente):
                raise ReservaError(
                    "Cliente inválido"
                )

            # Validar servicio
            if not isinstance(servicio, Servicio):
                raise ReservaError(
                    "Servicio inválido"
                )

            # Validar fecha
            if fecha == "":
                raise ReservaError(
                    "La fecha no puede estar vacía"
                )

            # Validar duración
            if duracion_horas <= 0:
                raise ReservaError(
                    "La duración debe ser mayor a cero"
                )

            # Atributos protegidos
            self._id_reserva = id_reserva
            self._cliente = cliente
            self._servicio = servicio
            self._fecha = fecha
            self._duracion_horas = duracion_horas

            # Estado inicial
            self._estado = "pendiente"

        except ReservaError as e:

            # Guardar error en logs
            self.log_error(e)

            raise

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

            raise

    # ======================================
    # CANCELAR RESERVA
    # ======================================

    def cancelar(self):

        try:

            # Verificar cancelación
            if self._estado == "cancelada":

                raise ReservaError(
                    "La reserva ya está cancelada"
                )

            self._estado = "cancelada"

        except ReservaError as e:

            self.log_error(e)

            raise

    # ======================================
    # MOSTRAR INFORMACIÓN
    # ======================================

    def mostrar_info(self):

        return (
            f"Reserva {self._id_reserva} - "
            f"Cliente: {self._cliente.mostrar_info()}, "
            f"Servicio: {self._servicio.descripcion()}, "
            f"Fecha: {self._fecha}, "
            f"Duración: {self._duracion_horas}h, "
            f"Estado: {self._estado}"
        )

    # ======================================
    # LOGS DE ERRORES
    # ======================================

    @staticmethod
    def log_error(error):

        with open("logs.txt", "a") as f:

            f.write(
                f"[{datetime.datetime.now()}] "
                f"ERROR: {str(error)}\n"
            )


# ==========================================
# FUNCIÓN PARA REGISTRAR LOGS
# ==========================================

def registrar_log(mensaje):

    with open("logs.txt", "a") as f:

        f.write(
            f"[{datetime.datetime.now()}] "
            f"{mensaje}\n"
        )