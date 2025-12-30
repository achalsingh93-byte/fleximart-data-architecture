-- Business Query 1: Total number of customers by city
SELECT 
    city,
    COUNT(*) AS total_customers
FROM customers
GROUP BY city;


-- Business Query 2: Average product price by category
SELECT
    category,
    AVG(price) AS avg_price
FROM products
GROUP BY category;


-- Business Query 3: Total orders placed by each customer
SELECT
    c.first_name,
    c.last_name,
    COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id;
