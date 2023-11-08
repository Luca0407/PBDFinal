create database segoviaa_cajero;

create table cajero(
ID_cajero int not null auto_increment,
numero_serie int not null,
ubicacion varchar(30)
);

create table cuentas(  
ID_cuenta int not null auto_increment
);

create table usuarios(
ID_cuenta int,
ID_usuario int not null auto_increment,
numero_usuario int not null,
pass int not null,
saldo int,
primary key (ID_usuario)
);

create table dinero(
ID_cantidad_dinero int not null auto_increment,
denominacion varchar(6),
stock int, 
primary key (ID_cantidad_dinero)
);

create table operaciones(
ID_operaciones int not null auto_increment,
historial_opciones varchar(1),
ingresos_egresos int
);