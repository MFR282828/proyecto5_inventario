import sqlite3
from src.models import Producto

DB_NAME = "inventario.db"


def obtener_conexion() -> sqlite3.Connection:
    """Establece y retorna la conexión con la base de datos SQLite."""
    conexion = sqlite3.connect(DB_NAME)
    conexion.row_factory = sqlite3.Row  # Permite acceder a las columnas por nombre
    return conexion


def inicializar_db() -> None:
    """Crea la tabla de productos si no existe."""
    query = """
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        stock INTEGER NOT NULL
    );
    """
    with obtener_conexion() as conn:
        conn.execute(query)


def insertar_producto(producto: Producto) -> int:
    """Guarda un nuevo producto en la base de datos y retorna su ID asignado."""
    query = "INSERT INTO productos (nombre, precio, stock) VALUES (?, ?, ?)"
    with obtener_conexion() as conn:
        cursor = conn.execute(query, (producto.nombre, producto.precio, producto.stock))
        return cursor.lastrowid


def listar_productos() -> list[Producto]:
    """Obtiene todos los productos registrados en la base de datos."""
    query = "SELECT id, nombre, precio, stock FROM productos"
    with obtener_conexion() as conn:
        cursor = conn.execute(query)
        filas = cursor.fetchall()
        return [
            Producto(
                id_producto=fila["id"],
                nombre=fila["nombre"],
                precio=fila["precio"],
                stock=fila["stock"],
            )
            for fila in filas
        ]

def obtener_producto_por_id(id_producto: int) -> Producto | None:
    """Busca un producto específico en la base de datos por su ID."""
    query = "SELECT id, nombre, precio, stock FROM productos WHERE id = ?"
    with obtener_conexion() as conn:
        cursor = conn.execute(query, (id_producto,))
        fila = cursor.fetchone()
        if fila:
            return Producto(
                id_producto=fila["id"],
                nombre=fila["nombre"],
                precio=fila["precio"],
                stock=fila["stock"],
            )
        return None


def actualizar_producto(id_producto: int, nuevo_precio: float, nuevo_stock: int) -> bool:
    """Actualiza precio y stock de un producto existente. Retorna True si modificó alguna fila."""
    query = "UPDATE productos SET precio = ?, stock = ? WHERE id = ?"
    with obtener_conexion() as conn:
        cursor = conn.execute(query, (nuevo_precio, nuevo_stock, id_producto))
        return cursor.rowcount > 0


def eliminar_producto(id_producto: int) -> bool:
    """Elimina un producto por su ID. Retorna True si eliminó la fila exitosamente."""
    query = "DELETE FROM productos WHERE id = ?"
    with obtener_conexion() as conn:
        cursor = conn.execute(query, (id_producto,))
        return cursor.rowcount > 0