from Inmuebles.Apartamento import Apartamento

class Apartaestudio(Apartamento):
    valorArea = 1500000
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños):
        super().__init__(identificadorInmobiliario, area, direccion, 1, 1)

    def imprimir(self):
        super().imprimir()
        print()