from enum import Enum
from TiendaMascotas.Gato import Gato

class razaNo(Enum):
    ESFINGE = "Esfinge"
    ELFO = "Elfo"
    DONSKOY = "Donskoy"

class PeloNo(Gato):
    def __init__(self, name, edad, color, altSalto, longSalto, razaNo):
        super().__init__(name, edad, color, altSalto, longSalto)
        self.razaNo = razaNo

    def imprimir(self):
        super().imprimir()
        print("Pelo: No")
        print(f"Raza: {self.razaNo.value}")