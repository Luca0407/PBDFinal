#  ---LIBRERIAS---
import mysql.connector
import random
import time


#  ---FUNCIONES_PROGRAMA---
def inicio():  #  "inicio()" HECHO.
    while True:
        cursor = conexion.cursor()
        opcion = input("""
- - - Menu Principal - - -
                       
a. Ingresar
b. Crear nuevo cliente
c. Salir

> """)
        match opcion.lower():
            case "a":
                ingresar(cursor)

            case "b":
                crear_cliente(cursor)

            case "c":
                salir(1)
                cursor.close()
                break

            case other:
                print("\nOpción invalida\n")


def operacion(usuario):  #  "operacion()" en proceso. Faltan opcion "b", "c" y "d".
    while True:
        cursor = conexion.cursor()
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
                consultar_saldo(cursor, usuario)

            case "b":
                print("\nEn proceso")

            case "c":
                print("\nEn proceso")

            case "d":
                print("\nEn proceso")

            case "e":  #  HECHO.
                cursor.close()
                salir(0)
                break

            case other:  #  HECHO.
                print("\nOpción invalida")


#  ---FUNCIONES_ACCION---
def ingresar(registro):
    checks = 0
    registro.execute(f"SELECT numero_usuario, pass FROM usuarios;")
    listado = registro.fetchall()
    
    id = input("\nNumero de usuario:\n> ")
    if id.isnumeric():
        id = int(id)
        checks += 1
        
    password = input("\nIngrese una contraseña:\n> ")
    if password.isnumeric():      
        password = int(password)
        checks += 1
        
    if checks == 2:
        userpass = (id, password)

        for i in listado:
            if i == userpass:
                print("\n- - - Usuario valido - - -")
                operacion(id)
                registro.close()
                break
        
        else:
            invalido()

    else:
        invalido()


def crear_cliente(cliente):
    checks = 0

    num = input("\nIngrese un número de usuario de 6 digitos:\n> ")
    if num.isnumeric() and len(num) == 6:
        num = int(num)
        checks += 1

    username = input("\nIngrese su nombre:\n> ")
    if username.isalpha():
        checks += 1

    apellido = input("\nIngrese su apellido:\n> ")
    if apellido.isalpha():
        checks += 1

    dni = input("\nIngrese su DNI:\n> ")
    if dni.isnumeric() and len(dni) == 8:
        dni = int(dni)
        checks += 1

    provincia = input("\nIngrese su provincia:\n> ")
    if all(x.isalpha() or x.isspace() for x in provincia):
        checks += 1
    
    localidad = input("\nIngrese su localidad:\n> ")
    if all(x.isalpha() or x.isspace() for x in localidad):
        checks += 1
    
    direccion = input("\nIngrese su dirección:\n> ")
    checks += 1
    
    password = input("\nIngrese una contraseña de 4 digitos:\n> ")
    if password.isnumeric() and len(password) == 4:
        password = int(password)
        checks += 1
    
    if checks == 8:
        cliente.execute(f""" INSERT INTO usuarios (
            numero_usuario,
            nombre_usuario,
            apellido_usuario,
            dni,
            provincia,
            localidad,
            direccion,
            pass ) VALUES (
                '{num}',
                '{username}',
                '{apellido}',
                '{dni}',
                '{provincia}',
                '{localidad}',
                '{direccion}',
                '{password}' ); """)
        
        cliente.fetchall
        conexion.commit()
        cliente.execute(f"""INSERT INTO cuentas (
                        ID_usuario,
                        saldo ) VALUES (
                            '{num}',
                            '0' ); """)
        cliente.fetchall
        conexion.commit()

        print("""- - - ¡Usuario registrado con exito! - - -
                 ¡¡Bienvenido!!
            """)
        time.sleep(1)       
        print("")
    
    else:
        invalido()


def consultar_saldo(saldo, user):  #  HECHO creo.
    saldo.execute(f"SELECT saldo FROM cuentas WHERE ID_usuario = '{user}';")
    plata = saldo.fetchone()

    print(f"\nUsted tiene ${plata[0]} en su cuenta.")
    saldo.close()
    time.sleep(1)


def retiro_dinero():
    pass


def deposito_efectivo():
    pass


def ultimas_operaciones():
    pass


#  ---FUNCIONES_SALIDA---
def invalido():
    print("\n- - - Datos Invalidos - - -\n")
    time.sleep(0.5)
    print("- - - Regresando al Menu Principal - - -\n")
    time.sleep(1)


def salir(i):
    mensajes_cierre = ["\n- - - Cerrando Sesión - - -\n", "\n- - - Gracias por usar nuestros servicios - - -"]
    print(mensajes_cierre[i])
    time.sleep(1)


#  ---LLAMADA Y CIERRE DE LA CONEXIÓN---
conexion=mysql.connector.connect(host="localhost", user="root", passwd="", database="segoviaa_cajero")
inicio()
conexion.close()
