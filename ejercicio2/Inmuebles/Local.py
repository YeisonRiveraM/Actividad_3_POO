from enum import Enum
from Inmuebles.Inmueble import Inmueble

class tipoLocal(Enum):
    INTERNO = "INTERNO"
    CALLE = "CALLE"

class Local(Inmueble):
    def __init__(self, identificadorInmobiliario, area, direccion, tipoLocal):
        super().__init__(identificadorInmobiliario, area, direccion)
        self._tipoLocal = tipoLocal

    def imprimir(self):
        super().imprimir()
        print(f"Tipo de local: {self._tipoLocal}")
        