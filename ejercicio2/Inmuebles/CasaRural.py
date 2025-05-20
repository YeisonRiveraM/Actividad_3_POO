from Inmuebles.Casa import Casa

class CasaRural(Casa):
    valorArea = 1500000
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos, distanciaCabera, altitud):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos)
        self._distanciaCabera = distanciaCabera
        self.altitud = altitud

    def imprimir(self):
        super().imprimir()
        print(f"Distancia a la cabecera municipal = {self._distanciaCabera} km")
        print(f"Altitud sobre el nivel del mar = {self.altitud} metros")
        print()