from enum import Enum
from TiendaMascotas.Gato import Gato

class razaCorto(Enum):
    AZUL_RUSO = "Azul ruso"
    BRITANICO = "Britanico"
    MANX = "Manx"
    DEVON_REX = "Devon Rex"

class PeloCorto(Gato):
    def __init__(self, name, edad, color, altSalto, longSalto, razaCorto):
        super().__init__(name, edad, color, altSalto, longSalto)
        self.razaCorto = razaCorto

    def imprimir(self):
        super().imprimir()
        print("Pelo: Corto")
        print(f"Raza: {self.razaCorto.value}")