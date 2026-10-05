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
