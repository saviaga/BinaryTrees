# Write your MySQL query statement below
SELECT DISTINCT (Email) 
FROM Person
WHERE (Email) IN 
(
    SELECT Email
    FROM Person
    GROUP BY EMAIL
    HAVING COUNT(Email) >1
) 
​
