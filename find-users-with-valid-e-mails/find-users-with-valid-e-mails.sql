# Write your MySQL query statement below
SELECT user_id, name, mail
FROM Users
WHERE mail REGEXP '^[a-z][a-z0-9._-]*@leetcode.com'
