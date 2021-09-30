import MySQLdb
class conexion:

    def conectar(query):
        host = "locahost"
        user = "root"
        db_name = "cadenaHotelera"

        info = [host, user, db_name]
    
        connection = MySQLdb.connect(*info)
        cursor = connection.cursor()       
        cursor.execute(query)      

        cursor.close()
        connection.close()

    def verHabitacionesDisponibles():
        pass



    