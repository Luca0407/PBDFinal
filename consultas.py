"""
#  Consulta 1
import mysql.connector
import random

num1 = random.randint(1000000000, 9999999999)
num2 = random.randint(1000000000, 9999999999)
num3 = random.randint(1000000000, 9999999999)
conexion = mysql.connector.connect(host="localhost", user="root", passwd="", database="segoviaa_cajero")
cajero = conexion.cursor()

sql = "INSERT INTO cajero (numero_serie, ubicacion) VALUES (%s, %s)"
val = [
 (f'{num1}', 'Calle 12, entre 9 y 11'),
 (f'{num2}', 'Calle 12, entre 13 y 15'),
 (f'{num3}', 'Calle 11, entre 10 y 12'),
]

cajero.executemany(sql, val)
conexion.commit()

cajero.close()
conexion.close()
"""


#  Consulta 2
import mysql.connector
import random


cantidad_billetes = []

for i in range(6):
    x = random.randint(300, 500)
    cantidad_billetes.append[x]

for i in range(9):
    pass


num3 = random.randint(1000000000, 9999999999)
conexion = mysql.connector.connect(host="localhost", user="root", passwd="", database="segoviaa_cajero")
cajero = conexion.cursor()

sql = "INSERT INTO cajero (numero_serie, ubicacion) VALUES (%s, %s)"
val = [
 (f'{num1}', 'Calle 12, entre 9 y 11'),
 (f'{num2}', 'Calle 12, entre 13 y 15'),
 (f'{num3}', 'Calle 11, entre 10 y 12'),
]

cajero.executemany(sql, val)
conexion.commit()

cajero.close()
conexion.close()

