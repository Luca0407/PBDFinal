create database segoviaa_cajero;

create table usuarios(
ID_usuario int not null auto_increment,
numero_usuario int not null,
contraseña int not null,
saldo int,
primary key (ID_usuario)
);

create table dinero(
ID_cantidad_dinero int not null auto_increment,
denominacion varchar(6), #$2.000 - $1.000...
stock int, 
primary key (ID_cantidad_dinero)
);

create table usuarios_dinero(
ID_usuario int,
ID_cantidad_dinero int,
operaciones int ########################
);