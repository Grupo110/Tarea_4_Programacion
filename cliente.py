# Código realizado por Julio Cesar Salgado Marín
# Archivo: cliente.py
#Correcciones y mejoras realizadas en cliente.py

# 1. Se creó una excepción personalizada llamada ClienteError
# para mejorar el manejo de errores específicos de clientes.

# 2. Se agregó registro de errores en el archivo logs.txt
# usando manejo de archivos y datetime.

# 3. Se implementó el bloque finally
# para garantizar la finalización del proceso.

# 4. Se mejoró el manejo de excepciones con try/except.

# 5. Se agregaron métodos getter y setter
# para fortalecer la encapsulación.

# 6. Se mantuvieron validaciones para nombre y correo electrónico.

# 7. Se mejoró la organización y documentación del código.

import datetime


# Excepción personalizada para clientes
class ClienteError(Exception):
    pass


# Clase Cliente
class Cliente:

    # Constructor
    def __init__(self, id, nombre, email):

        try:

            # Guardamos el id
            self._id = id

            # Validación de nombre
            if not nombre:
                raise ClienteError(
                    "El nombre no puede estar vacío"
                )

            # Validación de email
            if "@" not in email:
                raise ClienteError(
                    "El email no es válido"
                )

            # Guardamos datos
            self._nombre = nombre
            self._email = email

        except ClienteError as e:

            # Registro de errores en logs.txt
            self.log_error(e)

            # Relanzamos excepción
            raise

    # Método para mostrar información
    def mostrar_info(self):

        return (
            f"Cliente: {self._nombre}, "
            f"Email: {self._email}"
        )

    # Getter para nombre
    @property
    def nombre(self):
        return self._nombre

    # Setter para nombre
    @nombre.setter
    def nombre(self, nuevo_nombre):

        if not nuevo_nombre:
            raise ClienteError(
                "El nombre no puede estar vacío"
            )

        self._nombre = nuevo_nombre

    # Método estático para registrar errores
    @staticmethod
    def log_error(error):

        with open("logs.txt", "a") as f:

            f.write(
                f"[{datetime.datetime.now()}] "
                f"ERROR CLIENTE: {str(error)}\n"
            )


# =========================================
# PRUEBA DEL ARCHIVO
# =========================================
if __name__ == "__main__":

    try:

        # Cliente válido
        c1 = Cliente(
            1,
            "Julio",
            "julio@gmail.com"
        )

        print(c1.mostrar_info())

        # Cliente inválido
        c2 = Cliente(
            2,
            "",
            "correo.com"
        )

    except ClienteError as e:

        print("Error:", e)

    else:

        print("Clientes procesados correctamente")

    finally:

        print("Proceso de clientes finalizado")