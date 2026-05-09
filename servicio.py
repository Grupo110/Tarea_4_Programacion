# =========================================================
# SISTEMA DE RESERVAS - SOFTWARE FJ
# Autor: JULIO CESAR SALGADO MARIN
# Archivo: servicio.py
# =========================================================

# MODIFICACIONES REALIZADAS:
#
# 1. Se convirtió la clase Servicio en una
#    clase abstracta usando ABC.
#
# 2. Se implementó polimorfismo mediante
#    sobrescritura de métodos.
#
# 3. Se agregaron validaciones robustas
#    para nombre, precio y atributos.
#
# 4. Se implementó encapsulación mediante
#    atributos protegidos y getters.
#
# 5. Se agregó manejo avanzado de excepciones
#    y encadenamiento de errores.
#
# 6. Se registran errores automáticamente
#    en logs.txt.
#
# 7. Se añadieron parámetros opcionales
#    para simular sobrecarga de métodos.
#
# 8. Se implementaron bloques:
#    try, except, else y finally.
#
# =========================================================

import datetime

# Importamos herramientas abstractas
from abc import ABC, abstractmethod


# ==========================================
# EXCEPCIÓN PERSONALIZADA
# ==========================================

class ServicioError(Exception):
    pass


# ==========================================
# CLASE ABSTRACTA SERVICIO
# ==========================================

class Servicio(ABC):

    # Constructor
    def __init__(self, nombre, precio_base):

        try:

            # Validación del nombre
            if not nombre.strip():

                raise ServicioError(
                    "El servicio debe tener nombre"
                )

            # Validación del precio
            if precio_base <= 0:

                raise ServicioError(
                    "El precio debe ser mayor a cero"
                )

            # Encapsulación
            self._nombre = nombre
            self._precio_base = precio_base

        except ServicioError as e:

            # Registro del error
            self.log_error(e)

            # Encadenamiento de excepción
            raise ServicioError(
                "Error al crear el servicio"
            ) from e

    # ======================================
    # MÉTODOS ABSTRACTOS
    # ======================================

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass

    # ======================================
    # GETTERS
    # ======================================

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_base(self):
        return self._precio_base

    # ======================================
    # MÉTODO PARA LOGS
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
                    f"ERROR SERVICIO: "
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
                "al crear log:",
                e
            )


# ==========================================
# SERVICIO SALA
# ==========================================

class ServicioSala(Servicio):

    def __init__(
        self,
        nombre,
        precio_base,
        capacidad
    ):

        # Herencia
        super().__init__(
            nombre,
            precio_base
        )

        try:

            # Validación
            if capacidad <= 0:

                raise ServicioError(
                    "Capacidad inválida"
                )

            self._capacidad = capacidad

        except ServicioError as e:

            self.log_error(e)

            raise ServicioError(
                "Error en ServicioSala"
            ) from e

    # Polimorfismo
    def calcular_costo(
        self,
        horas=1
    ):

        return (
            self._precio_base * horas
        )

    # Descripción
    def descripcion(self):

        return (
            f"Servicio Sala: "
            f"{self._nombre} | "
            f"Capacidad: "
            f"{self._capacidad}"
        )


# ==========================================
# SERVICIO EQUIPO
# ==========================================

class ServicioEquipo(Servicio):

    def __init__(
        self,
        nombre,
        precio_base,
        tipo_equipo
    ):

        super().__init__(
            nombre,
            precio_base
        )

        try:

            if not tipo_equipo.strip():

                raise ServicioError(
                    "Tipo de equipo requerido"
                )

            self._tipo_equipo = tipo_equipo

        except ServicioError as e:

            self.log_error(e)

            raise ServicioError(
                "Error en ServicioEquipo"
            ) from e

    # Polimorfismo
    def calcular_costo(
        self,
        dias=1
    ):

        return (
            self._precio_base * dias
        )

    # Descripción
    def descripcion(self):

        return (
            f"Servicio Equipo: "
            f"{self._nombre} | "
            f"Tipo: "
            f"{self._tipo_equipo}"
        )


# ==========================================
# SERVICIO ASESORÍA
# ==========================================

class ServicioAsesoria(Servicio):

    def __init__(
        self,
        nombre,
        precio_base,
        especialidad
    ):

        super().__init__(
            nombre,
            precio_base
        )

        try:

            if not especialidad.strip():

                raise ServicioError(
                    "Especialidad requerida"
                )

            self._especialidad = especialidad

        except ServicioError as e:

            self.log_error(e)

            raise ServicioError(
                "Error en ServicioAsesoria"
            ) from e

    # Sobrecarga mediante parámetros opcionales
    def calcular_costo(
        self,
        horas=1,
        incluye_material=False
    ):

        costo = (
            self._precio_base * horas
        )

        # Costo adicional
        if incluye_material:

            costo += 50

        return costo

    # Descripción
    def descripcion(self):

        return (
            f"Servicio Asesoría: "
            f"{self._nombre} | "
            f"Especialidad: "
            f"{self._especialidad}"
        )


# ==========================================
# PRUEBAS DEL SISTEMA
# ==========================================

if __name__ == "__main__":

    try:

        # ==================================
        # SERVICIO SALA
        # ==================================

        s1 = ServicioSala(
            "Sala VIP",
            50,
            10
        )

        print(
            "Costo sala:",
            s1.calcular_costo(2)
        )

        print(
            s1.descripcion()
        )

        print()

        # ==================================
        # SERVICIO EQUIPO
        # ==================================

        s2 = ServicioEquipo(
            "Laptop",
            30,
            "Tecnología"
        )

        print(
            "Costo equipo:",
            s2.calcular_costo(3)
        )

        print(
            s2.descripcion()
        )

        print()

        # ==================================
        # SERVICIO ASESORÍA
        # ==================================

        s3 = ServicioAsesoria(
            "Consultoría",
            100,
            "Software"
        )

        print(
            "Costo asesoría:",
            s3.calcular_costo(
                2,
                True
            )
        )

        print(
            s3.descripcion()
        )

        print()

        # ==================================
        # ERROR INTENCIONAL
        # ==================================

        s4 = ServicioSala(
            "Sala Mala",
            -10,
            0
        )

    except ServicioError as e:

        print(
            "Error detectado:",
            e
        )

    else:

        print(
            "Servicios procesados correctamente"
        )

    finally:

        print(
            "Proceso de servicios finalizado"
        )