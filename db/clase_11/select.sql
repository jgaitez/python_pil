-- Sentencia Select
-- Tres partes principales
    -- SELECT: Campos a mostrar. Si quiero mostrar todo: "*".
                -- Varios campos se separan con coma.
                -- No solamente se pueden mostrar campos de la tabla.
                -- Se pueden mostrar resultados de operaciones
    -- FROM: Tabla a elegir
    -- WHERE: Condicion a cumplir. Si quiero concatenar otra
    -- condicion uso "AND" y "OR"
    -- Cuando quiero igualar puedo usar "=" o "LIKE" (para texto)
    SELECT id_provincia, id_pais, nombre
    FROM provincias_full
    WHERE id_provincia = 10 OR id_provincia = 18
    AND nombre LIKE "Catamarca"

-- Funcion IN: Permite listar una secuencia de condiciones. Ej.:
    SELECT id_provincia, id_pais, nombre
    FROM provincias_full
    WHERE id_provincia IN (10, 18)
-- Tambien existe NOT IN para excluir los valores de la secuencia
-- Tambien existe <>  para mostrar registros que no coincidan con esas
-- condiciones
-- ORDER BY: Establece el campo que va a servir para ordenar la vista
-- de los registros. El parametro ASC lista los resultados de mayor a
-- menor (o alfabeticamente) y DESC lo contrario

    SELECT nombre, id_departamento, id_provincia
    FROM ciudades_full
    WHERE id_provincia IN (6, 10)
    ORDER BY ciudades_full.id_provincia DESC
-- Se puede usar el nombre de columna o su lugar en la tabla.
    SELECT nombre, id_departamento, id_provincia
    FROM ciudades_full
    ORDER BY 4 ASC
-- Se pueden usar varios criterios para ordenar la vista
    ORDER BY 4, id_departamento ASC

-- Alias: Se pueden renombrar las columnas (para modificar el nombre
-- que se vea en la vista)escribiendo primero el nombre real y luego
-- el alias o usando el comando "as".

SELECT nombre AS Nombre_Ciudad
SELECT nombre Nombre_Ciudad

-- %: En LIKE el signo % sirve como comodin en SELECT. 
-- %TERMINO% busca todos los registros que dentro contengan "Termino"
-- %TERMINO busca todos los registros que terminen con "Termino"
-- TERMINO% busca todos los registros que empiecen con "Termino"

    WHERE nombre LIKE "Villa%"

-- BETWEEN: Permite filtrar por rango de valores (incluyendolos)

    WHERE id_pais BETWEEN 1 and 5


-- JOIN: Permite definir la relacion entre 2 tablas. Se usa en el 
-- FROM. Ademas necesita de ON para cotejar las semejanzas.
    -- INNER JOIN: Solo lo que las tablas comparten
    -- LEFT JOIN: Lo que tenga la primer tabla y que ademas este en la
    -- segunda
    -- RIGHT JOIN: Lo que tenga la segunda tabla y que ademas este en la
    -- primera
-- La primer lista a mostrar es la primera tabla que se nombre en la 
-- sentencia

SELECT c.nombre "Nombre de la Ciudad", p.nombre "Nombre de la provincia"
FROM ciudades_full c INNER JOIN provincias_full p 
ON c.id_provincia = p.id_provincia;

-- Otra forma de hacer el JOIN es:

SELECT c.nombre "Nombre de la Ciudad", p.nombre "Nombre de la provincia"
FROM ciudades_full c, provincias_full p 
WHERE c.id_provincia = p.id_provincia;


-- COUNT: Operador que muestra el total de registros de acuerdo a la 
-- condicion. Tambien existe sum() y avg() que suma y promedia los 
-- valores que estan dentro de sus parentesis respectivamente.

SELECT p.id_provincia, p.nombre, -- Mostrar el id_provincia y su nombre
COUNT(c.id_ciudad) Ciudades -- Mostrar ademas el total de registros 
FROM ciudades c, provincias p  -- Entre las tablas Ciudades y Provincias
WHERE c.id_provincia = p.id_provincia -- Siempre y cuando el id_provincia
-- de la tabla ciudad y la tabla provincia sean iguales
GROUP BY p.id_provincia, p.nombre -- Distribuir por id_provincia y su nombre

-- HAVING: Permite establecerle condiciones a COUNT

SELECT p.id_provincia, p.nombre, -- Mostrar el id_provincia y su nombre
COUNT(c.id_ciudad) Ciudades -- Mostrar ademas el total de registros 
FROM ciudades c, provincias p  -- Entre las tablas Ciudades y Provincias
WHERE c.id_provincia = p.id_provincia -- Siempre y cuando el id_provincia
-- de la tabla ciudad y la tabla provincia sean iguales
GROUP BY p.id_provincia, p.nombre -- Distribuir por id_provincia y su nombre
HAVING COUNT(c.id_ciudad) < 2; -- Mostrar solo los resultados menores a 2.

SELECT *
FROM domicilios sum(domicilios.altura)


