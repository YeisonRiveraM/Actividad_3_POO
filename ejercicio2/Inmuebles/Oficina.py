from Inmuebles.Local import Local

class Oficina(Local):
    valorArea = 3500000
    def __init__(self, identificadorInmobiliario, area, direccion, tipoLocal, esGobierno):
        super().__init__(identificadorInmobiliario, area, direccion, tipoLocal)
        self._esGobierno = esGobierno

    def imprimir(self):
        super().imprimir()
        print(f"Es oficina gubernamental: {self._esGobierno}")
        
    