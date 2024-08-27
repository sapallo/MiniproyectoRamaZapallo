import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")

# Etiquetas y campos de entrada
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack(padx=10, pady=5)
entrada_nombre = tk.Entry(ventana, width=50)
entrada_nombre.pack(padx=10, pady=5)

label_telefono = tk.Label(ventana, text="Teléfono:")
label_telefono.pack(padx=10, pady=5)
entrada_telefono = tk.Entry(ventana, width=50)
entrada_telefono.pack(padx=10, pady=5)

# Botones
boton_agregar = tk.Button(ventana, text="Agregar Contacto")
boton_agregar.pack(pady=10)

boton_buscar = tk.Button(ventana, text="Buscar Contacto")
boton_buscar.pack(pady=10)

boton_editar = tk.Button(ventana, text="Editar Contacto")
boton_editar.pack(pady=10)

boton_eliminar = tk.Button(ventana, text="Eliminar Contacto")
boton_eliminar.pack(pady=10)

# Ejecutar el loop principal de la interfaz
ventana.mainloop()
