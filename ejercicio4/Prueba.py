from Universidad.Estudiante import Estudiante
from Universidad.Profesor import Profesor

def main():
    persona1 = Estudiante("Mery", "Calle f 24-76", "Ingeniería agrícola", 8)
    print(">>>ESTUDIANTE<<<")
    print(f"Nombre: {persona1.nombre}")
    print(f"Direccion: {persona1.direccion}")
    print(f"Carrera: {persona1.carrera}")
    print(f"Semestre: {persona1.semestre}")
    persona1.carrera = "Licenciatura en español"
    persona1.semestre = 1
    persona1.direccion = "Diagonal ty 535-6"
    print()
    print(">>>ESTUDIANTE MODIFICADO<<<")
    print(f"Nombre: {persona1.nombre}")
    print(f"Direccion: {persona1.direccion}")
    print(f"Carrera: {persona1.carrera}")
    print(f"Semestre: {persona1.semestre}")

    print()
    print()

    persona2 = Profesor("Gerardo", "Avenida Gilberto Colon 45-6700", "Química", "Investigador")
    print(">>>PROFESOR<<<")
    print(f"Nombre: {persona2.nombre}")
    print(f"Direccion: {persona2.direccion}")
    print(f"Departamento: {persona2.departamento}")
    print(f"Categoría: {persona2.categoria}")
    persona2.nombre = "Pedro"
    persona2.categoria = "Jefe"
    print()
    print(">>>PROFESOR MODIFICADO<<<")
    print(f"Nombre: {persona2.nombre}")
    print(f"Direccion: {persona2.direccion}")
    print(f"Departamento: {persona2.departamento}")
    print(f"Categoría: {persona2.categoria}")

if __name__ == "__main__":
    main()