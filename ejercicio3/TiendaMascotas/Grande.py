from enum import Enum
from TiendaMascotas.Perro import Perro

class razaGrande(Enum):
    PASTOR_ALEMAN = "Pastor alemán"
    DOBERMAN = "Doberman"
    ROTWEILLER = "Rotweiller"

class Grande(Perro):
    def __init__(self, name, edad, color, peso, muerde, razaGrande):
        super().__init__(name, edad, color, peso, muerde)
        self.razaGrande = razaGrande

    def imprimir(self):
        super().imprimir()
        print("Tamaño: Grande")
        print(f"Raza: {self.razaGrande.value}")