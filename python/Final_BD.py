import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host='localhost',
        database='test',
        user='root',
        port='3306',
        password = ''
    )
    print("conectado")

except Error as e:

    print("Error al conectar")