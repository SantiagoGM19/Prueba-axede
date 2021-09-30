class Sede:
    def __init__(self, cupoMax, numeroHabitaciones, ciudad):
        self.cupoMaximo = cupoMax
        self.numeroHabitciones = numeroHabitaciones
        # estado --> True: disponible, False: No disponible
        self.estado = True
        self.tarifas = []
        self.ciudad = ciudad

    def verDisponibilidad(self):
        return self.estado
    
    def verTarifas(self):
        return self.tarifas
    
    def verNumeroPersonas(self):
        return self.cupoMaximo
    
    def agregarTarifas(self, habitacion):
        tarifa = habitacion.calcularTarifa()
        self.tarifa.append(tarifa)
    
    def eliminarTarifa():
        pass

class Habitacion:
    def __init__(self, valorEstandar, numeroPersonas):
        #Temporada --> 1:Alta, 0:Baja
        self.temporada = 1
        self.valor = valorEstandar
        self.tipoAlojamiento = 0
        self.numeroPersonas = numeroPersonas
        self.estado = True
    
    def precioTemporada(self, incremento):
        if(self.temporada == 1):
            self.valor = self.valor - self.valor*incremento
        else:
            self.valor = self.valor - self.valor*incremento

    def calcularTarifa(self):
        self.valor = self.valor*self.numeroPersonas

    def modificarTemporada(self):
        if(self.temporada == 1):
            self.temporada = 0
        else:
            self.temporada = 1

    def verDisponibilidad(self):
        return self.estado
