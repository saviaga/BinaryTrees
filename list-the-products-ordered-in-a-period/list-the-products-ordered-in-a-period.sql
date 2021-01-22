# Write your MySQL query statement below
SELECT s.product_name, SUM(unit) as unit
FROM(
    SELECT o.product_id,p.product_name,o.order_date, o.unit
    FROM Orders o
    JOIN Products p ON o.product_id = p.product_id
    WHERE o.order_date BETWEEN '2020-02-01' AND '2020-02-29'
    ) AS s
GROUP BY s.product_id
HAVING SUM(unit) >= 100
​
