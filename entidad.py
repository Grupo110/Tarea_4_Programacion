# =========================================================
# SISTEMA DE RESERVAS - SOFTWARE FJ
# Autor: JUAN DAVID CARVAJAL FRANCO
# Revisado por: JULIO CESAR SALGADO MARIN
# =========================================================

# MODIFICACIONES REALIZADAS:
#
# 1. Se agregó validación del identificador para evitar
#    que las entidades se creen con valores vacíos.
#
# 2. Se implementó correctamente la clase abstracta
#    utilizando ABC y @abstractmethod.
#
# 3. Se aplicó encapsulación usando el atributo privado _id.
#
# 4. Se añadió el decorador @property para acceder
#    de forma controlada al identificador.
#
# 5. Se mejoraron los comentarios y la documentación
#    interna del código para facilitar su comprensión.
#
# 6. Se dejó el método descripcion() como abstracto
#    para obligar a las clases hijas a implementarlo.
#
# =========================================================

from abc import ABC, abstractmethod


class Entidad(ABC):
    """Clase abstracta general para entidades del sistema."""

    def __init__(self, identificador):

        # Validación del identificador
        if not identificador:
            raise ValueError("El identificador no puede estar vacío")

        self._id = identificador

    @property
    def id(self):
        """Retorna el identificador de la entidad."""
        return self._id

    @abstractmethod
    def descripcion(self):
        """
        Método abstracto que debe implementarse
        en las clases hijas.
        """
        pass
