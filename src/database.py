import mysql.connector

try:
    database = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='usuarios'
    )
    print("Conexión exitosa a la base de datos")
except mysql.connector.Error as error:
    print("Error al conectarse a la base de datos: {}".format(error))
