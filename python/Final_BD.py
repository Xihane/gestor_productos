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
    for widget in root.winfo_children():
        widget.destroy()

    frame = ctk.CTkFrame(root)
    frame.pack(expand=True, pady=20, padx=20)

    ctk.CTkLabel(frame, text="Nombre del Producto:").pack(pady=5)
    entry_nombre = ctk.CTkEntry(frame)
    entry_nombre.pack()

    ctk.CTkLabel(frame, text="Descripción del Producto:").pack(pady=5)
    entry_descripcion = ctk.CTkEntry(frame)
    entry_descripcion.pack()

    ctk.CTkLabel(frame, text="Precio del Producto:").pack(pady=5)
    entry_precio = ctk.CTkEntry(frame)
    entry_precio.pack()

    ctk.CTkLabel(frame, text="Stock del Producto:").pack(pady=5)
    entry_stock = ctk.CTkEntry(frame)
    entry_stock.pack()

    ctk.CTkLabel(frame, text="ID de Categoría:").pack(pady=5)
    entry_id_categoria = ctk.CTkEntry(frame)
    entry_id_categoria.pack()

    def guardar_producto():
        nombre = entry_nombre.get()
        descripcion = entry_descripcion.get()
        precio = entry_precio.get()
        stock = entry_stock.get()
        id_categoria = entry_id_categoria.get()
        
        if nombre and descripcion and precio and stock:
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
                    mostrar_menu()
            except Error as e:
                messagebox.showerror("Error", f"No se pudo cargar el producto: {e}")
        else:
            messagebox.showwarning("Advertencia", "Debe completar todos los campos.")

    ctk.CTkButton(frame, text="Guardar", command=guardar_producto).pack(pady=10)
    ctk.CTkButton(frame, text="Volver al menú", command=mostrar_menu).pack(pady=10)

# Función para modificar un producto
def modificar_producto():
    for widget in root.winfo_children():
        widget.destroy()

    frame = ctk.CTkFrame(root)
    frame.pack(expand=True, pady=20, padx=20)

    ctk.CTkLabel(frame, text="ID del Producto a Modificar:").pack(pady=5)
    entry_id = ctk.CTkEntry(frame)
    entry_id.pack()

    ctk.CTkLabel(frame, text="Nuevo Nombre del Producto:").pack(pady=5)
    entry_nombre = ctk.CTkEntry(frame)
    entry_nombre.pack()

    ctk.CTkLabel(frame, text="Nuevo Precio del Producto:").pack(pady=5)
    entry_precio = ctk.CTkEntry(frame)
    entry_precio.pack()

    ctk.CTkLabel(frame, text="Nuevo Stock del Producto:").pack(pady=5)
    entry_stock = ctk.CTkEntry(frame)
    entry_stock.pack()

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
                    mostrar_menu()
            except Error as e:
                messagebox.showerror("Error", f"No se pudo modificar el producto: {e}")
        else:
            messagebox.showwarning("Advertencia", "Debe completar todos los campos.")

    ctk.CTkButton(frame, text="Actualizar", command=actualizar_producto).pack(pady=10)
    ctk.CTkButton(frame, text="Volver al menú", command=mostrar_menu).pack(pady=10)

# Función para listar los productos
def listar_productos():
    for widget in root.winfo_children():
        widget.destroy()
    
    frame = ctk.CTkFrame(root)
    frame.pack(expand=True, pady=20, padx=20)

    try:
        conn = conectar_db()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM producto")
            productos = cursor.fetchall()
            cursor.close()
            conn.close()

            lista_productos = "\n".join([f"ID: {p[0]}, Nombre: {p[1]}, Precio: {p[3]}, Stock: {p[4]}" for p in productos])
            ctk.CTkLabel(frame, text="Lista de Productos:").pack(pady=5)
            ctk.CTkLabel(frame, text=lista_productos if lista_productos else "No hay productos registrados.").pack(pady=5)
    except Error as e:
        messagebox.showerror("Error", f"No se pudo listar los productos: {e}")

    ctk.CTkButton(frame, text="Volver al menú", command=mostrar_menu).pack(pady=10)

# Función para eliminar un producto
def eliminar_producto():
    for widget in root.winfo_children():
        widget.destroy()

    frame = ctk.CTkFrame(root)
    frame.pack(expand=True, pady=20, padx=20)

    ctk.CTkLabel(frame, text="ID del Producto a Eliminar:").pack(pady=5)
    entry_id = ctk.CTkEntry(frame)
    entry_id.pack()

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
                    mostrar_menu()
            except Error as e:
                messagebox.showerror("Error", f"No se pudo eliminar el producto: {e}")
        else:
            messagebox.showwarning("Advertencia", "Debe ingresar un ID de producto.")

    ctk.CTkButton(frame, text="Eliminar", command=borrar_producto).pack(pady=10)
    ctk.CTkButton(frame, text="Volver al menú", command=mostrar_menu).pack(pady=10)

# Función principal que contiene el menú
def mostrar_menu():
    for widget in root.winfo_children():
        widget.destroy()
    
    menu_principal = ctk.CTkFrame(root)
    menu_principal.pack(expand=True, pady=20, padx=20)

    ctk.CTkButton(menu_principal, text="Cargar nuevo producto", command=cargar_producto).pack(pady=5)
    ctk.CTkButton(menu_principal, text="Modificar producto existente", command=modificar_producto).pack(pady=5)
    ctk.CTkButton(menu_principal, text="Listar productos", command=listar_productos).pack(pady=5)
    ctk.CTkButton(menu_principal, text="Eliminar producto", command=eliminar_producto).pack(pady=5)
    ctk.CTkButton(menu_principal, text="Salir", command=root.quit).pack(pady=5)
    
def centrar_ventana(ventana, ancho, alto):
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()
    posicion_x = int(screen_width / 2 - ancho / 2)
    posicion_y = int(screen_height / 2 - alto / 2)
    ventana.geometry(f'{ancho}x{alto}+{posicion_x}+{posicion_y}')

# Crear ventana principal
root = ctk.CTk()
root.geometry("500x600")
centrar_ventana(root, 500, 600)
root.title("Gestión de Productos")

# Mostrar el menú
mostrar_menu()

# Ejecutar la aplicación
root.mainloop()
