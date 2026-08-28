class Mascota:
    """
    Clase padre que representa una mascota de forma general.

    Las clases Perro, Gato y Conejo heredan de Mascota para reutilizar
    los atributos comunes nombre y costo_consulta. Cada clase hija
    sobrescribe el método obtener_descripcion() con sus propios datos.
    """

    def __init__(self, nombre, costo_consulta):
        """Inicializa una mascota con su nombre y costo de consulta."""
        self.nombre = nombre
        self._costo_consulta = None
        self.set_costo_consulta(costo_consulta)

    def get_costo_consulta(self):
        """Retorna el costo actual de la consulta de la mascota."""
        return self._costo_consulta

    def set_costo_consulta(self, costo_consulta):
        """
        Modifica el costo de consulta.
        Regla de negocio: el costo debe ser mayor que 0.
        """
        if costo_consulta <= 0:
            print("Error: el costo de consulta debe ser mayor que 0.")
            return False

        self._costo_consulta = costo_consulta
        return True

    def obtener_descripcion(self):
        """
        Retorna una descripción general de la mascota.
        Las clases hijas sobrescriben este método para aplicar polimorfismo.
        """
        return f"Mascota: {self.nombre} | Costo consulta: ${self._costo_consulta:,.0f}"
