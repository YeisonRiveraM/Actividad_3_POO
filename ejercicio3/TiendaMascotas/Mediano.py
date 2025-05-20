from enum import Enum
from TiendaMascotas.Perro import Perro

class razaMediano(Enum):
    COLLIE = "Collie"
    DALMATA = "Dalmata"
    BULLDOG = "Bulldog"
    GALGO = "Galgo"
    SABUESO = "Sabueso"

class Pequeño(Perro):
    def __init__(self, name, edad, color, peso, muerde, razaMediano):
        super().__init__(name, edad, color, peso, muerde)
        self.razaMediano = razaMediano

    def imprimir(self):
        super().imprimir()
        print("Tamaño: Mediano")
        print(f"Raza: {self.razaMediano.value}")