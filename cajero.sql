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
numero int not null,
saldo int not null,
primary key (ID_cuenta)
);

create table usuarios(
ID_usuario int not null auto_increment,
numero_usuario int not null,
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
ID_usuario int,
ID_cuenta int,
historial_opciones varchar(1),
historial_tiempo_opciones datetime,
ingresos_egresos int,
primary key (ID_operaciones)
);