from Inmuebles.Inmueble import Inmueble

class InmuebleVivienda(Inmueble):
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños):
        super().__init__(identificadorInmobiliario, area, direccion)
        self._numeroHabitaciones = numeroHabitaciones
        self._numeroBaños = numeroBaños

    def imprimir(self):
        super().imprimir()
        print(f"Número de habitaciones = {self._numeroHabitaciones}")
        print(f"Número de baños = {self._numeroBaños}")
        