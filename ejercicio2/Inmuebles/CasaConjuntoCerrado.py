from Inmuebles.CasaUrbana import CasaUrbana

class CasaConjuntoCerrado(CasaUrbana):
    valorArea = 2500000
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos, valorAdministracion, tienePiscina, tieneCamposDeportivos):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, numeroPisos)
        self._valorAdministracion = valorAdministracion
        self._tienePiscina = tienePiscina
        self._tieneCamposDeportivos = tieneCamposDeportivos

    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración: ${self._valorAdministracion}")
        print(f"Tiene {self._tienePiscina} piscinas")
        print(f"Tiene {self._tieneCamposDeportivos} campos deportivos")
        print()