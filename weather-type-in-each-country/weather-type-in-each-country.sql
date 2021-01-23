# Write your MySQL query statement below
​
SELECT c.country_name,
CASE WHEN AVG(weather_state)<= 15 THEN 'Cold'
     WHEN AVG(weather_state)>=25 THEN 'Hot'
     ELSE 'Warm' END AS weather_type 
FROM Weather 
LEFT JOIN Countries c USING (country_id)
WHERE LEFT(day,7) = '2019-11'
GROUP BY country_name
​
​
