import tkinter as tk
from tkinter import messagebox

# Lista para almacenar los contactos (en memoria)
contactos = []

# Función para agregar un contacto
def agregar_contacto():
    nombre = entrada_nombre.get()
    telefono = entrada_telefono.get()
    
    if nombre and telefono:
        contactos.append({'nombre': nombre, 'telefono': telefono})
        entrada_nombre.delete(0, tk.END)
        entrada_telefono.delete(0, tk.END)
        messagebox.showinfo("Éxito", "Contacto agregado correctamente.")
    else:
        messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")

# Función para buscar un contacto
def buscar_contacto():
    nombre = entrada_nombre.get()
    encontrado = False
    
    for contacto in contactos:
        if contacto['nombre'].lower() == nombre.lower():
            entrada_telefono.delete(0, tk.END)
            entrada_telefono.insert(0, contacto['telefono'])
            encontrado = True
            break
    
    if not encontrado:
        messagebox.showwarning("No encontrado", "Contacto no encontrado.")

# Función para editar un contacto
def editar_contacto():
    nombre = entrada_nombre.get()
    telefono = entrada_telefono.get()
    encontrado = False
    
    for contacto in contactos:
        if contacto['nombre'].lower() == nombre.lower():
            contacto['telefono'] = telefono
            messagebox.showinfo("Éxito", "Contacto editado correctamente.")
            encontrado = True
            break
    
    if not encontrado:
        messagebox.showwarning("No encontrado", "Contacto no encontrado.")

# Función para eliminar un contacto
def eliminar_contacto():
    nombre = entrada_nombre.get()
    encontrado = False
    
    for contacto in contactos:
        if contacto['nombre'].lower() == nombre.lower():
            contactos.remove(contacto)
            entrada_telefono.delete(0, tk.END)
            messagebox.showinfo("Éxito", "Contacto eliminado correctamente.")
            encontrado = True
            break
    
    if not encontrado:
        messagebox.showwarning("No encontrado", "Contacto no encontrado.")

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
boton_agregar = tk.Button(ventana, text="Agregar Contacto", command=agregar_contacto)
boton_agregar.pack(pady=10)

boton_buscar = tk.Button(ventana, text="Buscar Contacto", command=buscar_contacto)
boton_buscar.pack(pady=10)

boton_editar = tk.Button(ventana, text="Editar Contacto", command=editar_contacto)
boton_editar.pack(pady=10)

boton_eliminar = tk.Button(ventana, text="Eliminar Contacto", command=eliminar_contacto)
boton_eliminar.pack(pady=10)

# Ejecutar el loop principal de la interfaz
ventana.mainloop()
