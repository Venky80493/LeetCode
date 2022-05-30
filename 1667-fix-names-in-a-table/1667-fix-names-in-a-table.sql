# Write your MySQL query statement below
SELECT user_id, 
CONCAT(UPPER(LEFT(name,1)), Lower(RIGHT(name,LENGTH(NAME)-1))) AS name
FROM Users
order by user_id