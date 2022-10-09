CREATE DATABASE test; -- 1) Creo BD

USE test; -- Elijo BD para trabajar

-- 2) creo las tablas de la BD

CREATE TABLE CLIENTES (
    id_cliente int(8),
    nombre varchar(50),
    apellido varchar(50),
    id_domicilio int(8));

    
CREATE TABLE DOMICILIOS (
    id_domicilio int(8),
    calle varchar(100),
    altura int(5),
    barrio varchar(100),
    id_ciudad int(8));

    
CREATE TABLE CIUDADES (
    id_ciudad int(8),
    nombre varchar(100),
    id_provincia int(2));
   
CREATE TABLE PROVINCIAS (
    id_provincia int(2),
    nombre varchar(100),
    id_pais int(3));
    
CREATE TABLE PAISES (
    id_pais int(3),
    nombre varchar(100));

-- 3) Defino AI y PK 

ALTER TABLE CLIENTES
    CHANGE `id_cliente` `id_cliente` INT(8) NOT NULL AUTO_INCREMENT, 
    ADD PRIMARY KEY(id_cliente);
ALTER TABLE DOMICILIOS
    CHANGE `id_domicilio` `id_domicilio` INT(8) NOT NULL AUTO_INCREMENT, 
    ADD PRIMARY KEY(id_domicilio);
ALTER TABLE CIUDADES
    CHANGE `id_ciudad` `id_ciudad` INT(8) NOT NULL AUTO_INCREMENT,
    ADD PRIMARY KEY(id_ciudad);
ALTER TABLE PROVINCIAS
    CHANGE `id_provincia` `id_provincia` INT(2) NOT NULL AUTO_INCREMENT,
    ADD PRIMARY KEY(id_provincia);
ALTER TABLE PAISES
    CHANGE `id_pais` `id_pais` INT(3) NOT NULL AUTO_INCREMENT, 
    ADD PRIMARY KEY (id_pais);

-- Defino FK

ALTER TABLE PROVINCIAS
    ADD FOREIGN KEY (id_pais) REFERENCES PAISES(id_pais);
ALTER TABLE CIUDADES
    ADD FOREIGN KEY (id_provincia) REFERENCES PROVINCIAS(id_provincia);
ALTER TABLE DOMICILIOS
    ADD FOREIGN KEY (id_ciudad) REFERENCES CIUDADES(id_ciudad);
ALTER TABLE CLIENTES
    ADD FOREIGN KEY (id_domicilio) REFERENCES DOMICILIOS(id_domicilio);

-- 4) Inserto registros
-- PAISES
INSERT INTO PAISES (id_pais, nombre) VALUES (null,'Argentina');
INSERT INTO PAISES VALUES (null,'Brasil');
INSERT INTO PAISES VALUES (null,'Uruguay');
INSERT INTO PAISES VALUES (null,'Chile');
INSERT INTO PAISES VALUES (null,'Colombia');

-- PROVINCIAS
INSERT INTO PROVINCIAS (id_provincia, nombre, id_pais)
VALUES (null,'Córdoba',1);
INSERT INTO PROVINCIAS VALUES (null,'San Luis',1);
INSERT INTO PROVINCIAS VALUES (null,'La Pampa',1);
INSERT INTO PROVINCIAS VALUES (null,'Buenos Aires',1);
INSERT INTO PROVINCIAS VALUES (null,'Montevideo',3);

-- CIUDADES
INSERT INTO CIUDADES (id_ciudad, nombre, id_provincia)
VALUES (null,'Colonia Caroya',1);
INSERT INTO CIUDADES VALUES (null,'Merlo',2);
INSERT INTO CIUDADES VALUES (null,'Santa Rosa',3);
INSERT INTO CIUDADES VALUES (null,'La Plata',4);
INSERT INTO CIUDADES VALUES (null,'La Calera',1);

-- Domicilios
INSERT INTO DOMICILIOS (id_domicilio, calle, altura, barrio, id_ciudad) 
VALUES (null, 'Avenida Siempre Viva', 742, 'Lomas de Springield', 1);
INSERT INTO DOMICILIOS VALUES (null, 'Baker Street', 221, 'Westminster', 4);
INSERT INTO DOMICILIOS VALUES (null, 'Privet Drive', 4, 'Little Whinging', 5);
INSERT INTO DOMICILIOS VALUES (null, 'Grimmauld Place', 12, 'Islington', 3);
INSERT INTO DOMICILIOS VALUES (null, 'Spooner', 31, 'Quahog', 2);

-- Clientes
INSERT INTO CLIENTES (id_cliente, nombre, apellido, id_domicilio) 
VALUES (null,'Homero','Simpson',1);
INSERT INTO CLIENTES VALUES (null,'Sherlock','Holmes', 2);
INSERT INTO CLIENTES VALUES (null,'Vernon','Dursley', 3);
INSERT INTO CLIENTES VALUES (null,'Sirius','Black', 4);
INSERT INTO CLIENTES VALUES (null,'Stewart','Griffin', 5);

-- 5) Modifico Registros
-- PAISES
UPDATE PAISES SET nombre = 'República Argentina' WHERE id_pais = 1;
UPDATE PAISES SET nombre = 'República Federativa de Brasil' WHERE id_pais = 2;
UPDATE PAISES SET nombre = 'República Oriental del Uruguay' WHERE id_pais = 3;

-- PROVINCIAS
UPDATE PROVINCIAS SET nombre = 'Provincia de San Luis' WHERE id_provincia = 3;
UPDATE PROVINCIAS SET nombre = 'Provincia de Buenos Aires' WHERE id_provincia = 4;
UPDATE PROVINCIAS SET nombre = 'Departamento de Montevideo' WHERE id_provincia = 5;

-- CIUDADES
UPDATE CIUDADES SET nombre = 'Ciudad de Colonia Caroya' WHERE id_ciudad = 1;
UPDATE CIUDADES SET nombre = 'Ciudad de Santa Rosa' WHERE id_ciudad = 3;
UPDATE CIUDADES SET nombre = 'Ciudad de La Calera' WHERE id_ciudad = 5;

-- Domicilios
UPDATE DOMICILIOS SET calle = 'Evergreen Terrace' WHERE id_domicilio = 1;
UPDATE DOMICILIOS SET calle = 'Baker' WHERE id_domicilio = 2;
UPDATE DOMICILIOS SET id_ciudad = 2 WHERE id_domicilio = 4;

-- Clientes
UPDATE CLIENTES SET nombre = 'Lisa' WHERE id_cliente = 1;
UPDATE CLIENTES SET apellido = 'Black III' WHERE id_cliente = 4;
UPDATE CLIENTES SET nombre = 'Stewie' WHERE id_cliente = 5;

-- 6) Elimino Registros
-- PAISES
DELETE FROM PAISES WHERE id_pais = 4;

-- PROVINCIAS
DELETE FROM PROVINCIAS WHERE nombre = 'Departamento de Montevideo';

-- Clientes
DELETE FROM CLIENTES WHERE id_cliente = 4;

-- Domicilios
DELETE FROM DOMICILIOS WHERE barrio = 'Islington';

-- CIUDADES
DELETE FROM CIUDADES WHERE id_ciudad = 3;

-- 7) Sentencia SELECT que lista a los CLIENTES
SELECT id_cliente, nombre, apellido FROM CLIENTES;

-- 8) Sentencia SELECT con condicion WHERE
SELECT nombre FROM CIUDADES WHERE id_provincia=1;

-- 9) Sentencia SELECT con FROM de 2 tablas
-- SELECT: Elijo los campos a trabajar
SELECT CLIENTES.id_cliente, CLIENTES.nombre, CLIENTES.apellido, DOMICILIOS.calle, DOMICILIOS.altura, DOMICILIOS.barrio
-- FROM: Elijo una tabla
FROM CLIENTES
INNER JOIN DOMICILIOS -- Elijo la otra tabla 
ON CLIENTES.id_domicilio=DOMICILIOS.id_domicilio; -- Determino el criterio con el que se van a mostrar los registros
-- Es decir: Mostrar solo los campos determinados en SELECT cuando el id_domicilio de la tabla CLIENTES sea igual al
-- id_domicilio de la tabla DOMICILIOS

-- 10) Sentencia SELECT con solo descripciones
SELECT nombre FROM PAISES 