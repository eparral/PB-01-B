from aplicacion_mascotas import AplicacionMascotas
from perro import Perro
from gato import Gato
from conejo import Conejo


# Archivo principal del programa.
# 1) Crea la aplicación.
# 2) Instancia dos perros, un gato y un conejo.
# 3) Muestra la descripción de cada objeto.
# 4) Usa un setter para modificar el costo de una mascota.
# 5) Agrega las mascotas a la aplicación.
# 6) Muestra el catálogo completo y calcula el costo total de consultas.
def main():
    """Ejecuta la demostración principal del Sistema de Gestión de Mascotas."""
    aplicacion = AplicacionMascotas()

    # Se crean al menos dos perros, un gato y un conejo.
    perro_1 = Perro("Rocky", 18000, 4)
    perro_2 = Perro("Luna", 20000, 3)
    gato_1 = Gato("Michi", 16000, 7)
    conejo_1 = Conejo("Copito", 15000, "Heno y verduras")

    print("===== OBJETOS CREADOS =====")
    print(perro_1.obtener_descripcion())
    print(perro_2.obtener_descripcion())
    print(gato_1.obtener_descripcion())
    print(conejo_1.obtener_descripcion())

    # Uso solicitado del setter para modificar el costo de consulta.
    print("\nModificando costo de consulta de Rocky a $22.000...")
    perro_1.set_costo_consulta(22000)
    print(perro_1.obtener_descripcion())

    # Se agregan todos los objetos al catálogo de la aplicación.
    aplicacion.agregar_mascota(perro_1)
    aplicacion.agregar_mascota(perro_2)
    aplicacion.agregar_mascota(gato_1)
    aplicacion.agregar_mascota(conejo_1)

    # Al recorrer mascotas de distintos tipos usando el mismo método
    # obtener_descripcion(), se está aplicando polimorfismo.
    aplicacion.mostrar_catalogo()

    costo_total = aplicacion.calcular_costo_total_consultas()
    print(f"\nCosto total de consultas: ${costo_total:,.0f}")


if __name__ == "__main__":
    main()
