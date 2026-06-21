"""
Excepciones de negocio. Viven en el dominio porque representan
violaciones de reglas de negocio, no errores técnicos de HTTP o de Mongo.

Equivalente a excepciones custom en Java como:
    public class ProductoNoEncontradoException extends RuntimeException
"""

class ProductoError(Exception):
    """Excepción base para errores relacionados con Producto."""
    pass

class ProductoNoEncontrado(ProductoError):
    def __init__(self, producto_id: str):
        self.producto_id = producto_id
        super().__init__(f"Producto con id '{producto_id}' no encontrado")


class ProductoInvalido(ProductoError):
    def __init__(self, mensaje: str):
        super().__init__(mensaje)