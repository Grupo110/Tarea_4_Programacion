# ===============================
# CLASE BASE SERVICIO
# ===============================

class Servicio:

    # Constructor de la clase base
    def __init__(self, nombre, precio_base):
        
        # Validamos que el nombre no esté vacío
        if not nombre:
            raise ValueError("El servicio debe tener nombre")

        # Validamos que el precio sea mayor a 0
        if precio_base <= 0:
            raise ValueError("Precio inválido")

        # Guardamos los datos como atributos protegidos
        self._nombre = nombre
        self._precio_base = precio_base


# ===============================
# CLASE SERVICIO SALA (HEREDA)
# ===============================

class ServicioSala(Servicio):

    # Constructor
    def __init__(self, nombre, precio_base, capacidad):
        
        # Llamamos al constructor de la clase padre
        super().__init__(nombre, precio_base)

        # Validamos capacidad
        if capacidad <= 0:
            raise ValueError("Capacidad inválida")

        # Guardamos la capacidad
        self._capacidad = capacidad

    # Método para calcular costo
    def calcular_costo(self, horas=1):
        
        # Multiplicamos el precio por horas
        return self._precio_base * horas


# ===============================
# CLASE SERVICIO EQUIPO (HEREDA)
# ===============================

class ServicioEquipo(Servicio):

    # Constructor
    def __init__(self, nombre, precio_base, tipo_equipo):
        
        # Llamamos al constructor padre
        super().__init__(nombre, precio_base)

        # Validamos tipo de equipo
        if not tipo_equipo:
            raise ValueError("Tipo de equipo requerido")

        # Guardamos el tipo de equipo
        self._tipo_equipo = tipo_equipo

    # Método para calcular costo
    def calcular_costo(self, dias=1):
        
        # Multiplicamos el precio por días
        return self._precio_base * dias


# ===============================
# CLASE SERVICIO ASESORIA (HEREDA)
# ===============================

class ServicioAsesoria(Servicio):

    # Constructor
    def __init__(self, nombre, precio_base, especialidad):
        
        # Llamamos al constructor padre
        super().__init__(nombre, precio_base)

        # Validamos especialidad
        if not especialidad:
            raise ValueError("Especialidad requerida")

        # Guardamos la especialidad
        self._especialidad = especialidad

    # Método para calcular costo
    def calcular_costo(self, horas=1, incluye_material=False):
        
        # Calculamos costo base
        costo = self._precio_base * horas

        # Si incluye material, se suma costo extra
        if incluye_material:
            costo += 50

        # Retornamos el costo total
        return costo


# ===============================
# PRUEBAS DEL ARCHIVO
# ===============================

if __name__ == "__main__":

    try:
        # Creamos servicio de sala
        s1 = ServicioSala("Sala VIP", 50, 10)
        print("Costo sala:", s1.calcular_costo(2))

        # Creamos servicio de equipo
        s2 = ServicioEquipo("Laptop", 30, "Tecnología")
        print("Costo equipo:", s2.calcular_costo(3))

        # Creamos servicio de asesoría
        s3 = ServicioAsesoria("Consultoría", 100, "Software")
        print("Costo asesoría:", s3.calcular_costo(2, True))

        # Generamos error para probar validaciones
        s4 = ServicioSala("Sala mala", -10, 0)

    except Exception as e:
        # Capturamos y mostramos el error
        print("Error:", e)