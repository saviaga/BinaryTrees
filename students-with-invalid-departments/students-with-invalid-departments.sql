# Write your MySQL query statement below
​
SELECT s.id  as id, s.name as name
FROM Students as s
LEFT JOIN Departments as d
ON s.department_id = d.id
WHERE d.id IS NULL
​
​
