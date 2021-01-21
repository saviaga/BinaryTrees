# Write your MySQL query statement below
SELECT DISTINCT e1.employee_id, 
                    (SELECT COUNT(*)
                    FROM Employee e2
                    WHERE e1.team_id = e2.team_id) AS team_size
FROM Employee e1
​
​
​
​
​
