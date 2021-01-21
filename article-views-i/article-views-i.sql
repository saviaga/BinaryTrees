# Write your MySQL query statement below
​
​
SELECT DISTINCT(v1.viewer_id) as id
FROM Views v1
INNER JOIN
Views v2
ON v1.author_id = v2.author_id and v1.viewer_id = v2.author_id
ORDER BY v1.viewer_id ASC
