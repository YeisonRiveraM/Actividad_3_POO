from Inmuebles.Local import Local

class LocalComercial(Local):
    valorArea = 3000000
    def __init__(self, identificadorInmobiliario, area, direccion, tipoLocal, centroComercial):
        super().__init__(identificadorInmobiliario, area, direccion, tipoLocal)
        self._centroComercial = centroComercial

    def imprimir(self):
        super().imprimir()
        print(f"Centro comercial: {self._centroComercial}")