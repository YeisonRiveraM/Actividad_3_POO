from Inmuebles.Apartamento import Apartamento

class ApartamentoFamiliar(Apartamento):
    valorArea = 2000000
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños, valorAdministracion):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños)
        self._valorAdministracion = valorAdministracion

    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración: ${self._valorAdministracion}")
        print()
