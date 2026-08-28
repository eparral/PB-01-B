from mascota import Mascota


class Perro(Mascota):
    """
    Clase hija de Mascota.
    Hereda nombre y costo_consulta y agrega la cantidad de vacunas.
    """

    def __init__(self, nombre, costo_consulta, cantidad_vacunas):
        """Inicializa un perro y valida que tenga al menos una vacuna."""
        super().__init__(nombre, costo_consulta)
        self._cantidad_vacunas = None
        self.set_cantidad_vacunas(cantidad_vacunas)

    def get_cantidad_vacunas(self):
        """Retorna la cantidad de vacunas registradas del perro."""
        return self._cantidad_vacunas

    def set_cantidad_vacunas(self, cantidad_vacunas):
        """
        Modifica la cantidad de vacunas.
        Regla de negocio: debe ser mayor que 0.
        """
        if cantidad_vacunas <= 0:
            print("Error: un perro debe tener una cantidad de vacunas mayor que 0.")
            return False

        self._cantidad_vacunas = cantidad_vacunas
        return True

    def obtener_descripcion(self):
        """
        Sobrescribe el método de Mascota y retorna los datos propios del perro.
        Esta sobrescritura permite aplicar polimorfismo.
        """
        return (
            f"Perro: {self.nombre} | Vacunas: {self._cantidad_vacunas} | "
            f"Costo consulta: ${self.get_costo_consulta():,.0f}"
        )
