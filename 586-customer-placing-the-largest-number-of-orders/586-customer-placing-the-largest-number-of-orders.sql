# Write your MySQL query statement below
select customer_number from(
select customer_number, count(order_number) order_number from
Orders
group by customer_number)t1
order by order_number desc
limit 1