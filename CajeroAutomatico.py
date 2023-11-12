import mysql.connector
import random


def inicio():
    while True:
        opcion = input("a. Ingresar\nb. Crear nuevo cliente\nc. Salir\n")

        match opcion.lower():
            case "a":
                registro = conexion.cursor()

                num = int(input("Numero de usuario\n"))
                password = int(input("Ingrese una contraseña de 4 digitos\n"))

                query = f"SELECT numero_usuario, pass FROM usuarios;"
                registro.execute(query)
                
                for i in registro:
                    if i[0] == num and i[1] == password:
                        print("Usuario valido!")
                        operacion(num)
                        
                print("\nnuh huh\n")

            case "b":
                cursor1=conexion.cursor()

                num = int(input("Numero de usuario\n"))
                password = int(input("Ingrese una contraseña de 4 digitos\n"))
                
                query = f"INSERT INTO usuarios (numero_usuario, pass, saldo) VALUES ('{num}', '{password}', '0');"
                cursor1.execute(query)
                cursor1.fetchall
                conexion.commit()
                cursor1.execute("SELECT * FROM usuarios;")

                for i in cursor1:
                    print(i)
                    
                cursor1.close()
                print("")

            case "c":
                break

            case other:
                print("\nOpción invalida\n")


def operacion(usuario):
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
                saldo = conexion.cursor()

                quero = f"SELECT saldo FROM usuarios WHERE numero_usuario = '{usuario}';"
                saldo.execute(quero)
                
                print(f"Usted tiene ${saldo} en su cuenta")  # Corregir. No imprime el saldo como número.

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

conexion=mysql.connector.connect(host="localhost", user="root", passwd="", database="segoviaa_cajero")
inicio()
conexion.close()
