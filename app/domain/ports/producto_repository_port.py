"""
Port (puerto) de salida: define el contrato que el dominio/aplicación
exige para persistir y consultar Productos, sin saber qué tecnología
hay detrás (Mongo, Postgres, memoria, etc).

Equivalente conceptual a una interface Java en arquitectura hexagonal:

    public interface ProductoRepositoryPort {
        Producto save(Producto producto);
        Optional<Producto> findById(String id);
        List<Producto> findAll();
        void deleteById(String id);
    }

A diferencia de `extends MongoRepository<...>`, esta interfaz NO sabe
nada de MongoDB. Cualquier adapter (Mongo, Postgres, en memoria para
tests) puede implementarla.
"""

from abc import ABC, abstractmethod

from app.domain.models.producto import Producto


class ProductoRepositoryPort(ABC):

    @abstractmethod
    async def guardar(self, producto: Producto) -> Producto:
        """Inserta un nuevo producto y lo devuelve."""
        raise NotImplementedError

    @abstractmethod
    async def obtener_por_id(self, producto_id: str) -> Producto | None:
        """Devuelve el producto si existe, o None si no se encuentra."""
        raise NotImplementedError

    @abstractmethod
    async def listar_todos(self) -> list[Producto]:
        """Devuelve todos los productos."""
        raise NotImplementedError

    @abstractmethod
    async def actualizar(self, producto: Producto) -> Producto:
        """Persiste los cambios de un producto existente y lo devuelve."""
        raise NotImplementedError

    @abstractmethod
    async def eliminar_por_id(self, producto_id: str) -> bool:
        """Elimina el producto. Devuelve True si existía y se borró,
        False si no existía."""
        raise NotImplementedError