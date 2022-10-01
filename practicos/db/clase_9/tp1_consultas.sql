CREATE DATABASE test; -- 1) Creo BD

USE test; -- Elijo BD para trabajar

-- 2) creo las tablas de la BD

CREATE TABLE clientes (
    id_cliente int(8),
    nombre varchar(50),
    apellido varchar(50),
    id_domicilio int(8),
    id_ciudad int(8),
    id_provincia int(2),
    id_pais int(3));
    
CREATE TABLE domicilios (
    id_domicilio int(8),
    calle varchar(100),
    altura int(5),
    barrio varchar(100),
    id_ciudad int(8),
    id_provincia int(2),
    id_pais int(3));
    
CREATE TABLE ciudades (
    id_ciudad int(8),
    nombre varchar(100),
    id_provincia int(2),
    id_pais int(3));
   
CREATE TABLE provincias (
    id_provincia int(2),
    nombre varchar(100),
    id_pais int(3));
    
CREATE TABLE paises (
    id_pais int(3),
    nombre varchar(100));

-- 3) Defino AI y PK 

ALTER TABLE clientes
    CHANGE `id_cliente` `id_cliente` INT(8) NOT NULL AUTO_INCREMENT, 
    ADD PRIMARY KEY(id_cliente);
ALTER TABLE domicilios
    CHANGE `id_domicilio` `id_domicilio` INT(8) NOT NULL AUTO_INCREMENT, 
    ADD PRIMARY KEY(id_domicilio);
ALTER TABLE ciudades
    CHANGE `id_ciudad` `id_ciudad` INT(8) NOT NULL AUTO_INCREMENT,
    ADD PRIMARY KEY(id_ciudad);
ALTER TABLE provincias
    CHANGE `id_provincia` `id_provincia` INT(2) NOT NULL AUTO_INCREMENT,
    ADD PRIMARY KEY(id_provincia);
ALTER TABLE paises
    CHANGE `id_pais` `id_pais` INT(3) NOT NULL AUTO_INCREMENT, 
    ADD PRIMARY KEY (id_pais);

-- Defino FK

ALTER TABLE provincias
    ADD FOREIGN KEY (id_pais) REFERENCES paises(id_pais);
ALTER TABLE ciudades
    ADD FOREIGN KEY (id_provincia) REFERENCES provincias(id_provincia);
ALTER TABLE domicilios
    ADD FOREIGN KEY (id_provincia) REFERENCES provincias(id_provincia), 
    ADD FOREIGN KEY (id_ciudad) REFERENCES ciudades(id_ciudad);
    ADD FOREIGN KEY (id_pais) REFERENCES paises(id_pais);

ALTER TABLE clientes
    ADD FOREIGN KEY (id_domicilio) REFERENCES domicilios(id_domicilio), 
    ADD FOREIGN KEY (id_ciudad) REFERENCES ciudades(id_ciudad), 
    ADD FOREIGN KEY (id_provincia) REFERENCES provincias(id_provincia);


-- 4) Inserto registros
-- Paises
INSERT INTO paises (id_pais, nombre) VALUES (null,'Argentina');
INSERT INTO paises VALUES (null,'Brasil');
INSERT INTO paises VALUES (null,'Uruguay');
INSERT INTO paises VALUES (null,'Chile');
INSERT INTO paises VALUES (null,'Colombia');

-- Provincias
INSERT INTO provincias (id_provincia, nombre, id_pais)
VALUES (null,'Córdoba',1);
INSERT INTO provincias VALUES (null,'San Luis',1);
INSERT INTO provincias VALUES (null,'La Pampa',1);
INSERT INTO provincias VALUES (null,'Buenos Aires',1);
INSERT INTO provincias VALUES (null,'Montevideo',3);

-- Ciudades
INSERT INTO ciudades (id_ciudad, nombre, id_provincia)
VALUES (null,'Colonia Caroya',1);
INSERT INTO ciudades VALUES (null,'Merlo',2);
INSERT INTO ciudades VALUES (null,'Santa Rosa',3);
INSERT INTO ciudades VALUES (null,'La Plata',4);
INSERT INTO ciudades VALUES (null,'La Calera',1);

-- Domicilios
INSERT INTO domicilios (id_domicilio, calle, altura, barrio, id_ciudad, id_provincia, id_pais) 
VALUES (null, 'Avenida Siempre Viva', 742, 'Lomas de Springield', 1, 1, 1);
INSERT INTO domicilios VALUES (null, 'Baker Street', 221, 'Westminster', 4, 4, 1);
INSERT INTO domicilios VALUES (null, 'Privet Drive', 4, 'Little Whinging', 5, 1, 1);
INSERT INTO domicilios VALUES (null, 'Grimmauld Place', 12, 'Islington', 3, 3, 1);
INSERT INTO domicilios VALUES (null, 'Spooner', 31, 'Quahog', 2, 2, 1);

-- Clientes
INSERT INTO clientes (id_cliente, nombre, apellido, id_domicilio, id_ciudad, id_provincia, id_pais) 
VALUES (null,'Homero','Simpson',1, 1, 1, 1);
INSERT INTO clientes VALUES (null,'Sherlock','Holmes', 2, 4, 4, 1);
INSERT INTO clientes VALUES (null,'Vernon','Dursley', 3, 5, 1, 1);
INSERT INTO clientes VALUES (null,'Sirius','Black', 4, 3, 3, 1);
INSERT INTO clientes VALUES (null,'Stewart','Griffin', 5, 2, 2, 1);

-- 5) Modifico Registros
-- Paises
UPDATE paises SET nombre = 'República Argentina' WHERE id_pais = 1;
UPDATE paises SET nombre = 'República Federativa de Brasil' WHERE id_pais = 2;
UPDATE paises SET nombre = 'República Oriental del Uruguay' WHERE id_pais = 3;

-- Provincias
UPDATE provincias SET nombre = 'Provincia de San Luis' WHERE id_provincia = 3;
UPDATE provincias SET nombre = 'Provincia de Buenos Aires' WHERE id_provincia = 4;
UPDATE provincias SET nombre = 'Departamento de Montevideo' WHERE id_provincia = 5;

-- Ciudades
UPDATE ciudades SET nombre = 'Ciudad de Colonia Caroya' WHERE id_ciudad = 1;
UPDATE ciudades SET nombre = 'Ciudad de Santa Rosa' WHERE id_ciudad = 3;
UPDATE ciudades SET nombre = 'Ciudad de La Calera' WHERE id_ciudad = 5;

-- Domicilios
UPDATE domicilios SET calle = 'Evergreen Terrace' WHERE id_domicilio = 1;
UPDATE domicilios SET calle = 'Baker' WHERE id_domicilio = 2;
UPDATE domicilios SET id_ciudad = 2, id_provincia = 2 WHERE id_domicilio = 4;

-- Clientes
UPDATE clientes SET nombre = 'Lisa' WHERE id_cliente = 1;
UPDATE clientes SET apellido = 'Black III' WHERE id_cliente = 4;
UPDATE clientes SET nombre = 'Stewie' WHERE id_cliente = 5;

-- 6) Elimino Registros
-- Paises
DELETE FROM paises WHERE id_pais = 4;

-- Provincias
DELETE FROM provincias WHERE nombre = 'Departamento de Montevideo';

-- Clientes
DELETE FROM clientes WHERE id_cliente = 4;

-- Domicilios
DELETE FROM domicilios WHERE barrio = 'Islington';

-- Ciudades
DELETE FROM ciudades WHERE id_ciudad = 3;

-- 7) Sentencia SELECT que lista a los clientes
SELECT id_cliente, nombre, apellido FROM clientes;

-- 8) Sentencia SELECT con condicion WHERE
SELECT nombre FROM ciudades WHERE id_provincia=1;

--9) Sentencia SELECT con FROM de 2 tablas
-- SELECT: Elijo los campos a trabajar
SELECT clientes.id_cliente, clientes.nombre, clientes.apellido, domicilios.calle, domicilios.altura, domicilios.barrio
-- FROM: Elijo una tabla
FROM clientes
INNER JOIN domicilios -- Elijo la otra tabla 
ON clientes.id_domicilio=domicilios.id_domicilio; -- Determino el criterio con el que se van a mostrar los registros
-- Es decir: Mostrar solo los campos determinados en SELECT cuando el id_domicilio de la tabla clientes sea igual al
-- id_domicilio de la tabla domicilios

--10) Sentencia SELECT con solo descripciones
SELECT nombre FROM paises 