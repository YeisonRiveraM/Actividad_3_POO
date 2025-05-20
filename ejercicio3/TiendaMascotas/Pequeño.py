from enum import Enum
from TiendaMascotas.Perro import Perro

class razaPequeña(Enum):
    CANICHE = "Caniche"
    YORKSHIRE_TERRIER = "Yorkshire terrier"
    SCHNAUZER = "Schnauzer"
    CHIHUAHUA = "Chihuahua"

class Pequeño(Perro):
    def __init__(self, name, edad, color, peso, muerde, razaPequeña):
        super().__init__(name, edad, color, peso, muerde)
        self.razaPequeña = razaPequeña

    def imprimir(self):
        super().imprimir()
        print("Tamaño: Pequeño")
        print(f"Raza: {self.razaPequeña.value}")