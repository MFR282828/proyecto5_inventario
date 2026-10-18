import sys
from src.database import (
    actualizar_producto,
    eliminar_producto,
    inicializar_db,
    insertar_producto,
    listar_productos,
    obtener_producto_por_id,
)
from src.models import Producto


def mostrar_menu() -> None:
    print("\n" + "=" * 40)
    print(" 📦 GESTOR DE INVENTARIO (SQLite + UV) ")
    print("=" * 40)
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Actualizar producto (Precio / Stock)")
    print("4. Eliminar producto")
    print("5. Salir")


def registrar_producto_ui() -> None:
    print("\n--- Agregar Nuevo Producto ---")
    nombre = input("Nombre del producto: ").strip()

    if not nombre:
        print("❌ Error: El nombre no puede estar vacío.")
        return

    try:
        precio = float(input("Precio ($): "))
        stock = int(input("Cantidad en stock: "))

        nuevo_producto = Producto(nombre=nombre, precio=precio, stock=stock)
        id_generado = insertar_producto(nuevo_producto)
        print(f"✅ ¡Producto '{nombre}' registrado con éxito! (ID asignado: {id_generado})")

    except ValueError as err:
        print(f"❌ Error de entrada o validación: {err}")


def listar_productos_ui() -> None:
    print("\n--- Inventario Actual ---")
    productos = listar_productos()

    if not productos:
        print("📭 La base de datos está vacía.")
        return

    print(f"{'ID':<5} | {'Nombre':<20} | {'Precio':<10} | {'Stock':<6}")
    print("-" * 50)
    for p in productos:
        print(f"{p.id_producto:<5} | {p.nombre:<20} | ${p.precio:<9.2f} | {p.stock:<6}")


def actualizar_producto_ui() -> None:
    print("\n--- Actualizar Producto ---")
    try:
        id_prod = int(input("Ingrese el ID del producto a actualizar: "))
        producto_existente = obtener_producto_por_id(id_prod)

        if not producto_existente:
            print(f"❌ No existe ningún producto con el ID {id_prod}.")
            return

        print(f"Modificando: {producto_existente.nombre} (Actual -> Precio: ${producto_existente.precio:.2f}, Stock: {producto_existente.stock})")

        nuevo_precio = float(input("Nuevo Precio ($): "))
        nuevo_stock = int(input("Nuevo Stock: "))

        # Validamos los nuevos datos instanciando temporalmente un Producto para activar los setters
        Producto(nombre=producto_existente.nombre, precio=nuevo_precio, stock=nuevo_stock)

        if actualizar_producto(id_prod, nuevo_precio, nuevo_stock):
            print(f"✅ Producto ID {id_prod} actualizado correctamente.")
        else:
            print("⚠️ No se pudo realizar la actualización.")

    except ValueError as err:
        print(f"❌ Error de entrada o validación: {err}")


def eliminar_producto_ui() -> None:
    print("\n--- Eliminar Producto ---")
    try:
        id_prod = int(input("Ingrese el ID del producto a eliminar: "))
        producto = obtener_producto_por_id(id_prod)

        if not producto:
            print(f"❌ No existe ningún producto con el ID {id_prod}.")
            return

        confirmacion = input(f"⚠️ ¿Está seguro de eliminar '{producto.nombre}' (ID: {id_prod})? (s/n): ").strip().lower()

        if confirmacion == "s":
            if eliminar_producto(id_prod):
                print(f"🗑️ Producto '{producto.nombre}' eliminado exitosamente.")
            else:
                print("❌ Ocurrió un error al intentar eliminar.")
        else:
            print("Operación cancelada.")

    except ValueError as err:
        print(f"❌ Error: Debe ingresar un ID numérico válido. ({err})")


def main() -> None:
    inicializar_db()

    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción (1-5): ").strip()

        if opcion == "1":
            registrar_producto_ui()
        elif opcion == "2":
            listar_productos_ui()
        elif opcion == "3":
            actualizar_producto_ui()
        elif opcion == "4":
            eliminar_producto_ui()
        elif opcion == "5":
            print("\n👋 ¡Gracias por usar el sistema! Saliendo...")
            sys.exit(0)
        else:
            print("⚠️ Opción no válida. Intenta con un número del 1 al 5.")


if __name__ == "__main__":
    main()