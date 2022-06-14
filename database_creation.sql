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

