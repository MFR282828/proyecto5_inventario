class Producto:
    """Representa un producto dentro del sistema de inventario."""

    def __init__(self, nombre: str, precio: float, stock: int, id_producto: int | None = None) -> None:
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self._precio = float(valor)

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, valor: int) -> None:
        if valor < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = int(valor)

    def __repr__(self) -> str:
        return f"Producto(id={self.id_producto}, nombre='{self.nombre}', precio={self.precio}, stock={self.stock})"