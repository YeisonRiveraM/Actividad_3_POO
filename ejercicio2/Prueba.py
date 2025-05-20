from Inmuebles.ApartamentoFamiliar import ApartamentoFamiliar
from Inmuebles.Apartaestudio import Apartaestudio

def main():
    apto1 = ApartamentoFamiliar(103067, 120, "Avenida Santander 45-45", 3, 2, 200000)
    print(">>>Datos del apartamento<<<")
    apto1.calcularPrecioVenta(apto1.valorArea)
    apto1.imprimir()

    apto2 = Apartaestudio(12354, 50, "Avenida Caracas 30-15", 1, 1)
    print(">>>Datos del apartamento<<<")
    apto2.calcularPrecioVenta(apto2.valorArea)
    apto2.imprimir()

if __name__ == "__main__":
    main()