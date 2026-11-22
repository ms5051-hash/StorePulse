-- Top 10 Products by Revenue
SELECT
    p.product_id,
    p."Description",
    ROUND(SUM(sales_amount)::numeric, 2) AS total_revenue
FROM fact_sales f
JOIN dim_product p
    ON f.product_id = p.product_id  
GROUP BY p.product_id, p."Description"
ORDER BY total_revenue DESC
LIMIT 10;

-- 2. Top 10 customers by total revenue

SELECT
    customer_id,
    ROUND(SUM(sales_amount)::numeric, 2) AS total_revenue
FROM fact_sales
GROUP BY customer_id
ORDER BY total_revenue DESC
LIMIT 10;

-- 3 Monthly Revenue Analysis
SELECT
    d.year,
    d.month,
    ROUND(SUM(f.sales_amount)::numeric, 2) AS monthly_revenue
FROM fact_sales f
JOIN dim_date d
    ON f.date_id = d.date_id
GROUP BY d.year, d.month
ORDER BY monthly_revenue DESC;

-- 4 Top 10 Products by Units Sold
SELECT 
    product_id,
    SUM("Quantity") AS total_units_sold
FROM fact_sales
GROUP BY product_id
ORDER BY total_units_sold DESC
LIMIT 10;

-- 5 Revenue by Country
SELECT 
    c.country,
    ROUND(SUM(f.sales_amount)::numeric, 2) AS total_revenue
FROM fact_sales f
JOIN dim_customer c
    ON f.customer_id = c.customer_id
GROUP BY c.country
ORDER BY total_revenue DESC;

--  6 Overall Sales Performance
SELECT 
    COUNT(*) AS total_transactions,
    SUM("Quantity") AS total_units_sold,
    ROUND(SUM(sales_amount)::numeric, 2) AS total_revenue,
    ROUND(AVG(sales_amount)::numeric, 2) AS average_sales
FROM fact_sales f;


-- 7 Top 10 Highest Spending Customers
SELECT 
    f.customer_id,
    SUM(f.sales_amount) AS revenue

FROM fact_sales f
GROUP BY f.customer_id
ORDER BY revenue DESC
LIMIT 10;

-- 8 Average Product Selling Price
SELECT 
    f.product_id,
    ROUND(AVG(f.UnitPrice)::numeric, 2) AS average_price
FROM fact_sales f
GROUP BY f.product_id
ORDER BY average_price DESC
LIMIT 10;


-- 9 Sales By Hour 
SELECT
    d.hour,
    COUNT(*) AS total_sales,
    SUM(f.sales_amount) AS total_revenue
FROM fact_sales f
JOIN dim_date d
    ON f.date_id = d.date_id
GROUP BY d.hour
ORDER BY total_revenue DESC;

-- 10 Annual Revenue Analysis
SELECT 
    d.year,
    SUM(f.sales_amount) AS total_revenue
FROM fact_sales f
JOIN dim_date d
    ON f.date_id = d.date_id
GROUP BY d.year
ORDER BY total_revenue DESC;





