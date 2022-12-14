/*Table creation*/

CREATE TABLE category(
    categoryname VARCHAR(10),
    categoryKey INT PRIMARY KEY
);

CREATE TABLE product(
    productKey INT PRIMARY KEY,
    productname VARCHAR(20),
    price INT,
    quantity INT,
    categoryKey INT,
    CONSTRAINT fk_category
        FOREIGN KEY(categoryKey)
            REFERENCES category(categoryKey)
);


CREATE TABLE test_purchase(
    id SERIAL,
    customerKey INT,
    product VARCHAR(20),
    quantity INT
);


--obtain a certain number of letters from the word
SELECT SUBSTR(productname,1,3)
FROM product
LIMIT 5;

--adding an extra column to the table
ALTER TABLE test_purchase
ADD COLUMN pk INT;

--converting the extra column into a foreign key
ALTER TABLE test_purchase
ADD FOREIGN KEY(pK)
REFERENCES product(productkey);


SELECT * FROM test_purchase;

INSERT INTO test_purchase(customerkey,product,quantity,pk)
VALUES
(23,'Egg',50,1),
(24,'Indomie',40,1);

/*Procedures*/
DROP PROCEDURE update_product;
CREATE PROCEDURE update_product(item VARCHAR(20))
LANGUAGE SQL
AS $$
UPDATE product
SET quantity = quantity - (SELECT quantity FROM test_purchase WHERE product = item)
WHERE productname = item;$$

DROP PROCEDURE product_update;
CREATE PROCEDURE product_update(num INT)
LANGUAGE SQL
AS $$
UPDATE product
SET quantity = quantity - (SELECT quantity FROM test_purchase ORDER BY id DESC LIMIT 1)
WHERE productkey = num;$$

CALL update_product('Indomie');


/*Views*/
CREATE MATERIALIZED VIEW test_view
AS
    SELECT productname, quantity
    FROM
    product
WITH DATA;

REFRESH MATERIALIZED VIEW test_view;

CREATE MATERIALIZED VIEW test2_view
AS
    SELECT t.pk,t.date,t.product,t.quantity,p.price,(t.quantity*p.price) AS total
    FROM test_purchase t, product p
    WHERE t.pk = p.productkey
WITH DATA;

REFRESH MATERIALIZED VIEW test2_view;

SELECT * FROM test_view;


