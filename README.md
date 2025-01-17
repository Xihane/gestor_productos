
# Gestor de Productos

Este proyecto es una aplicación de escritorio para la gestión de productos, desarrollada en Python utilizando `mysql.connector`, `customtkinter` y `tkinter`.

## Descripción

La aplicación permite realizar las siguientes operaciones:

- Cargar un nuevo producto
- Modificar un producto existente
- Listar productos
- Eliminar un producto

## Requisitos

- Python 3.x
- `mysql.connector`
- `customtkinter`

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/Xihane/Final_BaseDatos_2024.git
    ```
2. Instala las dependencias necesarias:
    ```bash
    pip install mysql-connector-python customtkinter
    ```

3. Configura tu base de datos MySQL y crea la tabla `producto`:
    ```sql
    CREATE DATABASE final_bd;

    USE final_bd;

    CREATE TABLE producto (
        id_producto INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(255) NOT NULL,
        descripcion TEXT,
        precio FLOAT NOT NULL,
        stock INT NOT NULL,
        id_categoria INT NOT NULL
    );
    ```


## Funcionalidades

### Cargar un nuevo producto

Permite agregar un nuevo producto a la base de datos ingresando el nombre, descripción, precio, stock y la categoría.

### Modificar un producto

Permite modificar el nombre, precio y stock de un producto existente ingresando su ID.

### Listar productos

Muestra una lista de todos los productos registrados en la base de datos.

### Eliminar un producto

Permite eliminar un producto de la base de datos ingresando su ID.


