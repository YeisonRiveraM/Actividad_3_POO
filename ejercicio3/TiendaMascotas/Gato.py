from TiendaMascotas.Mascota import Mascota

class Gato(Mascota):

    @staticmethod
    def sonido():
        print(f"Los gatos maúllan y ronronean")

    def __init__(self, name, edad, color, altSalto, longSalto):
        super().__init__(name, edad, color)
        self.altSalto = altSalto
        self.longSalto = longSalto

    def imprimir(self):
        super().imprimir()
        print(f"Altura de salto: {self.altSalto} cm")
        print(f"Longitud de salto: {self.longSalto} cm")