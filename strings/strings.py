def general():
    general_strings = ["a", "b", "c", "d", "e",
                    "\nOpción invalida\n", "\n- - - Algo salió mal. - - -\n", "- - - Regresando al Menu Principal - - -\n", "- - - Ya existe otro usuario registrado con ese dato en nuestra base de datos. - - -\n",
                    "- - - Uno o más datos ingresados fueron inválidos. - - -\n", "\n- - - Cerrando Sesión - - -\n", "\n- - - Gracias por usar nuestros servicios - - -",
                    "\n- - - Regresando al Menu Principal - - -\n"]
    return general_strings

def queries():
    app_queries = [  #1
                    "SELECT numero_usuario, pass FROM usuarios;",
                    # 2
                    "SELECT ID_usuarios FROM usuarios WHERE numero_usuario = '",
                    # 3
                    "INSERT INTO usuarios (numero_usuario, nombre_usuario, apellido_usuario, dni, provincia, localidad, direccion, pass) VALUES ('",
                    # 4
                    "INSERT INTO cuentas (ID_usuarios, saldo) VALUES ('",
                    # 5
                    "SELECT saldo FROM cuentas WHERE ID_usuarios = '",
                    # 6
                    "UPDATE dinero SET stock = stock + '",
                    # 7
                    "SELECT numero_usuario FROM usuarios;",
                    # 8
                    "SELECT dni FROM usuarios;",
                    # 9
                    "SELECT pass FROM usuarios;",
                    # 10
                    "SELECT stock FROM dinero WHERE denominacion = %s;"
                    # 11
                    "UPDATE dinero SET stock = %s WHERE denominacion = %s;"
                    # 12
                    "UPDATE cuentas SET saldo = saldo - "
                    # 13
                    "SELECT saldo FROM cuentas WHERE ID_usuarios = '"
                    ]
    return app_queries

def funciones():
    programa_strings = ["\n- - - Menu Principal - - -\n\na. Ingresar\nb. Crear nuevo cliente\nc. Salir\n\n> ",
                    "\n- - - Menu de Tramites - - -\n\na. Consulta de saldo\nb. Retiro de dinero\nc. Deposito de efectivo\nd. Consultar últimas 10 operaciones\ne. Volver\n\n> "]
    return programa_strings

def ingresar():
    ingresar_strings = ["\nNumero de usuario:\n> ", "\nIngrese una contraseña:\n> ", "\n- - - Usuario valido - - -\n"]
    return ingresar_strings

def cliente():
    cliente_strings = ["\nIngrese un número de usuario de 6 digitos:\n> ", "\nIngrese su nombre:\n> ", "\nIngrese su apellido:\n> ", "\nIngrese su DNI:\n> ", "\nIngrese su provincia:\n> ",
                    "\nIngrese su localidad:\n> ", "\nIngrese su dirección:\n> ", "\nIngrese una contraseña de 4 digitos:\n> ", "- - - ¡Usuario registrado con exito! - - -\n¡¡Bienvenido!!\n\n"]
    return cliente_strings

def retiro():
    retiro_strings = ["\n\n- - - ¿Cuánto dinero desea retirar? - - -\n\na. $1.000\nb. $5.000\nc. $10.000\nd. $20.000\ne. Otro monto\nf. Volver al menú anterior\n\n> ",
                    "\n¿Cuánto dinero quiere sacar?\n> "]
    return retiro_strings

def deposito():
    deposito_strings = ["\n¿Cuantos billetes de", "quiere depositar?\n\n> ", " fue agregado a su cuenta."]
    return deposito_strings

def operaciones():
    operaciones_strings = ["%Y-%m-%d %H:%M:%S", "Fecha: ", " | Monto: "]
    return operaciones_strings

def stock():
    stock_strings = ["No se encontró información para billetes de ", "Retiro exitoso.\n", "Denominaciones y cantidad de billetes utilizados\n", "Saldo insuficiente para realizar el retiro "]
    return stock_strings

def db():
    db_strings = ["Ingrese los valores requeridos o presione enter sin escribir nada para usar valores por defecto (local)\n\n", "Host: ", "localhost", "\nNombre de usuario en MySQL Workbench: ",
                "root", "\nContraseña: ", "\nNombre de la base de datos (obligatorio): ", "Es obligatorio que rellene este campo."]
    return db_strings