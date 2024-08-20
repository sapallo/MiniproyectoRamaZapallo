class Contacto:

    def __init__(self, nombre, telefono, email, direccion):
        self.nombre=nombre
        self.telefono=telefono
        self.email=email
        self.direccion=direccion

    def __str__(self):
        return (f"Nombre:{self.nombre}\n Telefono:{self.telefono}\n Email:{self.email}\n Direccion:{self.direccion}\n")

pepito=Contacto("Pepito", "3624030303", "pepito@hotmail.com", "calle falsa 123")
print (pepito)