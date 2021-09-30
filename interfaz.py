
import datetime as date
from Modelo import *
from conexion import *


print("Bienvenido!!")



def MostrarHoteles():
    print("Seleccione Hotel")
    print("1 --> Barranquilla")
    print("2 --> Cali")
    print("3 --> Cartagena")
    print("4 --> Bogotá")
    opcion = int(input("Ingrese la opcion: "))
    return opcion

def mostrarFuncionalidades(hotel):
    print("1 --> Ver disponibilidad")
    print("2 --> Ver tarifas")
    print("3 --> Calcular tarifa")
    opcion = int(input("Ingrese opcion: "))
    
    if(opcion == 1):
        if(hotel.ciudad == "barranquilla"):
            habitacionesDisponibles = conexion.verHabitacionesDisponibles()
            pass
        elif(hotel.ciudad == "cali"):
            pass
        elif(hotel.ciudad == "cartagena"):
            pass
        else:
            pass

    elif(opcion == 2):
        pass
    elif(opcion == 3):
        pass



opcion = MostrarHoteles()

while True:
    if(opcion == 1):
        hotel = Sede(33, 4, "barranquilla")

    elif(opcion == 2):
        hotel = Sede(28, 6, "cali")

    elif(opcion == 3):
        hotel = Sede(11, 8, "cartagena")

    else:
        hotel = Sede(42, 6, "bogota")

    mostrarFuncionalidades(hotel)

    opcion2 = str(input("¿esea volver al menú de hoteles? Sí:y No:n"))

    if(opcion2 == "y"):
        opcion = MostrarHoteles()
    else:
        print("Gracias por pensar en nosotros!")
        break
