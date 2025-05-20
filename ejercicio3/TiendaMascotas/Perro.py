from TiendaMascotas.Mascota import Mascota

class Perro(Mascota):

    @staticmethod
    def sonido():
        print(f"Los perros ladran")

    def __init__(self, name, edad, color, peso, muerde):
        super().__init__(name, edad, color)
        self.peso = peso
        self.muerde = muerde

    def imprimir(self):
        super().imprimir()
        print(f"Peso: {self.peso} kilos")
        if self.muerde == True:
            print("Muerde: Si")
        else:
            print("Muerde: No")
    