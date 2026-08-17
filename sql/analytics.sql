-- 1. Top 10 Products by Revenue
SELECT
    product_id,
    ROUND(SUM(sales_amount)::numeric, 2) AS total_revenue
FROM fact_sales
GROUP BY product_id
ORDER BY total_revenue DESC
LIMIT 10;