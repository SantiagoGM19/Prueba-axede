
import datetime as date
from Modelo import *


print("Bienvenido!!")



def MostrarHoteles():
    opcion = int(input("Ingrese la opcion: "))
    print("Seleccione Hotel")
    print("1 --> Barranquilla")
    print("2 --> Cali")
    print("3 --> Cartagena")
    print("4 --> Bogotá")
    return opcion

def mostrarFuncionalidades():
    print("1 --> Ver disponibilidad")
    print("2 --> Ver tarifas")
    print("3 --> Calcular tarifa")


opcion = MostrarHoteles()

while True:
    if(opcion == 1):
        hotel = Sede(33, 4)

    elif(opcion == 2):
        hotel = Sede(28, 6)

    elif(opcion == 3):
        hotel = Sede(11, 8)

    else:
        hotel = Sede(42, 6)

    opcion2 = str(input("¿esea volver al menú de hoteles? Sí:y No:n"))

    if(opcion2 == "y"):
        opcion = MostrarHoteles()
    else:
        print("Gracias por pensar en nosotros!")
        break
