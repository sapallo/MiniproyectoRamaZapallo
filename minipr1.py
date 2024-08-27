import tkinter as tk

#  ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")

# Etiquetas y campos de entrada
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack(padx=20, pady=15)
entrada_nombre = tk.Entry(ventana, width=50)
entrada_nombre.pack(padx=10, pady=5)

label_telefono = tk.Label(ventana, text="Teléfono:")
label_telefono.pack(padx=20, pady=15)
entrada_telefono = tk.Entry(ventana, width=50)
entrada_telefono.pack(padx=10, pady=5)

ventana.mainloop()
