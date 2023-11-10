import mysql.connector
import random


def inicio():
    while True:
        opcion = input("a. Ingresar\nb. Crear nuevo cliente\nc. Salir\n")

        match opcion.lower():
            case "a":
                operacion()

            case "b":
                conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", database="segoviaa_cajero")
                cursor1=conexion1.cursor()
                num = int(input("Numero de usuario\n"))
                query = f"INSERT INTO usuarios (numero_usuario) VALUES ('{num}');"
                c = cursor1.execute(query)
                cod = cursor1.fetchall
                conexion1.commit()
                query = "SELECT * FROM usuarios;"
                #  Aca va un for.
                cursor1.close()
                conexion1.close()
                break

            case "c":
                break

            case other:
                print("\nOpción invalida\n")


def operacion():
    while True:
        opcion = input(
            """
a. Consulta de saldo
b. Retiro de dinero
c. Deposito de efectivo
d. Consultar últimas 10 operaciones
e. Volver
""")

        match opcion.lower():
            case "a":
                print("\n0 peso tu tiene")

            case "b":
                print("\n0 peso tu tiene")

            case "c":
                print("\n0 peso tu tiene")

            case "d":
                print("\nnosewe :V")

            case "e":
                print("")
                break

            case other:
                print("\nOpción invalida")


inicio()
