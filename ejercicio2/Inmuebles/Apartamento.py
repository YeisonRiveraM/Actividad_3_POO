from Inmuebles.InmuebleVivienda import InmuebleVivienda

class Apartamento(InmuebleVivienda):
    def __init__(self, identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños):
        super().__init__(identificadorInmobiliario, area, direccion, numeroHabitaciones, numeroBaños)
    
    def imprimir(self):
        super().imprimir()
