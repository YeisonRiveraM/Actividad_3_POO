from Universidad.Persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, direccion, departamento, categoria):
        super().__init__(nombre, direccion)
        self.departamento = departamento
        self.categoria = categoria

    @property
    def departamento(self):
        return self._departamento 
    
    @property
    def categoria(self):
        return self._categoria
    
    @departamento.setter
    def departamento(self, newdepartamento):
        self._departamento = newdepartamento

    @categoria.setter
    def categoria(self, newcategoria):
        self._categoria = newcategoria
        