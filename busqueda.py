
def buscar_contacto(contactos,nombre):
    for contacto in contactos:
        if contacto.nombre == nombre:
            return contacto
    return None

        