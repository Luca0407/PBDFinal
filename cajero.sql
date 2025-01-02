create database elizondol_cajero;

create table cuentas(
ID_cuentas int not null auto_increment,
ID_usuarios int,
saldo int not null,
primary key (ID_cuentas)
);

create table usuarios(
ID_usuarios int not null auto_increment,
numero_usuario int not null,
nombre_usuario varchar(15),
apellido_usuario varchar (15),
dni int not null,
provincia varchar (20),
localidad varchar(30),
direccion varchar(50),
pass int not null,
primary key (ID_usuarios)
);

create table dinero(
ID_dinero int not null auto_increment,
denominacion varchar(6),
stock int,
primary key (ID_dinero)
);

create table operaciones(
ID_operaciones int not null auto_increment,
ID_cuentas int,
tiempo_ingresos_egresos datetime,
ingresos_egresos int,
primary key (ID_operaciones)
);

INSERT INTO dinero (denominacion, stock)
VALUES
	('100','355'),
    ('200','425'),
	('500','660'),
	('1000','1135'),
	('2000','680');