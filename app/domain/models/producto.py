"""
Entidad de dominio: Producto.

Esta clase NO conoce FastAPI, Pydantic, ni MongoDB. Es Python puro.
Equivalente conceptual a un POJO de dominio en arquitectura hexagonal Java
(NO a una @Entity de JPA, que ya está contaminada con anotaciones de persistencia).
"""
from dataclasses import dataclass,field
from datetime import datetime,timezone
from uuid import uuid4
@dataclass
class Producto:
    """
    Nombre del producto.
    """
    nombre:str
    """
    Descripción breve del producto.
    """
    descripcion:str
    """
    Categoría a la que pertenece el producto.
    """
    precio:float
    """
    Cantidad disponible en stock del producto.
    """
    stock: int
    """
    Identificador único del producto, generado automáticamente.
    """
    id:str = field(default_factory=lambda: str(uuid4()))
    """ 
    Fecha de creación del producto.
    """
    creado_en: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    """
    Fecha de última actualización del producto.
    Se actualiza automáticamente cada vez que se modifica el producto.
    """
    actualizado_en: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __post_init__(self) -> None:
        self.validar()

    def validar(self) -> None:
        """Reglas de negocio invariantes. Se ejecutan SIEMPRE que se crea
              o reconstruye un Producto, sin importar quién lo llame."""
        if not self.nombre or not self.nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        if self.precio < 0:
            raise ValueError("El precio del producto no puede ser negativo.")
        if self.stock < 0:
            raise ValueError("El stock del producto no puede ser negativo.")

    def actualizar_stock(self,cantidad: int) -> None:
        """Ejemplo de comportamiento de negocio que vive en el dominio,
        no en un service ni en un controller."""
        nuevo_stock = self.stock + cantidad
        if nuevo_stock < 0:
            raise ValueError("El stock resultante no puede ser negativo.")
        self.stock = nuevo_stock
        self.actualizado_en = datetime.now(timezone.utc)

    def actualizar_datos(
            self,
            nombre:str|None = None,
            descripcion:str|None = None,
            precio:float|None = None
    ) -> None:
        """Actualiza campos editables y revalida invariantes."""
        if nombre is not None:
            self.nombre = nombre
        if descripcion is not None:
            self.descripcion = descripcion
        if precio is not None:
            self.precio = precio
        self.validar()
        self.actualizado_en = datetime.now(timezone.utc)


