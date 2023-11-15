#  ---LIBRERIAS---
import mysql.connector
import random
import time


#  ---FUNCIONES_PROGRAMA---
def inicio(curs, vuelta):  #  "inicio()" funcional. Falta arreglar bugs.
    while True:
        opcion = input("""
                       - - - Menu Principal - - -
a. Ingresar
b. Crear nuevo cliente
c. Salir

> """)

        match opcion.lower():
            case "a":  #  bugueado.
                if vuelta == 0:
                    query = f"SELECT numero_usuario, pass FROM usuarios;"
                    curs.execute(query)
                
                vuelta += 1
                ingresar(curs)

            case "b":  #  funcional.
                crear_cliente(curs)

            case "c":  #  funcional.
                salir()
                break

            case other:  #  funcional.
                print("\nOpción invalida\n")


def operacion(cursors):  #  "operacion()" en proceso. Faltan opcion "b", "c" y "d".
    while True:
        opcion = input(
            """
            - - - Menu de Tramites - - -
a. Consulta de saldo
b. Retiro de dinero
c. Deposito de efectivo
d. Consultar últimas 10 operaciones
e. Volver

> """)

        match opcion.lower():
            case "a":  #  funcional pero incompleto.
                consultar_saldo(cursors)

            case "b":
                print("\nEn proceso")

            case "c":
                print("\nEn proceso")

            case "d":
                print("\nEn proceso")

            case "e":  #  por ahora funcional.
                salir()
                break

            case other:  #  funcional.
                print("\nOpción invalida")

#  ---FUNCIONES_ACCION---
def ingresar(registro):  #  bugueado.
    userpass = ()
    num = input("\nNumero de usuario:\n")

    if num.isnumeric():
        num = int(num)
        for i in registro:
            print(i[0])

    password = input("\nIngrese una contraseña:\n")

    if password.isnumeric():      
        password = int(password)
        for i in registro:
            if password == i:
                print("pass")
                i = i[0]
                break
            else:
                print("no")
        
        print("\n- - - Usuario valido - - -")
        operacion(registro)      


def crear_cliente(cliente):  #  funcional.
    num = input("\nIngrese un Numero de usuario de 6 digitos:\n")
    if num.isnumeric() and len(num) == 6:
        num = int(num)

    password = input("\nIngrese una contraseña de 4 digitos:\n")
    if password.isnumeric() and len(password) == 4:
        password = int(password)
                
        query = f"INSERT INTO usuarios (numero_usuario, pass) VALUES ('{num}', '{password}');"
        cliente.execute(query)
        cliente.fetchall
        conexion.commit()
        cliente.execute("SELECT * FROM usuarios;")

        print("\n- - - Usuario registrado con exito - - -")
        time.sleep(1)

        for i in cliente:  #  DEBUG (borrar al final).
            print(i)
                            
        print("")


def consultar_saldo(saldo):
    saldo.execute(f"SELECT saldo FROM cuentas;")
                
    for i in saldo:
        print(f"Usted tiene ${i[0]} en su cuenta")


def invalido():
    print("\n- - - Datos Invalidos - - -\n")
    time.sleep(0.5)
    print("\n- - - Regresando al Menu Principal - - -\n")
    time.sleep(1)


def salir():  #  funcional.
    print("escribi un mensaje de cierre @SegoviaAgustin\n")

#  ---VARIABLES GLOBALES---
count = 0

#  ---LLAMADA Y CIERRE DE LA CONEXIÓN---
conexion=mysql.connector.connect(host="localhost", user="root", passwd="", database="segoviaa_cajero")
cursor = conexion.cursor()
inicio(cursor, count)
cursor.close()
conexion.close()
