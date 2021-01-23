# Write your MySQL query statement below
​
SELECT project_id, ROUND(SUM(experience_years)/COUNT(DISTINCT employee_id),2) AS average_years
FROM Project
LEFT JOIN Employee USING (employee_id)
GROUP BY project_id
​
