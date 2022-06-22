CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        /* Write your T-SQL query statement below. */
        SELECT DISTINCT salary
        FROM (SELECT salary,id, 
              DENSE_RANK() OVER(ORDER BY salary DESC) rank
             FROM Employee)t1
        WHERE rank=@N
        
        
    );
END