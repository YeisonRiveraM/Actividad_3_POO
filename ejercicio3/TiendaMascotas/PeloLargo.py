from enum import Enum
from TiendaMascotas.Gato import Gato

class razaLargo(Enum):
    ANGORA = "Angora"
    HIMALAYO = "Himalayo"
    BALINES = "Balines"
    SOMALI = "Somali"

class PeloLargo(Gato):
    def __init__(self, name, edad, color, altSalto, longSalto, razaLargo):
        super().__init__(name, edad, color, altSalto, longSalto)
        self.razaLargo = razaLargo

    def imprimir(self):
        super().imprimir()
        print("Pelo: Largo")
        print(f"Raza: {self.razaLargo.value}")