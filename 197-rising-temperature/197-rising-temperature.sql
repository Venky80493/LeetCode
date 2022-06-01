/* Write your T-SQL query statement below */
SELECT DISTINCT t1.id
FROM Weather t1
LEFT JOIN Weather t2
ON DATEADD(day,-1,t1.recordDate)=t2.recordDate 
where t1.temperature>t2.temperature