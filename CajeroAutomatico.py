#  ---LIBRERIAS---
import pymysql as db
import time
from datetime import datetime as dt
#  Modulos en demo wipper: db manager, strings, users y getpath.


#  --- FUNCIONES DEL PROGRAMA ---
def inicio():
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
                time.sleep(0.3)


def operacion(cursor, usuario):
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
            case "a":
                consultar_saldo(cursor, usuario)

            case "b":
                retiro_dinero(cursor, usuario)

            case "c":
                deposito_efectivo(cursor, usuario)

            case "d":
                ultimas_operaciones(cursor, usuario)

            case "e":
                cursor.close()
                salir(0)
                break

            case other:
                print("\nOpción invalida")
                time.sleep(0.3)


#  --- FUNCIONES DE ACCION 1 ---
def ingresar(registro):
    checks = 0
    registro.execute("SELECT numero_usuario, pass FROM usuarios;")
    listado = registro.fetchall()

    num_user = input("\nNumero de usuario:\n> ")
    if num_user.isnumeric() and len(num_user) == 6:
        num_user = int(num_user)
        checks += 1
        
    password = input("\nIngrese una contraseña:\n> ")
    if password.isnumeric() and len(password) == 4:      
        password = int(password)
        checks += 1

    if checks == 2:
        userpass = (num_user, password)

        registro.execute("SELECT ID_usuarios FROM usuarios WHERE numero_usuario = %s;", (num_user,))
        id = registro.fetchone()

        for usuarios in listado:
            if usuarios == userpass:
                print("\n- - - Usuario valido - - -\n")
                time.sleep(0.5)

                operacion(registro, id[0])
                registro.close()
                break

        else:
            invalido(0)
            registro.close()

    else:
        invalido(0)
        registro.close()


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
        cliente.execute("INSERT INTO usuarios (numero_usuario, nombre_usuario, apellido_usuario, dni, provincia, localidad, direccion, pass) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (num, username, apellido, dni, provincia, localidad, direccion, password))
        conexion.commit()

        cliente.execute("SELECT ID_usuarios FROM usuarios WHERE numero_usuario = %s;", (num,))
        id = cliente.fetchone()

        cliente.execute("INSERT INTO cuentas (ID_usuarios, saldo) VALUES (%s, %s);", (id[0], '0'))
        conexion.commit()

        print("""- - - ¡Usuario registrado con exito! - - -
            ¡¡Bienvenido!!
            """)
        time.sleep(0.6)

    else:
        invalido(2)


#  --- FUNCIONES DE ACCION 2 ---
def consultar_saldo(saldo, user):
    saldo.execute("SELECT saldo FROM cuentas WHERE ID_usuarios = %s;", (user,))
    plata = saldo.fetchone()

    print(f"\nUsted tiene ${plata[0]} en su cuenta.")

    time.sleep(0.5)


def retiro_dinero(retiro, user):
    while True:
        opcion = input("""

- - - ¿Cuánto dinero desea retirar? - - -

a. $1.000
b. $5.000
c. $10.000
d. $20.000
e. Otro monto
f. Volver al menú anterior

> """)

        match opcion.lower():
            case "a":
                stock_cajero(retiro, 1000, user)
                time.sleep(0.2)
                
            case "b":
                stock_cajero(retiro, 5000, user)
                time.sleep(0.2)

            case "c":
                stock_cajero(retiro, 10000, user)
                time.sleep(0.2)

            case "d":
                stock_cajero(retiro, 20000, user)
                time.sleep(0.2)

            case "e":
                while True:
                    monto = input("\n¿Cuánto dinero quiere sacar?\n> ")
                    if monto.isnumeric() and int(monto) % 100 == 0 and int(monto) > 99:      
                        monto = int(monto)
                        stock_cajero(retiro, monto, user)
                        time.sleep(0.2)
                        break

                    else:
                        invalido(2)
                        break

            case "f":
                salir(2)
                break

            case other:
                print("\nOpción invalida.\n")
                time.sleep(0.3)


def deposito_efectivo(deposito, user):
    checks = 0
    saldo_total = 0

    while True:
        if checks == 0:

            cien = input("\n¿Cuantos billetes de $100 quiere depositar?\n\n> ")
            if cien.isnumeric() and int(cien) >= 0:
                cien = int(cien)

                deposito.execute("UPDATE dinero SET stock = stock + %s WHERE denominacion = 100;", (cien,))
                conexion.commit()

                saldo_cien = (100 * cien)
                checks += 1
                saldo_total += saldo_cien

            else:
                invalido(2)
                continue
        
        if checks == 1:
            doscien = input("\n¿Cuantos billetes de $200 quiere depositar?\n\n> ")
            if doscien.isnumeric() and int(doscien) >= 0:
                doscien = int(doscien)

                deposito.execute("UPDATE dinero SET stock = stock + %s WHERE denominacion = 200;", (doscien,))
                conexion.commit()

                saldo_doscien = (200 * doscien)
                checks += 1
                saldo_total += saldo_doscien

            else:
                invalido(2)
                continue

        if checks == 2:
            quinien = input("\n¿Cuantos billetes de $500 quiere depositar?\n\n> ")
            if quinien.isnumeric() and int(quinien) >= 0:
                quinien = int(quinien)

                deposito.execute("UPDATE dinero SET stock = stock + %s WHERE denominacion = 500;", (quinien,))
                conexion.commit()

                saldo_quinien = (500 * quinien)
                checks += 1
                saldo_total += saldo_quinien

            else:
                invalido(2)
                continue

        if checks == 3:
            mil = input("\n¿Cuantos billetes de $1000 quiere depositar?\n\n> ")
            if mil.isnumeric() and int(mil) >= 0:
                mil = int(mil)

                deposito.execute("UPDATE dinero SET stock = stock + %s WHERE denominacion = 1000;", (mil,))
                conexion.commit()

                saldo_mil = (1000 * mil)
                checks += 1
                saldo_total += saldo_mil

            else:
                invalido(2)
                continue

        if checks == 4:
            dosmil = input("\n¿Cuantos billetes de $2000 quiere depositar?\n\n> ")
            if dosmil.isnumeric() and int(dosmil) >= 0:
                dosmil = int(dosmil)

                deposito.execute("UPDATE dinero SET stock = stock + %s WHERE denominacion = 2000;", (dosmil,))
                conexion.commit()

                saldo_dosmil = (2000 * dosmil)
                checks += 1
                saldo_total += saldo_dosmil

                operaciones_deposito(deposito, user, saldo_total)
                break

            else:
                invalido(2)
                continue
    
    deposito.execute("UPDATE cuentas SET saldo = saldo + %s WHERE ID_usuarios = %s;", (saldo_total, user))
    conexion.commit()

    print(f"${saldo_total} fue agregado a su cuenta.")


def operaciones_retiro(operacion, user, monto):
    fecha = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    operacion.execute("""INSERT INTO operaciones (
                    ID_cuentas, tiempo_ingresos_egresos, ingresos_egresos )
                    VALUES (%s, %s, %s)""", (user, fecha, -monto))
    conexion.commit()


def operaciones_deposito(operacion, user,monto):
    fecha= dt.now().strftime('%Y-%m-%d %H:%M:%S')
    operacion.execute("""INSERT INTO operaciones (
                    ID_cuentas, tiempo_ingresos_egresos, ingresos_egresos)
                    VALUES (%s, %s, %s)""", (user, fecha, monto))
    conexion.commit()


def ultimas_operaciones(operacion, user):
    operacion.execute("""SELECT tiempo_ingresos_egresos, ingresos_egresos
                    FROM operaciones WHERE ID_cuentas = %s
                    ORDER BY tiempo_ingresos_egresos DESC LIMIT 10;""", (user,))
    ultimas_realizadas = operacion.fetchall()

    for timestamp, amount in ultimas_realizadas:
        formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        print(f"Fecha: {formatted_timestamp} | Monto: {amount}")
        time.sleep(0.1)



#  ---FUNCIONES_SALIDA---
def invalido(i):
    print("\n- - - Algo salió mal. - - -\n")
    time.sleep(0.2)

    mensajes_invalidos = [
        "- - - Regresando al Menu Principal - - -\n",
        "- - - Ya existe otro usuario registrado con ese dato en nuestra base de datos. - - -\n",
        "- - - Uno o más datos ingresados fueron inválidos. - - -\n"]
    
    print(mensajes_invalidos[i])
    time.sleep(0.4)


def salir(i):
    mensajes_cierre = ["\n- - - Cerrando Sesión - - -\n",
                    "\n- - - Gracias por usar nuestros servicios - - -",
                    "\n- - - Regresando al Menu Principal - - -\n"]

    print(mensajes_cierre[i])
    time.sleep(0.4)


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

        else:
            return True


def stock_cajero(retiro, dinero, usuario):
    def consultar_stock(denominacion):
        retiro.execute("SELECT stock FROM dinero WHERE denominacion = %s;", (denominacion,))
        resultado = retiro.fetchone()

        if resultado is not None:
            return resultado[0]
        else:
            print(f"No se encontró información para billetes de {denominacion}.")
            return 0

    def actualizar_stock(conexion, denominacion, cantidad):
        retiro.execute("""UPDATE dinero SET stock = %s WHERE
                    denominacion = %s;""", (cantidad, denominacion))
        conexion.commit()

    def realizar_retiro(conexion, retiro_solicitado):
        denominaciones = [2000, 1000, 500, 200, 100]
        billetes_utilizados = {}

        for denominacion in denominaciones:
            cantidad_necesaria = retiro_solicitado // denominacion
            stock_disponible = consultar_stock(denominacion)

            if cantidad_necesaria > 0 and stock_disponible >= cantidad_necesaria:
                nuevo_stock = stock_disponible - cantidad_necesaria

                actualizar_stock(conexion, denominacion, nuevo_stock)
                retiro_solicitado -= cantidad_necesaria * denominacion

                billetes_utilizados[denominacion] = cantidad_necesaria

            if retiro_solicitado == 0:
                print("Retiro exitoso.\n")
                time.sleep(0.3)
                print("Denominaciones y cantidad de billetes utilizados\n")
                retiro.execute("UPDATE cuentas SET saldo = saldo - %s WHERE ID_usuarios = %s;", (dinero, usuario))
                conexion.commit()
                operaciones_retiro(retiro, usuario, dinero)

                for denominacion, cantidad in billetes_utilizados.items():
                    print(f"${denominacion}: {cantidad} billetes")
                    time.sleep(0.1)
                break
        else:
            invalido(2)

    retiro.execute("SELECT saldo FROM cuentas WHERE ID_usuarios = %s;", (usuario,))
    saldo_suficiente = retiro.fetchone()

    if saldo_suficiente[0] >= dinero:
        realizar_retiro(conexion, dinero)
    else:
        print(f"Saldo insuficiente para realizar el retiro ({saldo_suficiente[0]}).")
        return 0

#  --- INGRESO DINAMICO DE DATOS PARA WORKBENCH ---
print("Ingrese los valores requeridos o presione enter sin escribir nada para usar valores por defecto (local)\n\n")
time.sleep(0.5)

hst = input("Host: ")
if hst.strip() == "":
    hst = "localhost"

usr = input("\nNombre de usuario en MySQL Workbench: ")
if usr.strip() == "":
    usr = "root"

pwd = input("\nContraseña: ")

while True:
    dbname = input("\nNombre de la base de datos (obligatorio): ")
    if dbname.strip() != "":
        break
    else:
        print("Es obligatorio que rellene este campo.")

#  --- LLAMADA Y CONEXIÓN ---
conexion = db.connect(host=hst, user=usr, passwd=pwd.strip(), database=dbname)
inicio()
conexion.close()
