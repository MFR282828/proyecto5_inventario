# 📦 Sistema de Gestión de Inventario (CLI)

Un sistema interactivo en consola para la gestión de inventarios, construido en **Python 3.13** aplicando arquitectura modular en capas, programación defensiva con Orientación a Objetos (POO), persistencia relacional en **SQLite3** y gestión de entornos modernos con **`uv`**.

---

## 🚀 Características Principales

* **CRUD Completo:** Registro, consulta, actualización (precio/stock) y eliminación interactiva de productos.
* **Programación Defensiva (POO):** Encapsulamiento y validación estricta mediante decoradores `@property` y `@setter` (impide datos corruptos como precios o stock negativos).
* **Persistencia Segura en SQLite:** Consultas SQL parametrizadas que garantizan integridad de datos y previenen vulnerabilidades como **Inyección SQL**.
* **Arquitectura Modular (`src` package):** Separación estricta de responsabilidades entre el modelo de dominio, la capa de persistencia y la interfaz de usuario.
* **Gestión Moderna con `uv`:** Uso de `pyproject.toml` y `uv.lock` para una gestión ultra-rápida y reproducible del entorno virtual.

---

## 🏗️ Estructura del Proyecto

```text
proyecto5_inventario/
├── src/
│   ├── models.py       # Modelo de dominio (Producto) y validación de reglas de negocio
│   ├── database.py     # Capa de persistencia, conexión a SQLite3 y ejecutor CRUD
│   └── main.py         # Interfaz de usuario (CLI) y orquestación de operaciones
├── .gitignore          # Reglas de exclusión para Git (.venv, *.db, *.log)
├── pyproject.toml      # Configuración del proyecto Python gestionado por uv
├── uv.lock             # Bloqueo determinista de dependencias
└── README.md           # Documentación técnica del repositorio