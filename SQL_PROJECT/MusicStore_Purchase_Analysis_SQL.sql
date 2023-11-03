
/* Q1: How many employees are there in different posts(titles) in the company? */

SELECT title, count(employee_id) FROM employee
GROUP BY title;



/* Q2: Who is the senior most employee? */

SELECT * from employee
ORDER BY levels DESC 
limit 1 



/* Q3: Which countries have most invocies and top values of total invoices? */ 

SELECT billing_country, COUNT(*) as invoice_count, SUM(total) as total_value
FROM invoice 
GROUP BY billing_country 
ORDER BY 2 DESC, 3 DESC 



/* Q4: Inorder to through promotional music festival, we would like to know the city with highest number of invoice totals? */

SELECT billing_city, SUM(total) AS invoice_total
FROM invoice 
GROUP BY billing_city
ORDER BY invoice_total DESC
LIMIT 5;



/* Q5: What is the maximum, average, minimum total_spending spent by the customers */

SELECT
	MAX(c.totals) AS maximum_spending, 
	MIN(c.totals) AS minimum_spending, 
	AVG(c.totals) AS average_spending
	FROM (
		SELECT a.customer_id as customer_id, SUM(total) as totals
		FROM customer a
		JOIN invoice b 
		ON a.customer_id = b.customer_id
		GROUP BY a.customer_id	
	) c  
	


/* Q6: Write query to return email, frist_name, last_name of Pop and Rock music listeners, arrange email alphabetically */

SELECT DISTINCT email, first_name, last_name 
FROM customer c
JOIN invoice i ON c.customer_id = i.customer_id 
JOIN invoice_line il ON i.invoice_id = il.invoice_id
WHERE track_id IN (
	SELECT track_id FROM track
	JOIN genre ON track.genre_id = genre.genre_id 
	WHERE genre.name LIKE 'Rock' OR genre.name LIKE 'Pop'
) 
ORDER BY email;


select * from genre;

/* Q7. Return all the track names of genre 'Classical' longer than the average song length*/

SELECT name, milliseconds 
FROM track 
WHERE milliseconds > (
	SELECT AVG(milliseconds) AS avg_track_length 
	FROM track
   ) 
ORDER BY milliseconds DESC; 
	

	
/* Q8. Enlist the artists who have written the most rock music(Top 10) */

SELECT artist.artist_id, artist.name, COUNT(artist.artist_id) AS total_songs_composed
FROM track
JOIN album ON album.album_id = track.album_id
JOIN artist ON artist.artist_id = album.artist_id 
JOIN genre ON genre.genre_id = track.genre_id 
WHERE genre.name LIKE 'Rock' 
GROUP BY artist.artist_id 
ORDER BY total_songs_composed DESC
LIMIT 10;



/* Q9: How much amount is spent by each customer on best selling artist? */
WITH best_selling_artist AS (
	SELECT artist.artist_id AS artist_id, artist.name AS artist_name, SUM(invoice_line.unit_price * invoice_line.quantity) AS total_sales
	FROM invoice_line 
	JOIN track ON track.track_id = invoice_line.track_id 
	JOIN album ON album.album_id = track.album_id 
	JOIN artist ON artist.artist_id = album.artist_id 
	GROUP BY 1
	ORDER BY 3 DESC
	LIMIT 1
) 
SELECT c.customer_id, c.first_name, c.last_name, bsa.artist_name, SUM(il.unit_price*il.quantity) AS amount_spent
FROM invoice i 
JOIN customer c ON c.customer_id = i.customer_id
JOIN invoice_line il ON il.invoice_id = i.invoice_id
JOIN track t ON t.track_id = il.track_id
JOIN album alb ON alb.album_id = t.album_id
JOIN best_selling_artist bsa ON bsa.artist_id = alb.artist_id
GROUP BY 1,2,3,4
ORDER BY 5 DESC;

/* Q10 : We want to find out the most popular music Genre for each country. We determine the most popular genre as the genre 
with the highest amount of purchases. Write a query that returns each country along with the top Genre. For countries where 
the maximum number of purchases is shared return all Genres. */
WITH popular_genre AS 
(
    SELECT COUNT(invoice_line.quantity) AS purchases, customer.country, genre.name, genre.genre_id, 
	ROW_NUMBER() OVER(PARTITION BY customer.country ORDER BY COUNT(invoice_line.quantity) DESC) AS RowNo 
    FROM invoice_line 
	JOIN invoice ON invoice.invoice_id = invoice_line.invoice_id
	JOIN customer ON customer.customer_id = invoice.customer_id
	JOIN track ON track.track_id = invoice_line.track_id
	JOIN genre ON genre.genre_id = track.genre_id
	GROUP BY 2,3,4
	ORDER BY 2 ASC, 1 DESC
)
SELECT * FROM popular_genre WHERE RowNo <= 1



/*Q11. :Write a query that determines the customer that has spent the most on music for each country. 
Write a query that returns the country along with the top customer and how much they spent. 
For countries where the top amount spent is shared, provide all customers who spent this amount.  */

WITH RECURSIVE 
	customter_with_country AS (
		SELECT customer.customer_id,first_name,last_name,billing_country,SUM(total) AS total_spending
		FROM invoice
		JOIN customer ON customer.customer_id = invoice.customer_id
		GROUP BY 1,2,3,4
		ORDER BY 1,5 DESC),

	country_max_spending AS(
		SELECT billing_country,MAX(total_spending) AS max_spending
		FROM customter_with_country
		GROUP BY billing_country)

SELECT cc.billing_country, cc.total_spending, cc.first_name, cc.last_name, cc.customer_id
FROM customter_with_country cc
JOIN country_max_spending ms
ON cc.billing_country = ms.billing_country
WHERE cc.total_spending = ms.max_spending
ORDER BY 1;

/* */
/* */
/* */
/* */
/* */