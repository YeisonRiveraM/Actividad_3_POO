class Inmueble:
    def __init__(self, identificadorInmobiliario, area, direccion):
        self._identificadorInmobiliario = identificadorInmobiliario
        self._area = area
        self._direccion = direccion
        self._precioVenta = 0
    def calcularPrecioVenta(self, valorArea):
        self._precioVenta = self._area * valorArea
        return self._precioVenta
    def imprimir(self):
        print(f"Identificador inmobiliario = {self._identificadorInmobiliario}")
        print(f"Área = {self._area}")
        print(f"Dirección = {self._direccion}")
        print(f"Precio de venta = {self._precioVenta}")
        