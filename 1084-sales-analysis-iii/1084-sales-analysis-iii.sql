SELECT t1.product_id,t3.product_name 
FROM
(SELECT DISTINCT product_id, 1 as quarter1_flag 
                       FROM
                      Sales 
                      WHERE sale_date>='2019-01-01' and sale_date<='2019-03-31') t1
LEFT JOIN (SELECT DISTINCT product_id, 1 as not_quarter1_flag 
                       FROM
                      Sales 
                      WHERE sale_date<'2019-01-01' OR sale_date>'2019-03-31') t2
ON t1.product_id=t2.product_id
LEFT JOIN Product t3
on t1.product_id=t3.product_id
WHERE t2.not_quarter1_flag IS NULL
