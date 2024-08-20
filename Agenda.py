from busqueda import buscar_contacto
from Contacto import Contacto

class Agenda:
    def __init__(self):
        self.contactos=[]
        #inicializo una lista

    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)

    def eliminar_contacto(self,nombre):
        contacto= buscar_contacto(self.contactos, nombre)
        if contacto:
            self.contactos.remove(contacto)

    def editar_contacto(self):
        pass

    def buscar_contacto(self):
        pass

    def listar_contactos(self):
        for contacto in self.contactos:
            print("Listado de Contactos")
            print(contacto)
    
agendita=Agenda()
agendita.eliminar_contacto

