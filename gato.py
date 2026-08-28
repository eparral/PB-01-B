from mascota import Mascota


class Gato(Mascota):
    """
    Clase hija de Mascota.
    Hereda nombre y costo_consulta y agrega la cantidad de vidas.
    """

    def __init__(self, nombre, costo_consulta, cantidad_vidas):
        """Inicializa un gato y valida que su cantidad de vidas sea mayor que 0."""
        super().__init__(nombre, costo_consulta)
        self._cantidad_vidas = None
        self.set_cantidad_vidas(cantidad_vidas)

    def get_cantidad_vidas(self):
        """Retorna la cantidad de vidas registradas del gato."""
        return self._cantidad_vidas

    def set_cantidad_vidas(self, cantidad_vidas):
        """
        Modifica la cantidad de vidas.
        Regla de negocio: debe ser mayor que 0.
        """
        if cantidad_vidas <= 0:
            print("Error: un gato debe tener una cantidad de vidas mayor que 0.")
            return False

        self._cantidad_vidas = cantidad_vidas
        return True

    def obtener_descripcion(self):
        """
        Sobrescribe el método de Mascota y retorna los datos propios del gato.
        Esta sobrescritura permite aplicar polimorfismo.
        """
        return (
            f"Gato: {self.nombre} | Vidas: {self._cantidad_vidas} | "
            f"Costo consulta: ${self.get_costo_consulta():,.0f}"
        )
