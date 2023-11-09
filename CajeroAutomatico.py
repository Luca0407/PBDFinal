import mysql.connector
import random


def inicio():
    while True:
        opcion = input("a. Ingresar\nb. Crear nuevo cliente\nc. Salir\n")

        match opcion.lower():
            case "a":
                operacion()

            case "b":
                user = input("usuario de workbench:\n")
                contra = input("contraseña de workbench:\n")
                conexion1=mysql.connector.connect(host="127.0.0.1", user=f"{user}",
                passwd=f"{contra}")
                cursor1=conexion1.cursor()
                cursor1.execute("show databases")
                for base in cursor1:
                    print(base)
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
