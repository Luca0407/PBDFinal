create database segoviaa_cajero;

create table cajero(
ID_cajero int not null auto_increment,
numero_serie int not null,
ubicacion varchar(30),
primary key (ID_cajero)
);

create table cuentas(  
ID_cuenta int not null auto_increment,
ID_usuario int,
saldo int not null,
primary key (ID_cuenta)
);

create table usuarios(
ID_usuario int not null auto_increment,
numero_usuario int not null,
nombre_usuario varchar(15),
apellido_usuario varchar (15),
dni int not null,
provincia varchar (20),
localidad varchar(30),
direccion varchar(50),
pass int not null,
primary key (ID_usuario)
);

create table dinero(
ID_cantidad_dinero int not null auto_increment,
ID_cajero int,
denominacion varchar(6),
stock int,
primary key (ID_cantidad_dinero)
);

create table operaciones(
ID_operaciones int not null auto_increment,
ID_cajero int,
ID_cuenta int,
tiempo_ingresos_egresos datetime,
ingresos_egresos int,
primary key (ID_operaciones)
);

INSERT INTO cajero (numero_serie, ubicacion) 
VALUES
	('100', 'Calle 12, entre 9 y 11'),
    ('101', 'Calle 12, entre 13 y 15'),
	('102', 'Calle 11, entre 10 y 12');
    

INSERT INTO dinero (ID_cajero, denominacion, stock) 
VALUES
	#cajero 100
	('1', '100','355'),
    ('1', '200','425'),
	('1', '500','660'),
	('1', '1000','1135'),
	('1', '2000','680'),
    
    #cajero 101
    ('2', '100','425'),
    ('2', '200','310'),
    ('2', '500','550'),
    ('2', '1000','1050'),
    ('2', '2000','590'),
    
    #cajero 102
    ('3', '100','305'),
    ('3', '200','495'),
    ('3', '500','610'),
    ('3', '1000','1190'),
    ('3', '2000','775');