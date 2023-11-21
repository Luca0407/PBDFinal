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
                time.sleep(0.4)


def operacion(cursor, usuario):  #  "operacion()" en proceso. Faltan opcion "b", "c" y "d".
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
                consultar_saldo(cursor, usuario)

            case "b":
                retiro_dinero(cursor, usuario)

            case "c":
                deposito_efectivo(cursor, usuario)

            case "d":
                ultimas_operaciones(cursor, usuario)

            case "e":  #  HECHO.
                cursor.close()
                salir(0)
                break

            case other:  #  HECHO.
                print("\nOpción invalida")
                time.sleep(0.4)


#  ---FUNCIONES_ACCION_1---
def ingresar(registro):
    checks = 0
    registro.execute("SELECT numero_usuario, pass FROM usuarios;")
    listado = registro.fetchall()
    
    num_user = input("\nNumero de usuario:\n> ")
    if num_user.isnumeric():
        num_user = int(num_user)
        checks += 1
        
    password = input("\nIngrese una contraseña:\n> ")
    if password.isnumeric():      
        password = int(password)
        checks += 1
        
    if checks == 2:
        userpass = (num_user, password)

        registro.execute(f"SELECT ID_usuario FROM usuarios WHERE numero_usuario = '{num_user}';")
        id = registro.fetchone()

        for i in listado:
            if i == userpass:
                print("\n- - - Usuario valido - - -")

                operacion(registro, id)
                registro.close()
                break
        
        else:
            invalido(0)

    else:
        invalido(0)


def crear_cliente(cliente):
    checks = 0

    while True:
        if checks == 0:
            num = input("\nIngrese un número de usuario de 6 digitos:\n> ")

            if num.isnumeric() and len(num) == 6:
                num = int(num)
                
                if usuario_existente(num, cliente) == True:
                    invalido(1)
                    continue
                
                checks += 1
        
        if checks == 1:
            username = input("\nIngrese su nombre:\n> ")
            if username.isalpha():
                checks += 1

        if checks == 2:
            apellido = input("\nIngrese su apellido:\n> ")
            if apellido.isalpha():
                checks += 1

        if checks == 3:
            dni = input("\nIngrese su DNI:\n> ")
            if dni.isnumeric() and len(dni) == 8:
                dni = int(dni)
                checks += 1
        
        if checks == 4:
            provincia = input("\nIngrese su provincia:\n> ")
            if all(x.isalpha() or x.isspace() for x in provincia):
                checks += 1

        if checks == 5:
            localidad = input("\nIngrese su localidad:\n> ")
            if all(x.isalpha() or x.isspace() for x in localidad):
                checks += 1

        if checks == 6:
            direccion = input("\nIngrese su dirección:\n> ")
            checks += 1

        if checks == 7:
            password = input("\nIngrese una contraseña de 4 digitos:\n> ")
            if password.isnumeric() and len(password) == 4:
                password = int(password)

                if usuario_existente(password, cliente) == True:
                    invalido(1)
                    continue

                checks += 1
                break

            else:
                invalido(2)
        
        else:
            invalido(2)
    
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
        conexion.commit()

        cliente.execute(f"SELECT ID_usuario FROM usuarios WHERE numero_usuario = '{num}'")
        id = cliente.fetchone()

        cliente.execute(f"INSERT INTO cuentas (ID_usuario, saldo) VALUES ('{id[0]}', '1000'); ")
        conexion.commit()

        print("""- - - ¡Usuario registrado con exito! - - -
            ¡¡Bienvenido!!
            """)
        time.sleep(1)       
        print("")

    else:
        invalido(2)


#  ---FUNCIONES_ACCION_2---
def consultar_saldo(saldo, user):  #  HECHO creo.
    saldo.execute(f"SELECT saldo FROM cuentas WHERE ID_usuario = '{user[0]}';")
    plata = saldo.fetchone()

    print(f"\nUsted tiene ${plata[0]} en su cuenta.")
    saldo.close()
    
    time.sleep(1)


def retiro_dinero():
    pass


def deposito_efectivo(deposito, user):
    while True:
        checks = 0
        cien = input("\n¿Cuantos billetes de $100 quiere depositar?\n\n> ")
        if cien.isnumeric() and int(cien) >= 0:
            cien = int(cien)
            checks += 1
            

        doscien = input("\n¿Cuantos billetes de $200 quiere depositar?\n\n> ")
        if doscien.isnumeric() and int(doscien) >= 0:
            doscien = int(doscien)
            checks += 1

        quinien = input("\n¿Cuantos billetes de $500 quiere depositar?\n\n> ")
        if quinien.isnumeric() and int(quinien) >= 0:
            quinien = int(quinien)
            checks += 1

        mil = input("\n¿Cuantos billetes de $1000 quiere depositar?\n\n> ")
        if mil.isnumeric() and int(mil) >= 0:
            mil = int(mil)
            checks += 1

        dosmil = input("\n¿Cuantos billetes de $2000 quiere depositar?\n\n> ")
        if dosmil.isnumeric() and int(dosmil) >= 0:
            dosmil = int(dosmil)
            checks += 1

        if checks == 5:
            print("ok")
            break

        else:
            invalido(2)


def ultimas_operaciones(operacion, user):
    operacion.execute(f"SELECT ID_cajero, ID_cuenta, tiempo_ingresos_egresos, ingresos_egresos")


#  ---FUNCIONES_SALIDA---
def invalido(i):
    print("\n- - - Algo salió mal. - - -\n")
    time.sleep(0.5)

    mensajes_invalidos = [
        "- - - Regresando al Menu Principal - - -\n",
        "- - - Ya existe otro usuario registrado con ese dato en nuestra base de datos. - - -\n",
        "- - - Uno o más datos ingresados fueron inválidos. - - -\n"]
    
    print(mensajes_invalidos[i])
    time.sleep(1)


def salir(i):
    mensajes_cierre = ["\n- - - Cerrando Sesión - - -\n", "\n- - - Gracias por usar nuestros servicios - - -"]

    print(mensajes_cierre[i])
    time.sleep(0.8)


#  ---FUNCIONES_CHEQUEO---
def usuario_existente(dato, checking):
    while True:
        if len(str(dato)) == 6:
            checking.execute("SELECT numero_usuario FROM usuarios;")
            data = checking.fetchall()
            
            for i in data:
                if dato == i[0]:
                    return True
                else:
                    continue
            else:
                break
        
        elif len(str(dato)) == 8:
            checking.execute("SELECT dni FROM usuarios;")
            data = checking.fetchall()
            
            for i in data:
                if dato == i[0]:
                    return True
                else:
                    continue
            else:
                break
        
        elif len(str(dato)) == 4:
            checking.execute("SELECT pass FROM usuarios;")
            data = checking.fetchall()
            
            for i in data:
                if dato == i[0]:
                    return True
                else:
                    continue
            else:
                break


#  ---LLAMADA Y CIERRE DE LA CONEXIÓN---
conexion=mysql.connector.connect(host="localhost", user="root", passwd="", database="segoviaa_cajero")
inicio()
conexion.close()
