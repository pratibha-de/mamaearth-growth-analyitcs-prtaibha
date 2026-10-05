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
