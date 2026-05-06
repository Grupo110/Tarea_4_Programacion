#Julio Cesar Salgado 

# Clase Cliente independiente (SIN importar otros archivos)

class Cliente:

    # Constructor
    def __init__(self, id, nombre, email):
        
        # Guardamos el id
        self._id = id

        # Validamos nombre
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")

        # Validamos email
        if "@" not in email:
            raise ValueError("El email no es válido")

        # Guardamos datos
        self._nombre = nombre
        self._email = email


    # Método para mostrar información
    def mostrar_info(self):
        return f"Cliente: {self._nombre}, Email: {self._email}"


# ===============================
# PRUEBA DEL ARCHIVO (main interno)
# ===============================
if __name__ == "__main__":

    try:
        # Creamos cliente válido
        c1 = Cliente(1, "Julio", "julio@gmail.com")
        print(c1.mostrar_info())
 
        # Cliente inválido (para probar error)
        c2 = Cliente(2, "", "correo.com")

    except Exception as e:
        print("Error:", e)