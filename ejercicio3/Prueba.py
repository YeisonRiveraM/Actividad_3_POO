from TiendaMascotas.Pequeño import *
from TiendaMascotas.PeloLargo import *

def main():
    mascota1 = Pequeño("Pacho", 10, "Cafe", 5, True, razaPequeña.CHIHUAHUA)
    mascota1.imprimir()
    mascota1.sonido()
    print()

    mascota2 = PeloLargo("Wendy", 3, "Blanco", 100, 158, razaLargo.SOMALI)
    mascota2.imprimir()
    mascota2.sonido()
    print()

if __name__ == "__main__":
    main()