from Universidad.Persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, direccion, carrera, semestre):
        super().__init__(nombre, direccion)
        self.carrera = carrera
        self.semestre = semestre
    
    @property
    def carrera(self):
        return self._carrera
    
    @property
    def semestre(self):
        return self._semestre
    
    @carrera.setter
    def carrera(self, newcarrera):
        self._carrera = newcarrera

    @semestre.setter
    def semestre(self, newsemestre):
        self._semestre = newsemestre