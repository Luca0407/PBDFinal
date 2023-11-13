import mysql.connector
import random
import time

def inicio():
    while True:
        opcion = input("\n- - - Menu Principal - - -\na. Ingresar\nb. Crear nuevo cliente\nc. Salir\n\n> ")

        match opcion.lower():
            case "a":
                registro = conexion.cursor()

                num = input("\nNumero de usuario:\n")
                
                if num.isnumeric():

                    num = int(num)

                    password = input("\nIngrese una contraseña:\n")

                    if password.isnumeric():      

                        password = int(password)  

                        query = f"SELECT numero_usuario, pass FROM usuarios;"
                        registro.execute(query)
                
                for i in registro:
                    if i[0] == num and i[1] == password:
                        print("\n- - - Usuario valido - - -")
                        operacion(num)
                        
                print("\n- - - Datos Invalidos - - -\n")
                time.sleep(0.5)
                print("\n- - - Regresando al Menu Principal - - -\n")
                time.sleep(1)

            case "b":
                cursor1=conexion.cursor()

                num = input("\nIngrese un Numero de usuario de 6 digitos:\n")

                if num.isnumeric() and len(num) == 6:

                    num = int(num)

                    password = input("\nIngrese una contraseña de 4 digitos:\n")

                    if password.isnumeric() and len(password) == 4:

                        password = int(password)
                
                        query = f"INSERT INTO usuarios (numero_usuario, pass) VALUES ('{num}', '{password}');"
                        cursor1.execute(query)
                        cursor1.fetchall
                        conexion.commit()
                        cursor1.execute("SELECT * FROM usuarios;")

                        print("\n- - - Usuario registrado con exito - - -")
                        time.sleep(1)

                        for i in cursor1: # BORRAR AL FINAL (muestra datos de otros clientes)
                            print(i)
                            
                        cursor1.close()
                        print("")

                    else:
                        print("\n- - - Datos Invalidos - - -\n")
                        time.sleep(0.5)
                        print("\n- - - Regresando al Menu Principal - - -\n")
                        time.sleep(1)

                else:
                    print("\n- - - Datos Invalidos - - -\n")
                    time.sleep(0.5)
                    print("\n- - - Regresando al Menu Principal - - -\n")
                    time.sleep(1)

            case "c":
                break

            case other:
                print("\nOpción invalida")


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
                
                print(f"Usted tiene ${saldo} en su cuenta")  # Corregir. No imprime.

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
