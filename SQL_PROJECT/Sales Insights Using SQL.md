## Sales Insights by SQL 
<pre>
use sales; 

<b>1. Find Total number of customers</b>
select count(*) from sales.customers;

<b>2. Show different Markets</b>
select * from markets;

<b>3. Select distinct products sold in 'Mark001' Chennai. </b>
select distinct product_code from transactions 
where market_code='Mark001'; 

<b>4. Find top 5 products sold in Chennai market </b>
select product_code, count(*) as count_of_goods from sales.transactions
where market_code='Mark001'
group by product_code 
order by count_of_goods desc limit 5;

<b>5. Find total transactions in all years and total sales in Chennai </b>
select date.year, count(*) as total_transactions, sum(sales_amount) as total_sales FROM transactions 
INNER JOIN date
ON transactions.order_date = date.date
where transactions.market_code='Mark001'
group by date.year;  

<b>6. Find total sales based on customer type in Chennai year wise</b>
select date.year, customers.customer_type, sum(transactions.sales_amount) as total_sales
FROM transactions
INNER JOIN customers
ON transactions.customer_code = customers.customer_code
INNER JOIN date
on transactions.order_date = date.date
group by customers.customer_type, date.year; 

<b>7. Find average sales_amount transactions of 'own brand' and 'distribution.' year wise</b>

select date.year, p.product_type, sum(t.sales_amount) as total_sales 
from transactions as t
INNER JOIN products as p
ON t.product_code = p.product_code
INNER JOIN date
on t.order_date = date.date
group by p.product_type, date.year; 

<b>8. Find the product with highest sales in the month of 'June'</b>

select d.month_name as mn, t.product_code as pd, sum(t.sales_amount) as sales
from transactions t 
INNER JOIN date d 
ON t.order_date = d.date
where d.month_name = 'June'
group by t.product_code
order by sales desc 
limit 1;

<b>9. Procedure to find quantity sales greater than ten thousand</b>

use sales; 

DELIMITER $$
CREATE PROCEDURE TenKQuantity()
BEGIN 
   SELECT *
    FROM transactions
    where sales_qty>=10000; 
END$$

DELIMITER ; 

CALL TenKQuantity(); 

<b>10. Procedure to find total sales of the specified year and month</b> 
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


<b>11.Procedure to find total revenue of specified product in specified month</b>                                         
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
</pre>
