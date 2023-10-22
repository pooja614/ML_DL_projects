/* SALES INSIGHTS USING SQL
The project aims at exploring the sales data through SQL. 
Different questions are answered by SQL queries. 
*/
use sales;

/* What are the different products sold in Chennai? */

SELECT DISTINCT t.product_code
FROM transactions t
INNER JOIN markets m
ON t.market_code = m.markets_code
WHERE m.markets_name = 'Chennai';

/* What are the Top 5 Products sold in Chennai Market? */

SELECT product_code, COUNT(*) as count_of_goods 
FROM sales.transactions
WHERE market_code='Mark001'
GROUP BY product_code 
ORDER BY count_of_goods 
DESC LIMIT 5;

/* Find the total transactions and total sales in Chennai for different years  */

SELECT date.year, COUNT(*) as total_transactions, SUM(sales_amount) as total_sales 
FROM transactions 
INNER JOIN date
ON transactions.order_date = date.date
WHERE transactions.market_code='Mark001'
GROUP BY date.year;  

/* Find total sales based on customer type in Chennai year wise */
SELECT date.year, customers.customer_type, SUM(transactions.sales_amount) as total_sales
FROM transactions
INNER JOIN customers
ON transactions.customer_code = customers.customer_code
INNER JOIN date
ON transactions.order_date = date.date
GROUP BY customers.customer_type, date.year; 

/* Find average sales_amount transactions of 'own brand' and 'distribution.' year wise */  

select date.year, p.product_type, sum(t.sales_amount) as total_sales 
from transactions as t
INNER JOIN products as p
ON t.product_code = p.product_code
INNER JOIN date
on t.order_date = date.date
group by p.product_type, date.year; 

/* Find the product with highest sales in the month of 'June' */

select d.month_name as mn, t.product_code as pd, sum(t.sales_amount) as sales
from transactions t 
INNER JOIN date d 
ON t.order_date = d.date
where d.month_name = 'June'
group by t.product_code
order by sales desc 
limit 1;

/* Procedure to find quantity sales greater than ten thousand */

DELIMITER $$
CREATE PROCEDURE TenKQuantity()
BEGIN 
   SELECT *
    FROM transactions
    where sales_qty>=10000; 
END$$

DELIMITER ; 

CALL TenKQuantity(); 

/* Procedure to find total sales of the specified year and month */

DELIMITER $$
CREATE PROCEDURE YearlyMonthlySales(year_ INT,  month_ VARCHAR(10))
BEGIN 
   SELECT d.year, d.month_name,SUM(t.sales_amount) 
   FROM transactions as t
   INNER JOIN date as d
   ON t.order_date = d.date 
   WHERE d.year = year_ 
   AND d.month_name = month_ 
   GROUP BY d.year, d.month_name;
END$$ 
   
DELIMITER ; 
   
CALL YearlyMonthlySales(2018, 'July') 

/* Procedure to find total revenue of specified product in specified month */
DELIMITER $$ 
CREATE PROCEDURE TotalRevenueProductByMonth
(month_ VARCHAR(10), prod_ VARCHAR(10))
BEGIN  
SELECT d.month_name, p.product_code, SUM(t.sales_amount) as total_sales from transactions as t
INNER JOIN products as p 
ON t.product_code = p.product_code 
INNER JOIN date as d
ON t.order_date = d.date 
where d.month_name = month_ and p.product_code = prod_
group by d.month_name, p.product_code;
END$$ 

DELIMITER ; 
CALL totalRevenueProductByMonth('June', 'Prod010')

/* Create view of products and sales amount that are above average sales amount */

CREATE VIEW Products_Above_Average_Revenue AS
SELECT t.product_code, p.product_type, t.sales_amount 
FROM transactions t 
INNER JOIN products p
ON t.product_code = p.product_code
WHERE t.sales_amount > (
	SELECT AVG(sales_amount) FROM transactions
    ); 

SELECT * from Products_Above_Average_Revenue;

/* Products and customers with quantity bracket [1000,10000) using
Common table functions */ 

use sales;
WITH cte_qty_brackets AS ( 
	SELECT customer_code, market_code, product_code, 
	(CASE 
	WHEN sales_qty <300 THEN 'less'
	WHEN sales_qty < 1000 THEN 'average'
	WHEN sales_qty <10000 THEN 'medium'
    ELSE 'huge'
	END) qty
FROM transactions

)
SELECT 
DISTINCT customer_code, product_code, market_code, qty
FROM cte_qty_brackets 
WHERE qty = 'medium'
ORDER BY product_code; 

/* Find Top customers with average sales greater than 10k in south zone. */

SELECT t.market_code,m.markets_name, c.custmer_name, avg(sales_amount) as avg_sales
from transactions t 
INNER JOIN customers c
ON t.customer_code = c.customer_code
INNER JOIN markets m 
ON t.market_code = m.markets_code
where t.market_code IN (
				SELECT market_code FROM markets 
				WHERE zone = 'South'
                )  
GROUP BY custmer_name, market_code 
HAVING avg_sales > 10000;

/* Find the total and average sales of different customers and total transactions done by the customers.  */ 

SELECT DISTINCT customer_code,
	SUM(sales_amount) OVER
		(partition by customer_code) AS total_sales,
	COUNT(sales_amount) OVER
		(partition by customer_code) AS total_transactions,
	AVG(sales_amount) OVER
		(partition by customer_code) AS average_sales
FROM transactions
WHERE order_date > '2018-12-31';


