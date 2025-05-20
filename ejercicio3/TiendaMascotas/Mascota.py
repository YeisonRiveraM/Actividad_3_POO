class Mascota:
    def __init__(self, name, edad, color):
        self.name = name
        self.edad = edad
        self.color = color
    def imprimir(self):
        print(">>>Mascota<<<")
        print(f"Nombre: {self.name}") 
        print(f"Edad: {self.edad} años")
        print(f"Color: {self.color}")