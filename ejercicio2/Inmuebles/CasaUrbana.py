from Inmuebles.Casa import Casa

class CasaUrbana(Casa):
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos)

    def imprimir(self):
        return super().imprimir()