# Write your MySQL query statement below
​
​
SELECT customer_id,name
FROM Orders 
LEFT JOIN Product USING (product_id)
LEFT JOIN Customers  USING (customer_id) 
GROUP BY customer_id
HAVING SUM(IF(LEFT(order_date, 7) = '2020-06', quantity, 0)* price) >=100
    AND SUM(IF(LEFT(order_date, 7) = '2020-07', quantity, 0)* price) >=100
​
​
​
​
