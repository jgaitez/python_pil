-- Se necesita saber la siguiente informacion:
-- Todas las salidas del query deben contener descripciones, es decir si muestro una lista de productos
-- debo mostrar el id del producto y su nombre, ya que la salida SQL espera ser leida y mostrada al
-- usuario final.

-- 1) ¿Cuantos empleados tenemos registrados?

    SELECT COUNT(*) cantidad_empleados
    FROM `employees`;

-- 2) ¿Cuantos empleados hay en cada oficina?

    SELECT o.officeCode oficina_codigo, o.city oficina_lugar, COUNT(*) empleados_totales
    FROM employees e, offices o
    WHERE e.officeCode = o.officeCode
    GROUP BY e.officeCode, o.city;

-- 3) ¿Cuantos productos tenemos por linea?

    -- Sentencia Personal    
    SELECT l.productLine linea, COUNT(*) productos_totales
    FROM products p, productlines l 
    WHERE p.productLine = l.productLine 
    GROUP BY linea;
    -- Sentencia Profe
    SELECT p.productLine linea, COUNT(p.productCode) productos_totales
    FROM products p 
    GROUP BY linea;

-- 4) Listar los productos de la linea PLANES 

    SELECT p.productCode producto_codigo, p.productName producto_nombre, p.productLine producto_linea, p.productScale producto_escala, p.productVendor producto_fabricante, p.productDescription producto_descripcion, p.quantityInStock producto_stock, p.buyPrice producto_precio_compra, p.MSRP producto_precio_venta_sugerido
    FROM products p
    WHERE p.productLine = "Planes"; -- A mi me funciono "planes" tambien

-- 5) Listar solo los productos que vienen con logos oficiales

    SELECT p.productCode producto_codigo, p.productName producto_nombre, p.productLine producto_linea, p.productScale producto_escala, p.productVendor producto_fabricante, p.productDescription producto_descripcion, p.quantityInStock producto_stock, p.buyPrice producto_precio_compra, p.MSRP producto_precio_venta_sugerido 
    FROM products p 
    WHERE p.productDescription LIKE "%official logos%";

-- 6) ¿Todos los clientes son del mismo pais? Que paises?

    SELECT c.country listado_de_paises
    FROM customers c
    GROUP by c.country;

-- 7) ¿Cual fue el ultimo pago que se registro?

    -- Buscando por ultimo pago
        -- Mostrar solo datos del ultimo pago
        SELECT p.customerNumber cliente_numero, p.checkNumber recibo_numero, p.paymentDate fecha_pago, p.amount monto
        FROM payments p
        ORDER BY p.paymentDate DESC
        LIMIT 1; -- Limita el numero de registros/resultados a mostrar

        -- Mostrar ultimo pago y nombre del cliente que lo hizo
        SELECT p.customerNumber cliente_numero, c.customerName cliente_nombre, p.checkNumber recibo_numero, p.paymentDate fecha_pago, p.amount monto
        FROM payments p, customers c
        WHERE p.customerNumber = c.customerNumber
        ORDER BY p.paymentDate DESC
        LIMIT 1;

-- 8) ¿Cual fue el pago mas chico? (Con datos del cliente que lo hizo)

    SELECT p.customerNumber cliente_numero, c.customerName cliente_nombre, p.checkNumber recibo_numero, p.paymentDate fecha_pago, p.amount monto
    FROM payments p, customers c
    WHERE p.customerNumber = c.customerNumber
    ORDER BY p.amount ASC
    LIMIT 1;

-- 9) Listar los clientes que no tienen pagos

    -- Mostrar lo especificado en #76 de la tabla especificada en #77
    -- siempre y cuando no exista lo especificado en #78.
    SELECT c.customerNumber numero_cliente, c.customerName nombre_cliente
    FROM customers c
    WHERE NOT EXISTS (SELECT *
                    FROM payments p
                    WHERE p.customerNumber = c.customerNumber);
        -- Subconsulta: Mostrar todos los campos de la tabla payments
        -- siempre y cuando en el registro coincida el campo customerNumber
        -- de las tablas payments y customers

-- 10) ¿Cuanto se recaudo en los ultimos 6 meses?

    -- Tomando como tope del semestre la fecha de la ultima venta
        SELECT sum(p.amount) ventas_ultimo_semestre
        FROM payments p
        WHERE p.paymentDate
        -- Uso subconsultas para que sea la base de datos la que me determine
        -- la fecha y no ponerla "a mano".
        -- Uso max(p.paymentDate) para que la fecha tope la determine la
        -- bd y asi no calcular el total de ventas del ultimo semestre contando
        -- desde hoy.
        BETWEEN (
            SELECT adddate(max(p.paymentDate), INTERVAL -6 MONTH) 
            FROM payments p)
        AND (
            SELECT max(p.paymentDate)
            FROM payments p);
    
    -- Eligiendo mostrar el primer semestre del año
        SELECT SUM(p.amount) ventas_semestre_1
        FROM payments p
        WHERE p.paymentDate BETWEEN "2005-01-01" AND "2005-06-30";

-- 11) ¿Cual es el producto mas vendido?

    -- Caso de ejemplo: Yo tengo un negocio en donde vendo semanalmente 
    -- 10 veces el art "A" (en distintas cantidades). A su vez tengo el 
    -- art "B" del cual vendo ocasionalmente muchas unidades (que superan
    -- las unidades vendidas del art "A")

    -- Para identificar producto que es el presente en mas ventas
    SELECT o.productCode codigo_producto, p.productName nombre_producto, count(o.productCode) veces_vendido
    FROM orderdetails o, products p
    WHERE o.productCode = p.productCode
    GROUP BY o.productCode, p.productName
    ORDER BY count(o.productCode) DESC
    LIMIT 1;

    -- Para identificar producto  que es el que tiene la mayor cantidad
    -- de unidades vendidas sin importar las veces que fue vendido

    SELECT o.productCode codigo_producto, p.productName nombre_producto, sum(o.quantityOrdered) unidades_vendidas
    FROM orderdetails o, products p
    WHERE o.productCode = p.productCode
    GROUP BY o.productCode, p.productName
    ORDER BY sum(o.quantityOrdered) DESC
    LIMIT 1;

-- 12) ¿Cual les son los 10 mejores clientes?

    -- Criterio: Limite de credito:
    SELECT c.customerNumber codigo_cliente, c.customerName nombre_cliente, c.creditLimit limite_credito_cliente
    FROM customers c
    ORDER BY c.creditLimit DESC
    LIMIT 10;

    -- Criterio: Clientes que compraron mas veces:
    SELECT c.customerNumber codigo_cliente, c.customerName nombre_cliente, count(o.customerNumber) ventas_realizadas
    FROM orders o, customers c
    WHERE c.customerNumber = o.customerNumber
    GROUP BY c.customerNumber, c.customerName  
    ORDER BY count(o.customerNumber) DESC
    LIMIT 10;
    
    -- Criterio: Clientes que compraron mas cantidades de articulos:

    SELECT c.customerNumber codigo_cliente, c.customerName nombre_cliente, sum(d.quantityOrdered) total_articulos_llevados
    FROM orders o, customers c, orderdetails d
    WHERE o.customerNumber=c.customerNumber and o.orderNumber=d.orderNumber
    GROUP BY c.customerNumber  
    ORDER BY sum(d.quantityOrdered) DESC
    LIMIT 10;

    -- Criterio: Clientes que gastaron mas dinero
    SELECT c.customerNumber codigo_cliente, c.customerName nombre_cliente, sum(p.amount) total_monto_ventas
    FROM payments p, customers c
    WHERE c.customerNumber = p.customerNumber
    GROUP BY c.customerNumber, c.customerName  
    ORDER BY count(p.amount) DESC
    LIMIT 10;

-- 13 ¿Cada cuanto tiempo regresa un cliente?
    -- No encontre una consulta para responder adecuamente esta pregunta
    -- Lo que hice fue hacer una consulta que liste a los clientes, y
    -- que a la diferencia de dias entre la primera vez que compro y la
    -- última la divida en la cantidad de veces que compro.

    SELECT c.customerNumber cliente_codigo, c.customerName cliente_nombre, (datediff(max(o.orderDate), min(o.orderDate)) / COUNT(o.orderNumber)) promedio_regreso_dias
    FROM orders o, customers c
    WHERE o.customerNumber = c.customerNumber -- Aca no pude agregar 
    -- ninguna condicion para excluir 0 como resultado (el cliente 415
    -- compro solo una vez, por lo que no se puede promediar). Probe
    -- "(datediff(max(o.orderDate), min(o.orderDate))" y "COUNT(o.orderNumber)"
    -- mayores a 0 (por separado)
    GROUP BY c.customerName  
    ORDER BY (datediff(max(o.orderDate), min(o.orderDate)) / COUNT(o.orderNumber)) ASC;

-- 14 ¿Cuantos clientes no tienen registrado su telefono?

    SELECT COUNT(phone) clientes_sin_telefono FROM customers WHERE phone is null;

-- 15 ¿Quienes son?
    SELECT * FROM customers WHERE phone is null;  -- La consulta no arroja resultados

-- 16 Listar los productos mas vendidos en el ultimo mes registrado y su precio

    SELECT d.productCode producto_codigo, p.productName producto_nombre, sum(d.quantityOrdered) productos_vendidos, max(d.priceEach) precio_maximo, min(d.priceEach) precio_minimo, AVG(d.priceEach) precio_promedio
        FROM orderdetails d, orders o, products p
        WHERE (o.orderDate BETWEEN (
                    SELECT adddate(max(o.orderDate), INTERVAL -1 MONTH) 
                    FROM orders o)
                AND (
                    SELECT max(o.orderDate)
                    FROM orders o)) and d.productCode = p.productCode AND d.orderNumber = o.orderNumber
    GROUP BY d.productCode, p.productName
    ORDER BY `productos_vendidos` DESC;

-- 17 ¿Quien es el jefe de cada departamento ?
 
    SELECT concat(firstName, " ", lastName) jefe_nombre, jobTitle jefe_cargo 
    FROM `employees`
    WHERE jobTitle LIKE "%manager%";

-- 18 ¿Cual es el empleado que mas vende?

    SELECT e.employeeNumber empleado_numero, concat(e.firstName, " ", e.lastName) empleado_nombre, SUM(p.amount) empleado_ventas
    FROM payments p, customers c, employees e
    WHERE c.customerNumber = p.customerNumber AND e.employeeNumber = c.salesRepEmployeeNumber
    GROUP by e.employeenumber  
    ORDER BY SUM(p.amount) DESC
    LIMIT 1;