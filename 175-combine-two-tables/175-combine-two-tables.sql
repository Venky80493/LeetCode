/* Write your T-SQL query statement below */
SELECT t1.firstName, t1.lastname, t2.city, t2.state
from Person t1
left join Address t2
on t1.personId=t2.personId

