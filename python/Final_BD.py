import mysql.connector
from mysql.connector import Error
import customtkinter as ctk
from tkinter import messagebox


# Función para conectar a la base de datos
def conectar_db():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='final_bd',
            user='root',
            password=''
        )
        if conn.is_connected():
            return conn
    except Error as e:
        messagebox.showerror("Error", f"Error al conectar a la base de datos: {e}")
        return None

# Función para cargar un nuevo producto
def cargar_producto():
    def guardar_producto():
        nombre = entry_nombre.get()
        descripcion = entry_descripcion.get()
        precio = entry_precio.get()
        stock = entry_stock.get()
        id_categoria = entry_id_categoria.get()
        
        if nombre and descripcion and precio and stock and id_categoria:
            try:
                conn = conectar_db()
                if conn:
                    cursor = conn.cursor()
                    cursor.execute("""
                        INSERT INTO producto (nombre, descripcion, precio, stock, id_categoria)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (nombre, descripcion, float(precio), int(stock), int(id_categoria)))
                    conn.commit()
                    cursor.close()
                    conn.close()
                    messagebox.showinfo("Éxito", "Producto cargado con éxito.")
                    ventana_cargar.destroy()
            except Error as e:
                messagebox.showerror("Error", f"No se pudo cargar el producto: {e}")
        else:
            messagebox.showwarning("Advertencia", "Debe completar todos los campos.")
    
    ventana_cargar = ctk.CTkToplevel(root)
    ventana_cargar.title("Cargar Producto")
    ventana_cargar.geometry("400x400")  # Establecer el tamaño de la ventana de carga

    ctk.CTkLabel(ventana_cargar, text="Nombre del Producto:").pack(pady=5)
    entry_nombre = ctk.CTkEntry(ventana_cargar)
    entry_nombre.pack()

    ctk.CTkLabel(ventana_cargar, text="Descripción del Producto:").pack(pady=5)
    entry_descripcion = ctk.CTkEntry(ventana_cargar)
    entry_descripcion.pack()

    ctk.CTkLabel(ventana_cargar, text="Precio del Producto:").pack(pady=5)
    entry_precio = ctk.CTkEntry(ventana_cargar)
    entry_precio.pack()

    ctk.CTkLabel(ventana_cargar, text="Stock del Producto:").pack(pady=5)
    entry_stock = ctk.CTkEntry(ventana_cargar)
    entry_stock.pack()

    ctk.CTkLabel(ventana_cargar, text="ID de Categoría:").pack(pady=5)
    entry_id_categoria = ctk.CTkEntry(ventana_cargar)
    entry_id_categoria.pack()

    ctk.CTkButton(ventana_cargar, text="Guardar", command=guardar_producto).pack(pady=10)

# Función para modificar un producto
def modificar_producto():
    def actualizar_producto():
        producto_id = entry_id.get()
        nuevo_nombre = entry_nombre.get()
        nuevo_precio = entry_precio.get()
        nuevo_stock = entry_stock.get()

        if producto_id and nuevo_nombre and nuevo_precio and nuevo_stock:
            try:
                conn = conectar_db()
                if conn:
                    cursor = conn.cursor()
                    cursor.execute("""
                        UPDATE producto
                        SET nombre = %s, precio = %s, stock = %s
                        WHERE id_producto = %s
                    """, (nuevo_nombre, float(nuevo_precio), int(nuevo_stock), int(producto_id)))
                    conn.commit()
                    cursor.close()
                    conn.close()
                    messagebox.showinfo("Éxito", "Producto modificado con éxito.")
                    ventana_modificar.destroy()
            except Error as e:
                messagebox.showerror("Error", f"No se pudo modificar el producto: {e}")
        else:
            messagebox.showwarning("Advertencia", "Debe completar todos los campos.")
    
    ventana_modificar = ctk.CTkToplevel(root)
    ventana_modificar.title("Modificar Producto")
    ventana_modificar.geometry("400x300")
    
    ctk.CTkLabel(ventana_modificar, text="ID del Producto a Modificar:").pack(pady=5)
    entry_id = ctk.CTkEntry(ventana_modificar)
    entry_id.pack()

    ctk.CTkLabel(ventana_modificar, text="Nuevo Nombre del Producto:").pack(pady=5)
    entry_nombre = ctk.CTkEntry(ventana_modificar)
    entry_nombre.pack()

    ctk.CTkLabel(ventana_modificar, text="Nuevo Precio del Producto:").pack(pady=5)
    entry_precio = ctk.CTkEntry(ventana_modificar)
    entry_precio.pack()

    ctk.CTkLabel(ventana_modificar, text="Nuevo Stock del Producto:").pack(pady=5)
    entry_stock = ctk.CTkEntry(ventana_modificar)
    entry_stock.pack()

    ctk.CTkButton(ventana_modificar, text="Actualizar", command=actualizar_producto).pack(pady=10)

# Función para listar los productos
def listar_productos():
    try:
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM producto")
            productos = cursor.fetchall()
            cursor.close()
            conn.close()

            lista_productos = "\n".join([f"ID: {p[0]}, Nombre: {p[1]}, Precio: {p[3]}, Stock: {p[4]}" for p in productos])
            messagebox.showinfo("Lista de Productos", lista_productos if lista_productos else "No hay productos registrados.")
    except Error as e:
        messagebox.showerror("Error", f"No se pudo listar los productos: {e}")

# Función para eliminar un producto
def eliminar_producto():
    def borrar_producto():
        producto_id = entry_id.get()

        if producto_id:
            try:
                conn = conectar_db()
                if conn:
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM producto WHERE id_producto = %s", (int(producto_id),))
                    conn.commit()
                    cursor.close()
                    conn.close()
                    messagebox.showinfo("Éxito", "Producto eliminado con éxito.")
                    ventana_eliminar.destroy()
            except Error as e:
                messagebox.showerror("Error", f"No se pudo eliminar el producto: {e}")
        else:
            messagebox.showwarning("Advertencia", "Debe ingresar un ID de producto.")
    
    ventana_eliminar = ctk.CTkToplevel(root)
    ventana_eliminar.title("Eliminar Producto")
    ventana_eliminar.geometry("400x300")

    ctk.CTkLabel(ventana_eliminar, text="ID del Producto a Eliminar:").pack(pady=5)
    entry_id = ctk.CTkEntry(ventana_eliminar)
    entry_id.pack()

    ctk.CTkButton(ventana_eliminar, text="Eliminar", command=borrar_producto).pack(pady=10)

def centrar_ventana(ventana, ancho, alto):
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()
    posicion_x = int(screen_width / 2 - ancho / 2)
    posicion_y = int(screen_height / 2 - alto / 2)
    ventana.geometry(f'{ancho}x{alto}+{posicion_x}+{posicion_y}')


# Función principal que contiene el menú
def mostrar_menu():
    menu_principal = ctk.CTkFrame(root)
    menu_principal.pack(pady=20)

    ctk.CTkButton(menu_principal, text="Cargar nuevo producto", command=cargar_producto).pack(pady=5)
    ctk.CTkButton(menu_principal, text="Modificar producto existente", command=modificar_producto).pack(pady=5)
    ctk.CTkButton(menu_principal, text="Listar productos", command=listar_productos).pack(pady=5)
    ctk.CTkButton(menu_principal, text="Eliminar producto", command=eliminar_producto).pack(pady=5)
    ctk.CTkButton(menu_principal, text="Salir", command=root.quit).pack(pady=5)

# Crear ventana principal
root = ctk.CTk()
root.geometry("600x400")
centrar_ventana(root, 600, 400)
root.title("Gestión de Productos")

# Mostrar el menú
mostrar_menu()

# Ejecutar la aplicación
root.mainloop()
