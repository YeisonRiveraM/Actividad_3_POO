from Inmuebles.CasaUrbana import CasaUrbana

class CasaIndependiente(CasaUrbana):
    valorArea = 3000000
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos)

    def imprimir(self):
        super().imprimir()
        print()