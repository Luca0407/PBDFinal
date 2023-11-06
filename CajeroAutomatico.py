import random


def inicio():
    while True:
        opcion = input("a. Ingresar\nb. Crear nuevo cliente\nc. Salir\n")

        match opcion.lower():
            case "a":
                operacion()

            case "b":
                print("registra :v")
                break

            case "c":
                break


def operacion():
    while True:
        opcion = input(
            "a. Consulta de saldo\nb. Retiro de dinero\nc. Deposito de efectivo\nd. Consultar últimas 10 operaciones\ne. Volver\n"
            )

        match opcion.lower():
            case "a":
                print("0 peso tu tiene")
                break

            case "b":
                print("0 peso tu tiene")
                break

            case "c":
                print("0 peso tu tiene")
                break

            case "d":
                print("nosewe :V")
                break

            case "e":
                break

inicio()