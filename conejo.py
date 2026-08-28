from mascota import Mascota


class Conejo(Mascota):
    """
    Clase hija de Mascota.
    Hereda nombre y costo_consulta y agrega el tipo de alimentación.
    """

    def __init__(self, nombre, costo_consulta, tipo_alimentacion):
        """Inicializa un conejo y valida que su alimentación no esté vacía."""
        super().__init__(nombre, costo_consulta)
        self._tipo_alimentacion = None
        self.set_tipo_alimentacion(tipo_alimentacion)

    def get_tipo_alimentacion(self):
        """Retorna el tipo de alimentación registrado para el conejo."""
        return self._tipo_alimentacion

    def set_tipo_alimentacion(self, tipo_alimentacion):
        """
        Modifica el tipo de alimentación.
        Regla de negocio: no puede quedar vacío.
        """
        if not isinstance(tipo_alimentacion, str) or not tipo_alimentacion.strip():
            print("Error: el tipo de alimentación del conejo no puede estar vacío.")
            return False

        self._tipo_alimentacion = tipo_alimentacion.strip()
        return True

    def obtener_descripcion(self):
        """
        Sobrescribe el método de Mascota y retorna los datos propios del conejo.
        Esta sobrescritura permite aplicar polimorfismo.
        """
        return (
            f"Conejo: {self.nombre} | Alimentación: {self._tipo_alimentacion} | "
            f"Costo consulta: ${self.get_costo_consulta():,.0f}"
        )
