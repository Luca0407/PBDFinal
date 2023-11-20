import mysql.connector

def input_defecto(mensaje,valor):
    aux = input(mensaje+ "({}): ".format(valor))
    if aux == '':
        return valor
    else:
        return aux

def modifica_rubro(conexion,cursor):
    cursor.execute("select * from rubros")
    registros = cursor.fetchall()

    for (codigo, descrip, id) in registros:
        print(codigo, descrip, id)

    id_a_modificar = input("Ingrese la ID del rubro a modificar: ")
    cod_actual, desc_actual = "", ""
    encontrado = False
    for (codigo, descrip, id) in registros:
        if id == int(id_a_modificar):
            cod_actual, desc_actual = codigo, descrip
            encontrado = True
    if encontrado:
        descrip = input_defecto("Ingrese la nueva descripción", desc_actual)
        codigo = input_defecto("Ingrese al nuevo código",cod_actual)
        cursor.execute(f"""UPDATE rubros 
                            SET des_rub = '{descrip}', cod_rub = '{codigo}' 
                            WHERE idrubros = '{id_a_modificar}';""")
        conexion.commit()
    else:
        print("No se encontró el ID ingresado.")

def alta_rubro(conexion,cursor):
    nombre = input_defecto("Ingrese el nombre rubro ","")
    codigo = input_defecto("Ingrese el código ","99")
    cursor.execute(f"insert into rubros (des_rub,cod_rub) values ('{nombre}','{codigo}')")
    conexion.commit()

def menu_rubro():
    while True:
        print("""        MENU RUBROS
        ------------------------
        1- Agregar nuevo rubro
        2- Modificar nuevo rubro
        3- Borrar un rubro
        4- Listar los rubros
        0- Salir""")
        opc = input("Ingrese la opción:")
        if opc == "1":
            alta_rubro(conexion1, cursor1)
        elif opc == "2":
            modifica_rubro(conexion1, cursor1)
        elif opc == "0":
            break
        else:
            print("Ingrese una opción correcta")

conexion1 = mysql.connector.connect(host="localhost",
                                   user="root",
                                   passwd = "",
                                   database = "pruebabd")

cursor1 = conexion1.cursor()
menu_rubro()
conexion1.close()



