#yuliana cometa
import datetime   # Importamos datetime para registrar fecha y hora en el log

# Creamos una excepción personalizada para manejar errores de reservas
class ReservaError(Exception):
    pass

# Definimos la clase Reserva
class Reserva:
    def __init__(self, id_reserva, cliente, servicio, fecha, duracion_horas):
        try:
            # Validamos que el cliente sea un objeto de la clase Cliente
            if not isinstance(cliente, Cliente):
                raise ReservaError("Cliente inválido")
            
            # Validamos que el servicio sea un objeto de la clase Servicio
            if not isinstance(servicio, Servicio):
                raise ReservaError("Servicio inválido")
            
            # Validamos que la duración sea positiva
            if duracion_horas <= 0:
                raise ReservaError("La duración debe ser positiva")

            # Guardamos los atributos como protegidos (con _)
            self._id_reserva = id_reserva
            self._cliente = cliente
            self._servicio = servicio
            self._fecha = fecha
            self._duracion_horas = duracion_horas
            self._estado = "pendiente"   # Estado inicial de la reserva

        except ReservaError as e:
            # Si ocurre un error, lo registramos en el archivo logs.txt
            self.log_error(e)
            # Volvemos a lanzar la excepción para que el programa la capture
            raise

    # Método para confirmar la reserva
    def confirmar(self):
        try:
            # Solo se puede confirmar si está pendiente
            if self._estado != "pendiente":
                raise ReservaError("Solo se pueden confirmar reservas pendientes")
            self._estado = "confirmada"
        except ReservaError as e:
            self.log_error(e)
            raise

    # Método para cancelar la reserva
    def cancelar(self):
        try:
            # Si ya está cancelada, no se puede volver a cancelar
            if self._estado == "cancelada":
                raise ReservaError("La reserva ya está cancelada")
            self._estado = "cancelada"
        except ReservaError as e:
            self.log_error(e)
            raise

    # Método para mostrar información de la reserva
    def mostrar_info(self):
        return (f"Reserva {self._id_reserva} - Cliente: {self._cliente.mostrar_info()}, "
                f"Servicio: {self._servicio._nombre}, Fecha: {self._fecha}, "
                f"Duración: {self._duracion_horas}h, Estado: {self._estado}")

    # Método estático para registrar errores en un archivo
    @staticmethod
    def log_error(error):
        with open("logs.txt", "a") as f:
            f.write(f"[{datetime.datetime.now()}] ERROR: {str(error)}\n")
