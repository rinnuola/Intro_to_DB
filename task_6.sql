SELECT INFORMATION_SCHEMA.COLUMNS.COLUMN_NAME, COLUMN_TYPE, TABLE_SCHEMA, TABLE_NAME, COLUMN_KEY
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'ala_book_store' AND TABLE_NAME = 'Customers';
INSERT INTO Customers (customer_id, customer_name, email, address)
VALUES
(customer_id = 2, customer_name = 'Blessing Malik', email = 'bmalik@sandtech.com', address = '124 Happiness Ave.'),
(customer_id = 3, customer_name = 'Obed Ihoneah', email = 'eobe@sandtech.com', address = '125 Happiness Ave.'),
(customer_id = 4, customer_name = 'Nnehanial Kanoli', email = 'nkanoli@sandtech.com', address = '126 Happiness Ave.');