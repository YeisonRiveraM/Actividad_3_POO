class Persona:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion

    @property
    def nombre(self):
        return self._nombre
     
    @property
    def direccion(self):
        return self._direccion
    
    @nombre.setter
    def nombre(self, newNombre):
        self._nombre = newNombre

    @direccion.setter
    def direccion(self, newdireccion):
        self._direccion = newdireccion

        