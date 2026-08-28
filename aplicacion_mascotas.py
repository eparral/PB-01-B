class AplicacionMascotas:
    """Gestiona el catálogo de mascotas registradas en la aplicación."""

    def __init__(self):
        """Inicializa el catálogo como una lista vacía."""
        self.mascotas = []

    def agregar_mascota(self, mascota):
        """Agrega una mascota al catálogo de la aplicación."""
        self.mascotas.append(mascota)

    def mostrar_catalogo(self):
        """
        Muestra la descripción y costo de consulta de cada mascota.

        Aquí se aplica polimorfismo: todos los objetos se recorren de la misma
        forma, pero Python ejecuta obtener_descripcion() según la clase real
        del objeto (Perro, Gato o Conejo).
        """
        print("\n===== CATÁLOGO DE MASCOTAS =====")

        if not self.mascotas:
            print("No hay mascotas registradas.")
            return

        for mascota in self.mascotas:
            print(mascota.obtener_descripcion())

    def calcular_costo_total_consultas(self):
        """Retorna la suma de los costos de consulta de todas las mascotas."""
        return sum(mascota.get_costo_consulta() for mascota in self.mascotas)
