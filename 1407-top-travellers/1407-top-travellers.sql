/* Write your T-SQL query statement below */
SELECT t1.name, ISNULL(SUM(distance), 0) travelled_distance
FROM Users t1
LEFT JOIN Rides t2
ON t1.id=t2.user_id
GROUP BY t1.id,t1.name
ORDER BY travelled_distance DESC, t1.name ASC