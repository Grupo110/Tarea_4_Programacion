# Código revisado y mejorado por Julio Cesar Salgado Marín
# Archivo: servicio.py
# Correcciones y mejoras realizadas en servicio.py

# 1. Se convirtió la clase Servicio en una clase abstracta
# utilizando ABC y abstractmethod.

# 2. Se creó la excepción personalizada ServicioError
# para mejorar el manejo de errores específicos.

# 3. Se agregaron registros de errores en logs.txt
# usando manejo de archivos y datetime.

# 4. Se implementó polimorfismo mediante la sobrescritura
# del método calcular_costo() en las clases hijas.

# 5. Se implementó el método descripcion()
# en cada servicio especializado.

# 6. Se validaron datos como:
# nombre, precio, capacidad y especialidad.

# 7. Se agregó sobrecarga de métodos mediante
# parámetros opcionales en calcular_costo().

# 8. Se implementaron bloques:
# try, except, else y finally.

# 9. Se mejoró la documentación y organización del código.

# 10. Se verificó el correcto funcionamiento de:
# ServicioSala, ServicioEquipo y ServicioAsesoria.

import datetime

# Importamos herramientas para clases abstractas
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
            if not nombre:
                raise ServicioError(
                    "El servicio debe tener nombre"
                )

            # Validación del precio
            if precio_base <= 0:
                raise ServicioError(
                    "El precio debe ser mayor a cero"
                )

            # Atributos protegidos
            self._nombre = nombre
            self._precio_base = precio_base

        except ServicioError as e:

            # Registro de error
            self.log_error(e)

            raise

    # Método abstracto obligatorio
    @abstractmethod
    def calcular_costo(self):
        pass

    # Método abstracto obligatorio
    @abstractmethod
    def descripcion(self):
        pass

    # Método estático para registrar errores
    @staticmethod
    def log_error(error):

        try:

            # Abrir archivo en modo agregar
            with open(
                "logs.txt",
                "a",
                encoding="utf-8"
            ) as f:

                # Escribir mensaje de error
                f.write(
                    f"[{datetime.datetime.now()}] "
                    f"ERROR SERVICIO: "
                    f"{str(error)}\n"
                )

        except PermissionError:

            print(
                "No se pudo escribir en logs.txt "
                "porque el archivo está bloqueado."
            )

        except Exception as e:

            print(
                "Ocurrió un error al crear el log:",
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

            # Validación capacidad
            if capacidad <= 0:
                raise ServicioError(
                    "Capacidad inválida"
                )

            # Atributo protegido
            self._capacidad = capacidad

        except ServicioError as e:

            self.log_error(e)

            raise

    # Polimorfismo
    def calcular_costo(self, horas=1):

        return self._precio_base * horas

    # Descripción del servicio
    def descripcion(self):

        return (
            f"Servicio Sala: {self._nombre} | "
            f"Capacidad: {self._capacidad}"
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

        # Herencia
        super().__init__(
            nombre,
            precio_base
        )

        try:

            # Validación tipo equipo
            if not tipo_equipo:
                raise ServicioError(
                    "Tipo de equipo requerido"
                )

            # Atributo protegido
            self._tipo_equipo = tipo_equipo

        except ServicioError as e:

            self.log_error(e)

            raise

    # Polimorfismo
    def calcular_costo(self, dias=1):

        return self._precio_base * dias

    # Descripción del servicio
    def descripcion(self):

        return (
            f"Servicio Equipo: {self._nombre} | "
            f"Tipo: {self._tipo_equipo}"
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

        # Herencia
        super().__init__(
            nombre,
            precio_base
        )

        try:

            # Validación especialidad
            if not especialidad:
                raise ServicioError(
                    "Especialidad requerida"
                )

            # Atributo protegido
            self._especialidad = especialidad

        except ServicioError as e:

            self.log_error(e)

            raise

    # Sobrecarga mediante parámetros opcionales
    def calcular_costo(
        self,
        horas=1,
        incluye_material=False
    ):

        # Cálculo básico
        costo = self._precio_base * horas

        # Costo adicional
        if incluye_material:
            costo += 50

        return costo

    # Descripción del servicio
    def descripcion(self):

        return (
            f"Servicio Asesoría: "
            f"{self._nombre} | "
            f"Especialidad: "
            f"{self._especialidad}"
        )


# ==========================================
# PRUEBAS DEL ARCHIVO
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
        # GENERAR ERROR INTENCIONAL
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