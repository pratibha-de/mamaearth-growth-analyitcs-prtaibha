-- =============================================================================
-- Task 3 — SQL Reports and Analytical Queries
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Report (a): Order Totals (COUNT, Total Revenue, Average Order Value)
-- output:
-- total_orders: 180
-- total_revenue: 99860.20
-- avg_order_value: 554.78
SELECT 
    COUNT(*) AS total_orders,
    ROUND(SUM(o.quantity * p.price * (1 - COALESCE(o.discount_pct, 0) / 100.0)), 2) AS total_revenue,
    ROUND(AVG(o.quantity * p.price * (1 - COALESCE(o.discount_pct, 0) / 100.0)), 2) AS avg_order_value
FROM orders o
JOIN products p ON o.product_id = p.product_id;

-- -----------------------------------------------------------------------------
-- Report (b): COUNT(*) vs COUNT(column)
-- -----------------------------------------------------------------------------

+--------------+---------------+--------------+
-- total_orders :  180
--rated_orders: 165 
--unrated_orers:15 
SELECT 
    COUNT(*) AS total_orders,
    COUNT(rating) AS rated_orders,
    COUNT(*) - COUNT(rating) AS unrated_orders
FROM orders;


-- -----------------------------------------------------------------------------
-- Report (c): Zero-Match Customer (LEFT JOIN vs NOT IN Verification)
-- -----------------------------------------------------------------------------
-- Query 1 Output:
customer_id: C045
name: Vihan
-- Query 2 Output:
customer_id: C045
name: Vihan
*/

-- Query 1: Using LEFT JOIN and HAVING
SELECT 
    c.customer_id, 
    c.name
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING COUNT(o.order_id) = 0;

-- Query 2: Independent verification using NOT IN
SELECT 
    customer_id, 
    name
FROM customers
WHERE customer_id NOT IN (
    SELECT DISTINCT customer_id 
    FROM orders 
    WHERE customer_id IS NOT NULL
);

    -- -----------------------------------------------------------------------------
-- Report (d): GROUP BY + HAVING (Return Rate Filter)
-- -----------------------------------------------------------------------------
/*
+-----------+--------------+-----------------+-----------------+
| city      | total_orders | returned_orders | return_rate_pct |
+-----------+--------------+-----------------+-----------------+
| Jaipur               19          8             42.1 
| Lucknow              49           15            30.6 
| Bangalore            33           8            24.2 
+-----------+--------------+-----------------+-----------------+
*/
SELECT 
    c.city,
    COUNT(o.order_id) AS total_orders,
    SUM(o.returned) AS returned_orders,
    ROUND((SUM(o.returned) * 100.0 / COUNT(o.order_id)), 1) AS return_rate_pct
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.city
HAVING return_rate_pct > 20.0
ORDER BY return_rate_pct DESC;
FROM customers
WHERE customer_id NOT IN (
    SELECT DISTINCT customer_id 
    FROM orders 
    WHERE customer_id IS NOT NULL
);

-- -----------------------------------------------------------------------------
-- Report (e): Ranking with ORDER BY + LIMIT/OFFSET
-- Tie-break comment: customer_id ASC is added to ensure deterministic sorting order when multiple customers have identical total_spend values.
-- -----------------------------------------------------------------------------
/*
Top 5 Query Output:
+-------------+---------+-------------+
 customer_id  name     total_spend 
+-------------+---------+-------------+
 C043         Reyansh     12920.00 
 C026         Isha         8371.60 
 C008         Meera        4564.60 
 C011         Arjun        4111.00 
 C042         Sanya        3785.00 
+-------------+---------+-------------+

Ranks 3–5 Query Output:
+-------------+-------+-------------+
 customer_id  name   total_spend 
+-------------+-------+-------------+
 C008         Meera      4564.60 
 C011         Arjun      4111.00 
 C042         Sanya      3785.00 
+-------------+-------+-------------+
*/
-- Query 1: Top 5 Customers
SELECT 
    c.customer_id,
    c.name,
    ROUND(SUM(o.quantity * p.price * (1 - COALESCE(o.discount_pct, 0) / 100.0)), 2) AS total_spend
FROM orders o
JOIN products p ON o.product_id = p.product_id
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spend DESC, c.customer_id ASC
LIMIT 5;

-- Query 2: Ranks 3 to 5 (OFFSET 2)
SELECT 
    c.customer_id,
    c.name,
    ROUND(SUM(o.quantity * p.price * (1 - COALESCE(o.discount_pct, 0) / 100.0)), 2) AS total_spend
FROM orders o
JOIN products p ON o.product_id = p.product_id
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_spend DESC, c.customer_id ASC
LIMIT 3 OFFSET 2;

-- -----------------------------------------------------------------------------
-- Report (f): Three-Table JOIN with GROUP BY (Category Revenue)
-- -----------------------------------------------------------------------------
/*
+--------------+-------------+------------------+
| category     | order_count | category_revenue |
+--------------+-------------+------------------+
| Haircare     |          54 |         44956.10 |
| Skincare     |          60 |         27346.00 |
| Babycare     |          30 |         16805.00 |
| PersonalCare |          36 |         10753.10 |
+--------------+-------------+------------------+
*/
SELECT 
    p.category,
    COUNT(o.order_id) AS order_count,
    ROUND(SUM(o.quantity * p.price * (1 - COALESCE(o.discount_pct, 0) / 100.0)), 2) AS category_revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY p.category
ORDER BY category_revenue DESC;
