# Write your MySQL query statement below
​
SELECT customer_number
FROM (
    SELECT customer_number, COUNT(*) as orders
    FROM orders
    GROUP BY customer_number
    ) AS s
ORDER BY s.orders DESC
LIMIT 1
