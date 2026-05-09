# =========================================================
# SISTEMA DE RESERVAS - SOFTWARE FJ
# Autor: JUAN DAVID CARVAJAL FRANCO
# Revisado por: JULIO CESAR SALGADO MARIN
# =========================================================

# MODIFICACIONES REALIZADAS:
#
# 1. Se agregó herencia desde la clase abstracta Entidad.
#
# 2. Se implementó el método descripcion()
#    exigido por la clase abstracta.
#
# 3. Se mejoraron las validaciones del ID,
#    nombre y correo electrónico.
#
# 4. Se implementó encapsulación usando
#    atributos privados.
#
# 5. Se mejoró el manejo de excepciones
#    con encadenamiento de errores.
#
# 6. Se mantuvo el registro automático
#    de errores en logs.txt.
#
# 7. Se añadieron comentarios y documentación
#    para mejorar la comprensión del código.
#
# =========================================================

import datetime

from entidad import Entidad


# =========================================
# EXCEPCIÓN PERSONALIZADA
# =========================================
class ClienteError(Exception):
    pass


# =========================================
# CLASE CLIENTE
# =========================================
class Cliente(Entidad):

    # Constructor
    def __init__(self, id, nombre, email):

        try:

            # Llamamos constructor de Entidad
            super().__init__(id)

            # Validación de nombre
            if not nombre.strip():
                raise ClienteError(
                    "El nombre no puede estar vacío"
                )

            # Validación de email
            if "@" not in email or "." not in email:
                raise ClienteError(
                    "El email no es válido"
                )

            # Encapsulación de atributos
            self._nombre = nombre
            self._email = email

        except Exception as e:

            # Registro del error
            self.log_error(e)

            # Encadenamiento de excepción
            raise ClienteError(
                "Error al crear el cliente"
            ) from e

    # =========================================
    # MÉTODO ABSTRACTO IMPLEMENTADO
    # =========================================
    def descripcion(self):

        return (
            f"Cliente ID: {self.id} - "
            f"Nombre: {self._nombre}"
        )

    # =========================================
    # MÉTODO PARA MOSTRAR INFORMACIÓN
    # =========================================
    def mostrar_info(self):

        return (
            f"Cliente: {self._nombre}, "
            f"Email: {self._email}"
        )

    # =========================================
    # GETTERS Y SETTERS
    # =========================================
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):

        if not nuevo_nombre.strip():
            raise ClienteError(
                "El nombre no puede estar vacío"
            )

        self._nombre = nuevo_nombre

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, nuevo_email):

        if "@" not in nuevo_email:
            raise ClienteError(
                "Correo inválido"
            )

        self._email = nuevo_email

    # =========================================
    # MÉTODO ESTÁTICO PARA LOGS
    # =========================================
    @staticmethod
    def log_error(error):

        with open("logs.txt", "a") as f:

            f.write(
                f"[{datetime.datetime.now()}] "
                f"ERROR CLIENTE: {str(error)}\n"
            )


# =========================================
# PRUEBAS DEL SISTEMA
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
        print(c1.descripcion())

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