import tkinter as tk

# la idea es que el array de contactos que aca lleva el nombre de "lista" sea 
# global para que pueda ser utilizado por "editar" y "eliminar"
lista = ["apple", "banana", "cherry"]

# Función que se ejecuta al presionar el botón de búsqueda. O tb podemos usar la de Natasha
# pero la cosa es que la funcion buscar este antes que los botones
def buscar():
    contacto = entrada.get() 
    
    if contacto in lista:
        print(f"{contacto} encontrado")
        boton_eliminar.pack(pady=10)  # Muestra el botón "Eliminar"
        boton_editar.pack(pady=10)  # Muestra el botón "Editar"
    else:
        print(f"{contacto} no encontrado")
        boton_eliminar.pack_forget()  # Oculta el botón "Eliminar"
        boton_editar.pack_forget()  # Oculta el botón "Editar"

# Función para eliminar un contacto
def eliminar():
    contacto = entrada.get()
    
    if contacto in lista:
        lista.remove(contacto)
        print(f"{contacto} eliminado")
        boton_eliminar.pack_forget()  # Oculta el botón "Eliminar" después de eliminar
        boton_editar.pack_forget()  # Oculta el botón "Editar" después de eliminar
    else:
        print(f"{contacto} no se encuentra en la lista")

# Función para editar un contacto
def editar():
    contacto = entrada.get()
    print(f"Editando {contacto}")
    # Aca se puede agregar el código para editar un contacto abriendo una ventana
    ventana_editar = tk.Toplevel(ventana)
    ventana_editar.title(f"Editar {contacto}")
    label_editar = tk.Label(ventana_editar, text=f"Editando {contacto}")
    label_editar.pack(padx=10, pady=10)

# Ventana principal
ventana = tk.Tk()
ventana.title("La Agendita Definitiva")

# barra de búsqueda
entrada = tk.Entry(ventana, width=50)
entrada.pack(padx=10, pady=10)

# botón de búsqueda
boton_buscar = tk.Button(ventana, text="Buscar", command=buscar)
boton_buscar.pack(pady=10)

# botón de eliminar (inicialmente oculto)
boton_eliminar = tk.Button(ventana, text="Eliminar", command=eliminar)
boton_eliminar.pack_forget()  # con este metodo queda oculto inicialmente

# botón de editar (inicialmente oculto)
boton_editar = tk.Button(ventana, text="Editar", command=editar)
boton_editar.pack_forget()  # oculto inicialmente


ventana.mainloop()