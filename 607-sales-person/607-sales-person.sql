/* Write your T-SQL query statement below */
SELECT DISTINCT t1.name
FROM SalesPerson t1
WHERE sales_id NOT IN
    (SELECT t2.sales_id FROM 
    Orders t2
    LEFT JOIN Company  t3
    ON t2.com_id=t3.com_id
    WHERE t3.name  LIKE '%RED%')
